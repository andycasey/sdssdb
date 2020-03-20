#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2018-11-02
# @Filename: catalogdb.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
#
# @Last modified by: José Sánchez-Gallego (gallegoj@uw.edu)
# @Last modified time: 2019-09-23 00:54:42


from peewee import (BigAutoField, BigIntegerField, CharField,
                    DeferredThroughModel, DoubleField, FloatField,
                    ForeignKeyField, IntegerField, ManyToManyField, TextField)

from . import BaseModel, database  # noqa


class CatalogdbModel(BaseModel):

    class Meta:
        database = database
        use_reflection = True
        reflection_options = {'skip_foreign_keys': True}
        primary_key = False


_GaiaDR2TmassBestNeighbourDeferred = DeferredThroughModel()


class AllWise(CatalogdbModel):

    class Meta:
        table_name = 'allwise'
        schema = 'catalogdb'


class TwoMassPsc(CatalogdbModel):

    pts_key = IntegerField(primary_key=True)

    class Meta:
        table_name = 'twomass_psc'
        schema = 'catalogdb'


class GaiaDR2Source(CatalogdbModel):

    source_id = BigIntegerField(primary_key=True)

    tmass_best_sources = ManyToManyField(TwoMassPsc,
                                         through_model=_GaiaDR2TmassBestNeighbourDeferred,
                                         backref='gaia_best_sources')

    class Meta:
        table_name = 'gaia_dr2_source'
        schema = 'catalogdb'


class GaiaDR2Clean(CatalogdbModel):

    source_id = ForeignKeyField(GaiaDR2Source,
                                field='source_id',
                                backref='gaia_clean',
                                lazy_load=True)

    class Meta:
        table_name = 'gaia_dr2_clean'
        schema = 'catalogdb'


class GaiaDR2SDSSDR9BestNeighbour(CatalogdbModel):

    class Meta:
        table_name = 'gaiadr2_sdssdr9_best_neighbour'
        schema = 'catalogdb'


class GalacticGenesis(CatalogdbModel):

    class Meta:
        table_name = 'galactic_genesis'
        schema = 'catalogdb'


class GalacticGenesisBig(CatalogdbModel):

    class Meta:
        table_name = 'galactic_genesis_big'
        schema = 'catalogdb'


class GUVCat(CatalogdbModel):

    class Meta:
        table_name = 'guvcat'
        schema = 'catalogdb'


class KeplerInput10(CatalogdbModel):

    class Meta:
        table_name = 'kepler_input_10'
        schema = 'catalogdb'


class SDSSDR13Photoobj(CatalogdbModel):

    class Meta:
        table_name = 'sdss_dr13_photoobj'
        schema = 'catalogdb'


class SDSSDR14APOGEEStar(CatalogdbModel):

    class Meta:
        table_name = 'sdss_dr14_apogeestar'
        schema = 'catalogdb'


class SDSSDR14APOGEEStarVisit(CatalogdbModel):

    class Meta:
        table_name = 'sdss_dr14_apogeestarvisit'
        schema = 'catalogdb'


class SDSSDR14APOGEEVisit(CatalogdbModel):

    class Meta:
        table_name = 'sdss_dr14_apogeevisit'
        schema = 'catalogdb'


class SDSSDR14ASCAPStar(CatalogdbModel):

    class Meta:
        table_name = 'sdss_dr14_ascapstar'
        schema = 'catalogdb'


class SDSSDR14CannonStar(CatalogdbModel):

    class Meta:
        table_name = 'sdss_dr14_cannonstar'
        schema = 'catalogdb'


class SDSSDR14SpecObj(CatalogdbModel):

    class Meta:
        table_name = 'sdss_dr14_specobj'
        schema = 'catalogdb'


class SDSSDR16SpecObj(SDSSDR14SpecObj):

    class Meta:
        table_name = 'sdss_dr16_specobj'


class TIC_v8(CatalogdbModel):

    class Meta:
        table_name = 'tic_v8'
        schema = 'catalogdb'


class TwoMassClean(CatalogdbModel):

    pts_key = ForeignKeyField(TwoMassPsc,
                              backref='tmass_clean',
                              lazy_load=True)

    class Meta:
        table_name = 'twomass_clean'
        schema = 'catalogdb'


class TwoMassCleanNoNeighbor(CatalogdbModel):

    class Meta:
        table_name = 'twomass_clean_noneighbor'
        schema = 'catalogdb'


