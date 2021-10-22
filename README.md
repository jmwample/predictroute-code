# PredictRoute

To Start using PredictRoute, follow these steps:

1. Create a file `consts.py` with directories that contain your traceroute datasets. The location of the traceroutes is used in `api.py`.
2. Download RIPE traceroutes either from the RIPE measurement page or from the FTP link with daily dumps of public traces.
3. Store RIPE traces at a location defined in `consts.py` called `RIPE_DAILY_DUMPS`.
4. `parse_traces_offline.py` will create several processes to parse these daily dumps, one for each day's compressed traceroutes. This code mainly refers to `compute_dest_based_graphs_offline` which has much of the logic for parsing large quantities of traceroute data in parallel, creating graphs at prefix or ASN level and committing them to disk.
5. The graphs are stored in `.gt` format which can be opened using the `graph-tool` library.
6. Once the graphs for a single day's worth of traces are stored, they are combined with graphs from before. This job is done by `combine_dags_src_dst.py`.
7. The processes of downloading, parsing, building graphs  and combining them with previous graphs can be easily made into cron jobs. Shell scripts to run this code are also checked into the repo.

## Required Files && Global Vars

Both the PredictRoute library and it's dependency
[m-kit](https://github.com/racheesingh/m-kit) require various
data source files and Global Const variables (mostly filepaths for data
management). These are enumerated here with information about where to find
download required data.

### PredictRoute

Variables that **must** be defined in `consts.py`:

- `RIPE_DAILY_DUMPS` - path to directory where daily RIPE Atlas data will be pulled. When processing traceroutes `parse_traces_offline.py` checks the date in the fname; if running using the `global_date` option (`sys.argv[2]`) it will only include files for the specified date, otherwise all days will be processed.

- `PFX2ASN_DIR`

- `RIPE_PROBE_METADATA`

- `ATLAS_API_KEY_PG` - probably want this in consts (don't publish)
- `ATLAS_API_KEY_RS` - probably want this in consts (don't publish)
- `ATLAS_API_KEY_RS2` -

- `CAIDA_AS2ORG` - File path pointing to CAIDA ASN to Organization data described below.

Files:

- `CAIDA_AS2ORG.dat` - Required by `api.py` (and anything that imorts it), this data source provides ASN to Organization mappings as maintained by CAIDA. This is descibed on the [CAIDA AS2ORG](https://www.caida.org/archive/as2org/) site and the data can be [downloaded here](https://www.caida.org/catalog/datasets/as-organizations/). Note - this data updates 3-4 times per year.

### M-Kit

These files are required by the [m-kit](https://github.com/racheesingh/m-kit) library as they are parsed on init (import). The paths are fixed, with the exception of the username which is added in on import - so the path should reflect whatever user will be running the python files.

- `/home/${USER}/data/all_ixps.csv`

- `/home/${USER}/data/routeviews-rv2-20160101-1200.pfx2as`

- `/home/${USER}/data/routeviews-rv6-20161224-1200.pfx2as`

- `/home/${USER}/data/GeoIPASNum.dat`

- `/home/${USER}/data/20180218.json`

## Workflow

The HTTP api is used to query and access predicted routes. This is done by running the `api.py` script. The API requires generated, processed, and merged DAGs. This is done periodically using the helper files. The worflow is pictured below.

<img title="tmp_workflow_placholder" alt="Tmp workflow placeholder" src="https://3.bp.blogspot.com/--GsolnJQBdc/UiD3wCgDRyI/AAAAAAAAAUM/L3H8AtE03sQ/s1600/Cat.jpg">
