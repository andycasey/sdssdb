/*

AAVSO Cataclysmic Variables

*/

CREATE TABLE catalogdb.cataclysmic_variables (
    ref_id BIGINT,
    solution_id BIGINT,
    designation TEXT,
    source_id BIGINT,
    random_index INTEGER,
    ref_epoch REAL,
    ra DOUBLE PRECISION,
    ra_error DOUBLE PRECISION,
    dec DOUBLE PRECISION,
    dec_error DOUBLE PRECISION,
    parallax DOUBLE PRECISION,
    parallax_error DOUBLE PRECISION,
    parallax_over_error DOUBLE PRECISION,
    pmra DOUBLE PRECISION,
    pmra_error DOUBLE PRECISION,
    pmdec DOUBLE PRECISION,
    pmdec_error DOUBLE PRECISION,
    ra_dec_corr DOUBLE PRECISION,
    ra_parallax_corr DOUBLE PRECISION,
    ra_pmra_corr DOUBLE PRECISION,
    ra_pmdec_corr DOUBLE PRECISION,
    dec_parallax_corr DOUBLE PRECISION,
    dec_pmra_corr DOUBLE PRECISION,
    dec_pmdec_corr DOUBLE PRECISION,
    parallax_pmra_corr DOUBLE PRECISION,
    parallax_pmdec_corr DOUBLE PRECISION,
    pmra_pmdec_corr DOUBLE PRECISION,
    astrometric_n_obs_al SMALLINT,
    astrometric_n_obs_ac SMALLINT,
    astrometric_n_good_obs_al SMALLINT,
    astrometric_n_bad_obs_al SMALLINT,
    astrometric_gof_al DOUBLE PRECISION,
    astrometric_chi2_al DOUBLE PRECISION,
    astrometric_excess_noise DOUBLE PRECISION,
    astrometric_excess_noise_sig DOUBLE PRECISION,
    astrometric_params_solved SMALLINT,
    astrometric_primary_flag BOOLEAN,
    astrometric_weight_al DOUBLE PRECISION,
    astrometric_pseudo_colour DOUBLE PRECISION,
    astrometric_pseudo_colour_error DOUBLE PRECISION,
    mean_varpi_factor_al DOUBLE PRECISION,
    astrometric_matched_observations SMALLINT,
    visibility_periods_used SMALLINT,
    astrometric_sigma5d_max DOUBLE PRECISION,
    frame_rotator_object_type SMALLINT,
    matched_observations SMALLINT,
    duplicated_source BOOLEAN,
    phot_g_n_obs SMALLINT,
    phot_g_mean_flux DOUBLE PRECISION,
    phot_g_mean_flux_error DOUBLE PRECISION,
    phot_g_mean_flux_over_error DOUBLE PRECISION,
    phot_g_mean_mag DOUBLE PRECISION,
    phot_bp_n_obs SMALLINT,
    phot_bp_mean_flux DOUBLE PRECISION,
    phot_bp_mean_flux_error DOUBLE PRECISION,
    phot_bp_mean_flux_over_error DOUBLE PRECISION,
    phot_bp_mean_mag DOUBLE PRECISION,
    phot_rp_n_obs SMALLINT,
    phot_rp_mean_flux DOUBLE PRECISION,
    phot_rp_mean_flux_error DOUBLE PRECISION,
    phot_rp_mean_flux_over_error DOUBLE PRECISION,
    phot_rp_mean_mag DOUBLE PRECISION,
    phot_bp_rp_excess_factor DOUBLE PRECISION,
    phot_proc_mode SMALLINT,
    bp_rp DOUBLE PRECISION,
    bp_g DOUBLE PRECISION,
    g_rp DOUBLE PRECISION,
    radial_velocity DOUBLE PRECISION,
    radial_velocity_error DOUBLE PRECISION,
    rv_nb_transits SMALLINT,
    rv_template_teff REAL,
    rv_template_logg REAL,
    rv_template_fe_h REAL,
    phot_variable_flag TEXT,
    l DOUBLE PRECISION,
    b DOUBLE PRECISION,
    ecl_lon DOUBLE PRECISION,
    ecl_lat DOUBLE PRECISION,
    priam_flags INTEGER,
    teff_val DOUBLE PRECISION,
    teff_percentile_lower DOUBLE PRECISION,
    teff_percentile_upper DOUBLE PRECISION,
    a_g_val REAL,
    a_g_percentile_lower REAL,
    a_g_percentile_upper REAL,
    e_bp_min_rp_val REAL,
    e_bp_min_rp_percentile_lower REAL,
    e_bp_min_rp_percentile_upper REAL,
    flame_flags INTEGER,
    radius_val DOUBLE PRECISION,
    radius_percentile_lower DOUBLE PRECISION,
    radius_percentile_upper DOUBLE PRECISION,
    lum_val DOUBLE PRECISION,
    lum_percentile_lower DOUBLE PRECISION,
    lum_percentile_upper DOUBLE PRECISION
);

ALTER TABLE catalogdb.cataclysmic_variables ADD PRIMARY KEY (ref_id);

CREATE INDEX CONCURRENTLY ON catalogdb.cataclysmic_variables (q3c_ang2ipix(ra, dec));
CLUSTER cataclysmic_variables_q3c_ang2ipix_idx ON catalogdb.cataclysmic_variables;
ANALYZE catalogdb.cataclysmic_variables;