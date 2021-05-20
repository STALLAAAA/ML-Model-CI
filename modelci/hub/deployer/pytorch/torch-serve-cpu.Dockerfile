FROM continuumio/miniconda

# set system environment
ENV CONDA_ROOT=/opt/conda
ENV CONDA_PREFIX=${CONDA_ROOT}
ENV PATH=$CONDA_PREFIX/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY ./modelci/hub/deployer/pytorch /server/

WORKDIR /server/

# install build dependencies
RUN apt-get update -y \
 && apt-get install -y libc-dev gcc

# install conda environment
RUN conda env update --name base --file /server/environment.yml \
 && conda install -y pytorch cpuonly -c pytorch -c conda-forge \
 && conda clean -ayf \
 && rm -rf ~/.cache/pip
RUN find ${CONDA_ROOT}/ -follow -type f -name '*.a' -delete 2> /dev/null; exit 0 \
 && find ${CONDA_ROOT}/ -follow -type f -name '*.pyc' -delete 2> /dev/null; exit 0 \
 && find ${CONDA_ROOT}/ -follow -type f -name '*.js.map' -delete 2> /dev/null; exit 0 \
 && find ${CONDA_ROOT}/lib/python*/site-packages/bokeh/server/static \
     -follow -type f -name '*.js' ! -name '*.min.js' -delete 2> /dev/null; exit 0

CMD python pytorch_serve.py
