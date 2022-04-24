FROM ubuntu:18.04

# non interactive frontend for locales
ARG DEBIAN_FRONTEND=noninteractive

# installing texlive and utils
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget pandoc texlive-full biber latexmk make git procps openssh-client locales curl python3-pip \
    && apt-get clean \
    && apt-get autoremove -y

# generating locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8 LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8

# installing cpanm & missing latexindent dependencies
RUN curl -L http://cpanmin.us | perl - --self-upgrade && \
    cpanm Log::Dispatch::File YAML::Tiny File::HomeDir
