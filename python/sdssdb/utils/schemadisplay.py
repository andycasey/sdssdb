#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2018-12-14
# @Filename: peewee_schemadisplay.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
#
# @Last modified by: José Sánchez-Gallego (gallegoj@uw.edu)
# @Last modified time: 2018-12-14 20:46:43

# The following functions are adapted from the sqlalchemy_schemadisplay by
# Florian Schulze (https://github.com/fschulze/sqlalchemy_schemadisplay).

import pydot
from peewee import ForeignKeyField


__all__ = ['create_schema_graph', 'show_schema_graph']


def _render_table_html(model, show_indices=True, show_datatypes=True):
    """Creates the HTML tags for a table, including PKs, FKs, and indices.

    Parameters
    ----------
    model : `peewee.Model`
        The Peewee model for which to create the table.
    show_indices : `bool`
        Whether to show the indices from the table as separate rows.
    show_datatypes : `bool`
        Whether to show the data type of each column.

    """

    table_name = model._meta.table_name
    fields = model._meta.fields

    pk_col_names = set([fields[field_name].column_name for field_name in fields
                        if fields[field_name].primary_key])

    fk_col_names = set([fields[field_name].column_name for field_name in fields
                        if isinstance(fields[field_name], ForeignKeyField)])

    def format_field_str(field):
        """Add in (PK) OR (FK) suffixes to column names."""

        column_name = field.column_name

        suffixes = []

        if column_name in pk_col_names:
            suffixes.append('PK')
        if column_name in fk_col_names:
            suffixes.append('FK')

        suffix = ' (' + ', '.join(suffixes) + ')' if len(suffixes) > 0 else ''

        if show_datatypes:
            return f'- {column_name}{suffix} : {field.field_type}'
        else:
            return f'- {column_name}{suffix}'

    html = (f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">'
            f'<TR><TD ALIGN="CENTER">{table_name}</TD></TR>'
            f'<TR><TD BORDER="1" CELLPADDING="0"></TD></TR>')

    added_col_name = []
    fields_html = []

    # Add a row for each column in the table.
    for field in fields.values():

        column_name = field.column_name

        # Avoids repeating columns. This can happen if there are multiple
        # FKs pointing to the same column.
        if column_name in added_col_name:
            continue

        fields_html.append(
            '<TR><TD ALIGN="LEFT" PORT="{}">{}</TD></TR>'.format(
                column_name, format_field_str(field)))

        added_col_name.append(column_name)

    html += ''.join(fields_html)

    # Add indexes and unique constraints
    if show_indices:

        indexes = [index for index in model._meta.fields_to_index()
                   if not isinstance(index._expressions[0], ForeignKeyField)]

        if len(indexes) > 0:
            html += '<TR><TD BORDER="1" CELLPADDING="0"></TD></TR>'

            for index in indexes:

                column_name = index._expressions[0].column_name

                if index._unique:
                    ilabel = 'UNIQUE'
                else:
                    ilabel = 'INDEX'

                html += f'<TR><TD ALIGN="LEFT">{ilabel} {column_name}</TD></TR>'

    html += '</TABLE>>'

    return html


def create_schema_graph(models=None, base=None, schema=None, show_indices=True,
                        show_datatypes=True, font='Bitstream-Vera Sans',
                        concentrate=True, relation_options={}, rankdir='TB'):
    """Creates a graph visualisation from a series of Peewee models.

    Produces a `pydot <https://pypi.org/project/pydot/>`__ graph including the
    tables and relationships from a series of models or from a base model
    class.

    Parameters
    ----------
    models : `list`
        A list of Peewee `models <peewee:Model>` to be graphed.
    base : `peewee:Model`
        A base model class. If passed, all the model classes that were created
        by subclassing from the base model will be used.
    schema : `str`
        A schema name. If passed, will be used to limit the list of models or
        ``base`` subclasses to only the models that match the schema name.
    show_indices : `bool`
        Whether to show the indices from the table as separate rows.
    show_datatypes : `bool`
        Whether to show the data type of each column.
    font : `str`
        The name of the font to use.
    relation_options : `dict`
        Additional parameters to be passed to ``pydot.Edge`` when creating the
        relationships.

    Returns
    -------
    graph : pydot.Dot
        A ``pydot.Dot`` object with the graph representation of the schema.

    Example
    -------
    ::

        >>> graph = create_schema_graph([User, Tweet])
        >>> graph.write_pdf('tweetdb.pdf')

    """

    assert models or base, 'either model or base must be passed.'

    relation_kwargs = {'fontsize': '7.0'}
    relation_kwargs.update(relation_options)

    if base and not models:
        models = base.__subclasses__()

    if schema:
        models = [model for model in models if model._meta.schema == schema]

    graph = pydot.Dot(prog='dot',
                      mode='ipsep',
                      overlap='ipsep',
                      sep='0.01',
                      concentrate=str(concentrate),
                      rankdir=rankdir)

    for model in models:

        graph.add_node(
            pydot.Node(str(model._meta.table_name),
                       shape='plaintext',
                       label=_render_table_html(model,
                                                show_indices=show_indices,
                                                show_datatypes=show_datatypes),
                       fontname=font,
                       fontsize='7.0')
        )

        for field in model._meta.fields.values():

            if (not isinstance(field, ForeignKeyField) or
                    field.rel_model not in models):
                continue

            from_col_name = field.column_name
            to_col_name = field.rel_field.column_name

            edge = [model._meta.table_name, field.rel_model._meta.table_name]

            # is_inheritance = from_field.primary_key and to_field.primary_key
            # if is_inheritance:
            #     edge = edge[::-1]

            # is_index = from_field.primary_key or from_field.unique

            graph_edge = pydot.Edge(
                dir='both',
                headlabel=f'+ {to_col_name}',
                taillabel=f'+ {from_col_name}',
                arrowhead='none',
                arrowtail='none',
                # arrowhead=is_inheritance and 'none' or 'odot',
                # arrowtail=is_index and 'empty' or 'crow',
                fontname=font,
                *edge,
                **relation_kwargs
            )
            graph.add_edge(graph_edge)

    return graph


def show_schema_graph(*args, **kwargs):
    """Creates and displays a schema graph."""

    from io import StringIO
    from PIL import Image

    iostream = StringIO(create_schema_graph(*args, **kwargs).create_png())
    Image.open(iostream).show(command=kwargs.get('command', 'gwenview'))