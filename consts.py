

# Make sure this terminates with a '/' since filenames will be appended raw.
PFX2ASN_DIR = "./data/PFX2ASN/"

# File path pointing to CAIDA ASN to Organization. Required by `api.py` (and
# anything that imorts it), this data source provides ASN to Organization
# mappings as maintained by CAIDA. This is descibed on the
# [CAIDA AS2ORG](https://www.caida.org/archive/as2org/) site and the data can be
# [downloaded here](https://www.caida.org/catalog/datasets/as-organizations/).
CAIDA_AS2ORG = "/home/root/data/CAIDA_AS2ORG.dat"

# file path format string to historical traceroute data. Format specifier in
# `api.py` expects to add the node granularity and a file identifier.
HIST_DATA = ""

# Path to directory where daily RIPE Atlas data will be pulled. When processing
# traceroutes parse_traces_offline.py checks the date in the fname; if running
# using the global_date option (sys.argv[2]) it will only include files for the
# specified date, otherwise all days will be processed. The location of the
# traceroutes is used in api.py.
RIPE_DAILY_DUMPS = "./data/RIPE_DUMPS"
RIPE_PROBE_METADATA = "/home/root/data/20180218.json"

# RIPE API Key (DO NOT PUBLISH)
ATLAS_API_KEY = ""