class GaiaDR2TmassBestNeighbour(CatalogdbModel):

    source_id = ForeignKeyField(GaiaDR2Source,
                                field='source_id',
                                column_name='source_id',
                                backref='+',
                                lazy_load=False)

    tmass_pts_key = ForeignKeyField(TwoMassPsc,
                                    field='pts_key',
                                    column_name='tmass_pts_key',
                                    backref='+',
                                    lazy_load=False)

    class Meta:
        table_name = 'gaiadr2_tmass_best_neighbour'
        schema = 'catalogdb'


class DR14QV44(CatalogdbModel):

    class Meta:
        table_name = 'dr14q_v4_4'
        schema = 'catalogdb'


class unWISE(CatalogdbModel):

    class Meta:
        table_name = 'unwise'
        schema = 'catalogdb'


class LegacySurveyDR8(CatalogdbModel):

    class Meta:
        table_name = 'legacy_survey_dr8'
        schema = 'catalogdb'


class GaiaUnwiseAgn(CatalogdbModel):

    unwise_objid = ForeignKeyField(unWISE,
                                   lazy_load=True)

    gaia = ForeignKeyField(GaiaDR2Source,
                           lazy_load=True)

    class Meta:
        table_name = 'gaia_unwise_agn'
        schema = 'catalogdb'


class EbosstargetV5(CatalogdbModel):

    class Meta:
        table_name = 'ebosstarget_v5'
        schema = 'catalogdb'


# The following model (BhmSpidersGenericSuperset) does not need to be represented
# as a table in the database it is used only as the parent class of BhmSpidersAGNSuperset,
# BhmSpidersClustersSuperset which are real database tables. I am assuming that PeeWee
# can handle such a scheme without problems. If not, then we will have to duplicate the

class BhmSpidersGenericSuperset(CatalogdbModel):

    # Not using reflection here to preserve Tom's notes.

    pk = BigAutoField()

    # Parameters derived from eROSITA eSASS catalogue
    # Chosen to match X-ray columns defined in eROSITA/SDSS-V MoU (v2.0, April 2019)
    ero_version = TextField(index=True, null=True)  # string identifying this eROSITA data
                                                    # reduction version
    ero_souuid = TextField(index=True, null=True)   # string identifying this X-ray source
    ero_flux = FloatField(null=True)                # X-ray flux, 0.5-8keV band, erg/cm2/s
    ero_flux_err = FloatField(null=True)            # X-ray flux uncertainty, 0.5-8keV band,
                                                    # erg/cm2/s
    ero_ext = FloatField(null=True)                 # X-ray extent parameter - arcsec
    ero_ext_err = FloatField(null=True)             # X-ray extent parameter uncertainty - arcsec
    ero_ext_like = FloatField(null=True)            # X-ray extent likelihood
    ero_det_like = FloatField(null=True)            # X-ray detection likelihood
    ero_ra = DoubleField(index=True, null=True)     # X-ray position, RA, ICRS, degrees
    ero_dec = DoubleField(index=True, null=True)    # X-ray position, Dec, ICRS, degrees
    ero_radec_err = FloatField(null=True)           # X-ray position uncertainty, arcsec

    # Parameters describing the cross-matching of X-ray to optical/IR catalogue(s)

    # 'ML+NWAY', 'LR' , 'SDSS_REDMAPPER', 'LS_REDMAPPER', 'HSC_REDMAPPER', 'MCMF' etc
    xmatch_method = TextField(null=True)
    # version identifier for cross-matching algorithm
    xmatch_version = TextField(null=True)
    # separation between X-ray position and opt positions - arcsec
    xmatch_dist = FloatField(null=True)
    # measure of quality of xmatch (e.g. p_any for Nway, LR)
    xmatch_metric = FloatField(null=True)
    # flavour of match, quality flags, e.g. NWAY match_flag - treat as bitmask
    xmatch_flags = BigIntegerField(null=True)

    # Parameters that describe the major class of the object
    target_class = TextField(null=True)     # TBD, but e.g. 'unknown', 'AGN', 'Star', 'Galaxy'

    target_priority = IntegerField(null=True)  # allows priority ranking based on
                                               # info not available in catalogdb
    target_has_spec = IntegerField(null=True)  # (bitmask) allows flagging of targets
                                               # that have a redshift from a catalogue
                                               # that might not be listed in catalogdb
                                               # follow bit pattern in spec compilation
                                               # values < 0 means 'unknown'

    # Parameters derived from the cross-matched opt/IR catalogue

    # which optical catalogue(and version) provided this counterpart,
    # e.g. 'ls_dr8', 'ps1_dr2' ... will also be the origin of the photometry columns below
    best_opt = TextField(null=True)

    # arithmetically derived from ls_release, ls_brickid and ls_objid
    # ls_id = ls_objid + ls_brickid * 2**16 + ls_release * 2**40
    #  - make sure that we have a common definition within CatalogDB
    # must be used when ls was the main source of counterparts to
    # erosita source, otherwise is optional
    ls_id = BigIntegerField(index=True, null=True)

    # Pan-STARRS1-DR2 object id (= ObjectThin.ObjID = StackObjectThin.ObjID)
    # Must be used when ps1-dr2(+unWISE) was the main source of counterparts
    # to an erosita source, otherwise is optional
    ps1_dr2_objid = BigIntegerField(index=True, null=True)

    # derived from legacysurvey sweeps OPT_REF_ID when OPT_REF_CAT='G2'
    # must be used when ls was the main source of counterparts to erosita source,
    # otherwise is optional
    # - SPIDERS team should also pre-match to gaia dr2 when using counterparts
    # from non-LS catalogues
    gaia_dr2_source_id = BigIntegerField(index=True, null=True)

    # Corresponds to the unWISE catalog band-merged 'unwise_objid'
    #  - should be used when ps1-dr2+unWISE was the main source of
    # counterparts to erosita sources, otherwise is optional
    unwise_dr1_objid = CharField(index=True, null=True, max_length=16)

    # provisional:
    # Corresponds to the DES dr1 coadd_object_id
    #  - must be used when DES-dr1 was the primary source of counterpart to an
    # erosita source, otherwise is optional
    des_dr1_coadd_object_id = BigIntegerField(index=True, null=True)

    # Corresponds to the SDSS DR16 photoObj https://www.sdss.org/dr13/help/glossary/#ObjID
    #  - must be used when SDSS photoObj was the primary source of counterpart
    # to an erosita source, otherwise is optional
    sdss_dr16_objid = BigIntegerField(index=True, null=True)

    # included for convenience, but are copied from columns in other tables
    opt_ra = DoubleField(index=True, null=True)
    opt_dec = DoubleField(index=True, null=True)
    opt_pmra = FloatField(null=True)
    opt_pmdec = FloatField(null=True)
    opt_epoch = FloatField(null=True)

    # For convenience we send a subset of magnitude columns over to the database
    # - the full set of columns is available via a database JOIN to e.g. main ls_dr8 catalogue
    # Note to self: Be careful with use of modelflux, fiberflux, fiber2flux etc!
    opt_modelflux_g = FloatField(null=True)
    opt_modelflux_ivar_g = FloatField(null=True)
    opt_modelflux_r = FloatField(null=True)
    opt_modelflux_ivar_r = FloatField(null=True)
    opt_modelflux_r = FloatField(null=True)
    opt_modelflux_ivar_r = FloatField(null=True)
    opt_modelflux_i = FloatField(null=True)
    opt_modelflux_ivar_i = FloatField(null=True)
    opt_modelflux_z = FloatField(null=True)
    opt_modelflux_ivar_z = FloatField(null=True)

    class Meta:
        table_name = 'bhm_spiders_generic_superset'
        schema = 'catalogdb'
        use_reflection = False


