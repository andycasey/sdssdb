/*

schema for gaia dr2 source

data model:
https://gea.esac.esa.int/archive/documentation/GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html

notes: byte value (astrometric_params_solved, phot_proc_mode) stored as integer



to run:
psql -f gaia_dr2.sql -U sdss sdss5db

drop schema catalogdb cascade;
*/


CREATE TABLE catalogdb.gaia_dr2_source (
    solution_id bigint,
    designation text,
    source_id bigint,
    random_index bigint,
    ref_epoch double precision,
    ra double precision,
    ra_error double precision,
    dec double precision,
    dec_error double precision,
    parallax double precision,
    parallax_error double precision,
    parallax_over_error real,
    pmra double precision,
    pmra_error double precision,
    pmdec double precision,
    pmdec_error double precision,
    ra_dec_corr real,
    ra_parallax_corr real,
    ra_pmra_corr real,
    ra_pmdec_corr real,
    dec_parallax_corr real,
    dec_pmra_corr real,
    dec_pmdec_corr real,
    parallax_pmra_corr real,
    parallax_pmdec_corr real,
    pmra_pmdec_corr real,
    astrometric_n_obs_al integer,
    astrometric_n_obs_ac integer,
    astrometric_n_good_obs_al integer,
    astrometric_n_bad_obs_al integer,
    astrometric_gof_al real,
    astrometric_chi2_al real,
    astrometric_excess_noise double precision,
    astrometric_excess_noise_sig double precision,
    astrometric_params_solved integer,
    astrometric_primary_flag boolean,
    astrometric_weight_al real,
    astrometric_pseudo_colour double precision,
    astrometric_pseudo_colour_error double precision,
    mean_varpi_factor_al real,
    astrometric_matched_observations smallint,
    visibility_periods_used smallint,
    astrometric_sigma5d_max real,
    frame_rotator_object_type integer,
    matched_observations smallint,
    duplicated_source boolean,
    phot_g_n_obs integer,
    phot_g_mean_flux double precision,
    phot_g_mean_flux_error double precision,
    phot_g_mean_flux_over_error real,
    phot_g_mean_mag real,
    phot_bp_n_obs integer,
    phot_bp_mean_flux double precision,
    phot_bp_mean_flux_error double precision,
    phot_bp_mean_flux_over_error real,
    phot_bp_mean_mag real,
    phot_rp_n_obs integer,
    phot_rp_mean_flux double precision,
    phot_rp_mean_flux_error double precision,
    phot_rp_mean_flux_over_error real,
    phot_rp_mean_mag real,
    phot_bp_rp_excess_factor real,
    phot_proc_mode integer,
    bp_rp real,
    bp_g real,
    g_rp real,
    radial_velocity double precision,
    radial_velocity_error double precision,
    rv_nb_transits integer,
    rv_template_teff real,
    rv_template_logg real,
    rv_template_fe_h real,
    phot_variable_flag text,
    l double precision,
    b double precision,
    ecl_lon double precision,
    ecl_lat double precision,
    priam_flags bigint,
    teff_val real,
    teff_percentile_lower real,
    teff_percentile_upper real,
    a_g_val real,
    a_g_percentile_lower real,
    a_g_percentile_upper real,
    e_bp_min_rp_val real,
    e_bp_min_rp_percentile_lower real,
    e_bp_min_rp_percentile_upper real,
    flame_flags bigint,
    radius_val real,
    radius_percentile_lower real,
    radius_percentile_upper real,
    lum_val real,
    lum_percentile_lower real,
    lum_percentile_upper real);



