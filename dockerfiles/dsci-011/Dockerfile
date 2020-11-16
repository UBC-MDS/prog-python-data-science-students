# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER
LABEL maintainer="Elijah Willie <ewillie@cmmt.ubc.ca"

# Install Python packages on conda-forge
RUN conda install --quiet --yes -c conda-forge \
    altair=4.* \
    black=19.* \
    flake8=3.* \
    pytest=6.* \
    isort \
    pytest \
    xlrd \
    graphviz \
    python-graphviz \
    scikit-learn \
    xgboost \
    matplotlib 

# Install jupyter extensions (nbgitpuller, git and jupytext)
USER root

RUN pip install git+https://github.com/data-8/nbgitpuller \
    && pip install git+https://github.com/altair-viz/altair_saver \
    && jupyter serverextension enable --sys-prefix nbgitpuller \
    && jupyter labextension install @jupyterlab/git \
    && pip install jupyterlab-git \
    && jupyter serverextension enable --py jupyterlab_git \
    && pip install jupytext --upgrade \
    && jupyter labextension install jupyterlab-flake8 \
    && jupyter labextension install @ryantam626/jupyterlab_code_formatter \
    && pip install jupyterlab_code_formatter \
    && jupyter serverextension enable --py jupyterlab_code_formatter --sys-prefix\
    && pip install black isort \
    && jupyter lab build  \
    && pip install flake8-nb
    
RUN useradd -m -s /bin/bash -N -u 9999 jupyter

USER jupyter

# Configure jupyter user
ENV NB_USER=jupyter \
    NB_UID=9999
ENV HOME=/home/$NB_USER
WORKDIR $HOME
