# continuum.io is the org that maintains and distributes anaconda / miniconda3
FROM continuumio/miniconda3 as base
 
# Set working directory for the project
WORKDIR /usr/src/app
 
# Install dependencies required by python libs
RUN apt-get update
RUN apt-get install -y -q libxi6 libgconf-2-4 libxfixes-dev libxcursor1 libxdamage-dev libxcomposite-dev libxrandr-dev libxinerama1 build-essential

# Create Conda environment centrally installing graph-tool and using python2
RUN conda create --name gt -c conda-forge graph-tool python=2.7

# Install python dependencies
COPY requirements.txt .
RUN conda install -n gt pip
RUN conda run -n gt /bin/bash -c "python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt"

# Determine node granularity when parsing traceroutes in to graph
#       one of 'asn', 'bgp_pfx' or 'pfx'
ENV NODE_GRANULARITY="asn" \
    GLOBAL_DATE="abc"

# Override default shell and use bash
SHELL ["conda", "run", "-n", "gt", "/bin/bash", "-c"]


# Install non-pip mkit dependency from source
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
    touch /home/root/data/20180218.json && \
    echo '{"meta": { "total_count": 0 }, "objects": [] }' > /home/root/data/20180218.json

RUN touch /home/root/data/CAIDA_AS2ORG.dat

# Python program to run in the container
COPY . .

FROM base as test
ENTRYPOINT ["conda", "run", "-n", "gt", "python", "script.py"]

FROM base as parse_traces_offline
CMD [ "sh", "-c", "python ./parse_traces_offline.py $NODE_GRANULARITY $GLOBAL_DATE" ]


FROM base as build_sim_bgp_graphs
CMD [ "sh", "-c", "python ./build_sim_bgp_graphs.py"]


FROM base as api
CMD [ "sh", "-c", "python ./api.py" ]

FROM base as combine_dags
CMD [ "sh", "-c", "python ./combine_dags_src_dst.py" ]
