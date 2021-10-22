FROM python:2 as base
WORKDIR /usr/src/app

# How to determine node granularity when parsing traceroutes in to graph
#       one of 'asn', 'bgp_pfx' or 'pfx'
ENV NODE_GRANULARITY="asn" \
    GLOBAL_DATE="abc"

# Install dependencies
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install non-pip dependency
RUN git clone https://github.com/racheesingh/m-kit.git && \
    cd m-kit && python setup.py install
# mkit expects a set of probes in /home/${user}/data/20180218.json and a csv
# list of IXPs in /home/${user}/data/all_ixps.csv in order to init 
# the library (i.e. on import)
RUN mkdir -p /home/root/data/ && \
    touch /home/root/data/all_ixps.csv && \
    touch /home/root/data/routeviews-rv2-20160101-1200.pfx2as && \
    touch /home/root/data/routeviews-rv6-20161224-1200.pfx2as && \
    touch /home/root/data/GeoIPASNum.dat && \
    echo '{"meta": { "total_count": 0 }, "objects": [] }' > /home/root/data/20180218.json

RUN touch /home/root/data/CAIDA_AS2ORG.dat

COPY . .

FROM base as parse_traces_offline
CMD [ "sh", "-c", "python ./parse_traces_offline.py $NODE_GRANULARITY $GLOBAL_DATE" ]


FROM base as build_sim_bgp_graphs
CMD [ "sh", "-c", "python ./parse_traces_offline.py $NODE_GRANULARITY $GLOBAL_DATE" ]


FROM base as api
CMD [ "sh", "-c", "python ./parse_traces_offline.py $NODE_GRANULARITY $GLOBAL_DATE" ]

FROM base as combine_dags
CMD [ "sh", "-c", "python ./parse_traces_offline.py $NODE_GRANULARITY $GLOBAL_DATE" ]
