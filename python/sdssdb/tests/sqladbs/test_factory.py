# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Filename: test_testdb.py
# Project: sqladbs
# Author: Brian Cherinka
# Created: Sunday, 1st March 2020 3:17:17 pm
# License: BSD 3-clause "New" or "Revised" License
# Copyright (c) 2020 Brian Cherinka
# Last Modified: Monday, 23rd March 2020 6:19:07 pm
# Modified By: Brian Cherinka


from __future__ import print_function, division, absolute_import

import pytest
from sdssdb.tests.sqladbs import models, database


@pytest.fixture(scope='function', autouse=True)
def fix_session(user_factory):
    ''' fixture to replace factory session with real db session after initialization '''
    user_factory._meta.sqlalchemy_session = database.Session


@pytest.fixture()
def batchit(user_factory):
    user_factory.create_batch(10)


class TestFactory(object):

    def test_factory_fixture(self, session, user_factory):
        ''' test the factory can create new entries '''
        print('tf', user_factory._meta.sqlalchemy_session, database.Session)
        table = user_factory(name="Test Human")
        assert table.id == 0
        assert table.name == "Test Human"
        assert table.essence == 'human'

    def test_a_transaction(self, session, batchit):
        rows = session.query(models.User).all()
        print('rows', rows)
        assert len(rows) == 11

    def test_model_fixture(self, user):
        ''' test a single new instance of model Table is created '''
        assert isinstance(user, models.User)
        assert user.essence == 'human'
        assert user.name != 'Test Human'
