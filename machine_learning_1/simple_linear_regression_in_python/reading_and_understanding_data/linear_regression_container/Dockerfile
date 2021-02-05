FROM ubuntu:18.04
MAINTAINER "Anshul Chandra"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
        libopencv-dev \
        python3-pip \
        python3-opencv && \
     rm -rf /var/lib/apt/lists/*

RUN pip3 install tensorflow && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter pyyaml h5py && \
    pip3 install keras --no-deps && \
    pip3 install opencv-python && \
    pip3 install imutils

RUN ["mkdir", "notebooks"]
COPY conf/.jupyter /root/.jupyter
COPY run_jupyter.sh /

#jupyter and tensorboard ports
EXPOSE 8888 6006

#store notebooks in the mounted directory
VOLUME /notebooks

CMD ["/run_jupyter.sh"]

