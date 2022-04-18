-- https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_crossmatches/ssec_dm_tmass_psc_xsc_neighbourhood.html

create table catalogdb.gaia_edr3_tmass_psc_xsc_neighbourhood(
source_id bigint, -- Unique Gaia source identifier (long)
original_ext_source_id text, -- Original External Catalogue source identifier (string)
angular_distance real, -- Angular Distance between the two sources (float, Angle[arcsec])
score double precision, -- Score of neighbours (double)
xm_flag smallint, -- Cross-match algorithm flag (short)
clean_tmass_psc_xsc_oid bigint -- External Catalogue source identifier (int)
);
