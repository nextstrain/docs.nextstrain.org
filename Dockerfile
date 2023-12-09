FROM continuumio/miniconda3:4.9.2

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=user
ARG GROUP=user
ARG UID=1000
ARG GID=1000

ENV TERM="xterm-256color"
ENV HOME="/home/user"

RUN set -x \
  && mkdir -p ${HOME}/data \
  && addgroup --system --gid ${GID} ${GROUP} \
  && useradd --system --create-home --home-dir ${HOME} \
  --shell /bin/bash \
  --gid ${GROUP} \
  --groups sudo \
  --uid ${UID} \
  ${USER} \
  && touch ${HOME}.hushlogin

RUN set -x \
  && chown -R ${USER}:${GROUP} ${HOME}

COPY conda.yml ${HOME}/src/

WORKDIR ${HOME}/src

RUN set -x \
  && conda env create --file conda.yml

USER ${USER}

RUN set -x \
  && conda init bash \
  && echo "conda activate docs.nextstrain.org" >> ${HOME}/.bashrc

CMD bash -c "set -x \
  && source ${HOME}/.bashrc \
  && make html \
  "
