# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

ARG BASE_CONTAINER=ubcdsci/r-dsci-100
FROM $BASE_CONTAINER
LABEL maintainer="Elijah Willie <ewillie@cmmt.ubc.ca"

# Install jupyter extensions (nbgitpuller, git and jupytext)
USER root

# Install Python packages on conda-forge
RUN conda config --add channels conda-forge
RUN conda install --quiet --yes -c conda-forge \
    altair \
    black \
    flake8 \
    panel \
    dash-html-components \
    dash-core-components \
    dash-bootstrap-components \
    altair_data_server \
    jupyter-server-proxy \
    altair_saver \
    vega_datasets \
    dash \
    flake8-nb \
    isort \
    pytest \
    xlrd= \
    openpyxl \
    python-graphviz \
    scikit-learn \
    xgboost \
    matplotlib

# version of altair_data_server that works with subfolders on a JupyterHub
# will replace with installation from https://github.com/altair-viz/altair_data_server
# once this PR is merged
RUN pip install -U git+https://github.com/yuvipanda/altair_data_server@better-hub-support-2

RUN jupyter labextension install jupyterlab-flake8 \
    && pip install git+https://github.com/data-8/nbgitpuller \
    && pip install jupyterlab_code_formatter \
    && pip install jupyterlab-git \
    && pip install jupytext --upgrade \
    && jupyter lab build

USER jupyter

COPY rm-merge-shortcut.py /tmp/user-settings/\@jupyterlab/shortcuts-extension/shortcuts.jupyterlab-settings

# Configure jupyter user
ENV NB_USER=jupyter \
    NB_UID=9999
ENV HOME=/home/$NB_USER
WORKDIR $HOME
