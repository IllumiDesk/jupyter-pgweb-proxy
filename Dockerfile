FROM jupyter/minimal-notebook:45bfe5a474fa

ARG PGWEB_VERSION=0.11.6

USER root
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y \
    curl \
    unzip \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# install pgweb
ENV PGWEB_VERSION="${PGWEB_VERSION}"
RUN wget -q "https://github.com/sosedoff/pgweb/releases/download/v${PGWEB_VERSION}/pgweb_linux_amd64.zip" \
 && unzip pgweb_linux_amd64.zip -d /usr/bin \
 && mv /usr/bin/pgweb_linux_amd64 /usr/bin/pgweb

# setup package, enable classic extension, build lab extension
USER "${NB_USER}"
RUN mkdir -p "/tmp/jupyter-pgweb-proxy"
COPY . "/tmp/jupyter-pgweb-proxy"
WORKDIR "/tmp/jupyter-pgweb-proxy"
RUN python3 -m pip install . \
 && jupyter serverextension enable --sys-prefix jupyter_server_proxy \
 && jupyter labextension install @jupyterlab/server-proxy \
 && jupyter lab build

# copy configs, update permissions as root
USER root
RUN cp /etc/jupyter/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config_base.py
COPY jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py
RUN fix-permissions /etc/jupyter

USER "${NB_USER}"

WORKDIR "${HOME}"