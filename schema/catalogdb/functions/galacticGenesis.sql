\timing

select a.source_id, c.ra, c.dec, c.phot_g_mean_mag b.original_ext_source_id, d.h_m
from catalogdb.gaia_dr2_clean a
inner join catalogdb.gaiadr2_tmass_best_neighbour b on b.source_id = a.source_id
inner join catalogdb.gaia_dr2_source c on c.source_id = a.source_id
inner join catalogdb.twomass_psc d on b.original_ext_source_id = d.designation
limit 10;

\timing