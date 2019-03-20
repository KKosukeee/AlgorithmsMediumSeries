ARG TAG
FROM python:$TAG
ARG WORKDIR=/home/docker

RUN apt-get update && \
    apt-get install -y \
    git \
    vim \
    htop \
    sudo \
    fish \
    python3-dev \
    python3-numpy \
    python3-pip \
    python3-tk

RUN mkdir -p $WORKDIR

# Install everything else
COPY requirements.txt $WORKDIR

RUN cd $WORKDIR && \
    pip3 install -r requirements.txt && \
    rm requirements.txt

WORKDIR $WORKDIR

ENTRYPOINT ["fish"]