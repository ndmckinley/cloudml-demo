FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python \
        python-dev \
        rsync \
        software-properties-common \
        unzip \
        wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

RUN pip --no-cache-dir install \
        Pillow \
        h5py \
        matplotlib \
        numpy \
        pandas \
        scipy \
        sklearn

RUN pip --no-cache-dir install tensorflow==1.7.0

RUN wget https://raw.githubusercontent.com/tensorflow/models/master/tutorials/image/imagenet/classify_image.py

RUN mkdir /tmp/imagenet/
RUN cd /tmp/imagenet && wget http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz && tar xvfz inception-2015-12-05.tgz
ADD run_imagenet.sh /run_imagenet.sh
VOLUME data

CMD ./run_imagenet.sh