# Note that following models are currently identical in form, but may well diverge in the future

class BhmSpidersAgnSuperset(BhmSpidersGenericSuperset):

    class Meta:
        table_name = 'bhm_spiders_agn_superset'


class BhmSpidersClustersSuperset(BhmSpidersGenericSuperset):

    class Meta:
        table_name = 'bhm_spiders_clusters_superset'


class BhmCsc(CatalogdbModel):

    class Meta:
        table_name = 'bhm_csc'
        schema = 'catalogdb'


class Gaia_DR2_WD_SDSS(CatalogdbModel):

    @property
    def specobj(self):
        """Returns the matching record in `.SDSSDR16SpecObj`."""

        return SDSSDR16SpecObj.get(SDSSDR16SpecObj.plate == self.plate,
                                   SDSSDR16SpecObj.mjd == self.mjd,
                                   SDSSDR16SpecObj.fiberid == self.fiber)

    class Meta:
        table_name = 'gaia_dr2_wd_sdss'
        schema = 'catalogdb'


class Gaia_DR2_WD(CatalogdbModel):

    @property
    def sdss_spectra(self):
        """Returns records from `.Gaia_DR2_WD_SDSS` with matching ``wd``."""

        return Gaia_DR2_WD_SDSS.select().where(Gaia_DR2_WD_SDSS.wd == self.wd)

    class Meta:
        table_name = 'gaia_dr2_wd'
        schema = 'catalogdb'


class Tycho2(CatalogdbModel):

    class Meta:
        table_name = 'tycho2'
        schema = 'catalogdb'


_GaiaDR2TmassBestNeighbourDeferred.set_model(GaiaDR2TmassBestNeighbour)
