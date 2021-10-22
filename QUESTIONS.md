## Q `RIPE_PROBE_DATA`

What goes in `RIPE_PROBE_DATA` to satisfy mkit/ripteatlas/probes.py `init_probeset()`?
It seems to be looking for a json file `"/home/%s/data/20180218.json" % user` which is
probably some seed probe data. 

### A:



## Q `PFX2ASN_DIR`
Should `PFX2ASN_DIR` -- presumably where IP to ASN data is stored -- match the
`PFX2ASN_DATA_OLD` or `PFX2ASN_DATA_v6` fields from mkit or are they 
independent values?


## Q Missing `settings` module in api.py

Should there be a file settings.py locally that stores something to change the
way the api runs or is there some python2 `settings` module that is pulled from
a repo somewhere?


## Q `RIPE_PROBE_METADATA`

What needs to go in this value? it seems like this has to go in consts.py\?


## Q `CAIDA_AS2ORG`

where do we get the files for `CAIDA_AS2ORG` from?

## Q  Example consts file 

Would it be possible to get an example consts file with annotations about
the purpose of each value, and source for any that are file paths to data
sources expected by the app



## Directory layout - 
```txt
.
├── api.py
├── build_sim_bgp_graphs.py
├── combine_dags_src_dst.py
├── consts.py
├── data
│   ├── PFX2ASN
│   └── RIPE_DUMPS
├── docker
│   └── Dockerfile
├── Makefile
├── parse_traces_offline.py
├── QUESTIONS.md
├── README.md
├── requirements.txt
├── ripe_atlas_helpers
│   ├── get_ripe_msm_ids.py
│   └── sanity_check_msms.py
├── settings.py
├── tools
│   ├── convert_caida_to_cyclops.py
│   ├── DAG.py
│   └── internet_tools.py
└── topology_discovery
    ├── get_greedy_mmts.py
    ├── get_ripe_measurement.py
    └── greedy_adaptive.py
```
