# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=ubcdsci/r-dsci-100
FROM $BASE_CONTAINER
LABEL maintainer="Elijah Willie <ewillie@cmmt.ubc.ca"

# Install jupyter extensions (nbgitpuller, git and jupytext)
USER root

# Install Python packages on conda-forge
RUN conda install --quiet --yes -c conda-forge \
    altair \
    black \
    flake8 \
    flake8-nb \
    isort \
    pytest \
    xlrd
    
RUN jupyter labextension install jupyterlab-flake8 \
    && jupyter labextension install @ryantam626/jupyterlab_code_formatter \
    && pip install jupyterlab_code_formatter \
    && jupyter serverextension enable --py jupyterlab_code_formatter --sys-prefix\
    && jupyter lab build 

USER jupyter

# Configure jupyter user
ENV NB_USER=jupyter \
    NB_UID=9999
ENV HOME=/home/$NB_USER
WORKDIR $HOME
