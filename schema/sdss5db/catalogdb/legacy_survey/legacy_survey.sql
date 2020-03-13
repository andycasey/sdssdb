/*

Schema for Legacy Survey.

Files: /uufs/chpc.utah.edu/common/home/sdss10/sdss5/target/catalogs/legacysurvey/dr8

*/

CREATE TABLE catalogdb.legacy_survey (
    release INTEGER,
    brickid BIGINT,
    brickname TEXT,
    objid BIGINT,
    type TEXT,
    ra DOUBLE PRECISION,
    dec DOUBLE PRECISION,
    ra_ivar REAL,
    dec_ivar REAL,
    dchisq REAL[5],
    ebv REAL,
    flux_g REAL,
    flux_r REAL,
    flux_z REAL,
    flux_w1 REAL,
    flux_w2 REAL,
    flux_w3 REAL,
    flux_w4 REAL,
    flux_ivar_g REAL,
    flux_ivar_r REAL,
    flux_ivar_z REAL,
    flux_ivar_w1 REAL,
    flux_ivar_w2 REAL,
    flux_ivar_w3 REAL,
    flux_ivar_w4 REAL,
    mw_transmission_g REAL,
    mw_transmission_r REAL,
    mw_transmission_z REAL,
    mw_transmission_w1 REAL,
    mw_transmission_w2 REAL,
    mw_transmission_w3 REAL,
    mw_transmission_w4 REAL,
    nobs_g INTEGER,
    nobs_r INTEGER,
    nobs_z INTEGER,
    nobs_w1 INTEGER,
    nobs_w2 INTEGER,
    nobs_w3 INTEGER,
    nobs_w4 INTEGER,
    rchisq_g REAL,
    rchisq_r REAL,
    rchisq_z REAL,
    rchisq_w1 REAL,
    rchisq_w2 REAL,
    rchisq_w3 REAL,
    rchisq_w4 REAL,
    fracflux_g REAL,
    fracflux_r REAL,
    fracflux_z REAL,
    fracflux_w1 REAL,
    fracflux_w2 REAL,
    fracflux_w3 REAL,
    fracflux_w4 REAL,
    fracmasked_g REAL,
    fracmasked_r REAL,
    fracmasked_z REAL,
    fracin_g REAL,
    fracin_r REAL,
    fracin_z REAL,
    anymask_g INTEGER,
    anymask_r INTEGER,
    anymask_z INTEGER,
    allmask_g INTEGER,
    allmask_r INTEGER,
    allmask_z INTEGER,
    wisemask_w1 SMALLINT,
    wisemask_w2 SMALLINT,
    psfsize_g REAL,
    psfsize_r REAL,
    psfsize_z REAL,
    psfdepth_g REAL,
    psfdepth_r REAL,
    psfdepth_z REAL,
    galdepth_g REAL,
    galdepth_r REAL,
    galdepth_z REAL,
    psfdepth_w1 REAL,
    psfdepth_w2 REAL,
    wise_coadd_id TEXT,
    fracdev REAL,
    fracdev_ivar REAL,
    shapedev_r REAL,
    shapedev_r_ivar REAL,
    shapedev_e1 REAL,
    shapedev_e1_ivar REAL,
    shapedev_e2 REAL,
    shapedev_e2_ivar REAL,
    shapeexp_r REAL,
    shapeexp_r_ivar REAL,
    shapeexp_e1 REAL,
    shapeexp_e1_ivar REAL,
    shapeexp_e2 REAL,
    shapeexp_e2_ivar REAL,
    fiberflux_g REAL,
    fiberflux_r REAL,
    fiberflux_z REAL,
    fibertotflux_g REAL,
    fibertotflux_r REAL,
    fibertotflux_z REAL,
    ref_cat TEXT,
    ref_id BIGINT,
    ref_epoch REAL,
    gaia_phot_g_mean_mag REAL,
    gaia_phot_g_mean_flux_over_error REAL,
    gaia_phot_bp_mean_mag REAL,
    gaia_phot_bp_mean_flux_over_error REAL,
    gaia_phot_rp_mean_mag REAL,
    gaia_phot_rp_mean_flux_over_error REAL,
    gaia_astrometric_excess_noise REAL,
    gaia_duplicated_source BOOL,
    gaia_phot_bp_rp_excess_factor REAL,
    gaia_astrometric_sigma5d_max REAL,
    gaia_astrometric_params_solved SMALLINT,
    parallax REAL,
    parallax_ivar REAL,
    pmra REAL,
    pmra_ivar REAL,
    pmdec REAL,
    pmdec_ivar REAL,
    maskbits INTEGER
) WITHOUT OIDS;


-- Add the serial PK after copying the data.
ALTER TABLE catalogdb.legacy_survey ADD COLUMN pk BIGSERIAL PRIMARY KEY;
