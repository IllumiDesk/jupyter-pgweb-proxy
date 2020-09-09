FROM jupyter/minimal-notebook:latest

USER root
RUN apt-get update \
 && apt-get install -y \
    curl \
    unzip \
    wget

USER root

ENV PGWEB_VERSION=0.11.6

RUN wget -q "https://github.com/sosedoff/pgweb/releases/download/v${PGWEB_VERSION}/pgweb_linux_amd64.zip" \
 && unzip pgweb_linux_amd64.zip -d /usr/bin \
 && mv /usr/bin/pgweb_linux_amd64 /usr/bin/pgweb

USER "${NB_USER}"

COPY . "${HOME}"/
COPY requirements.txt "${HOME}"/
WORKDIR "${HOME}"
RUN python3 -m pip install .
RUN python3 -m pip install -r requirements.txt \
 && jupyter serverextension enable --sys-prefix jupyter_server_proxy \
 && jupyter labextension install @jupyterlab/server-proxy \
 && jupyter lab build

COPY /etc/jupyter/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config_base.py
COPY jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py
RUN fix-permissions /etc/jupyter

USER "${NB_USER}"
