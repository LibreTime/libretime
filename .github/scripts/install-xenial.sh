#!/usr/bin/env bash

# Adding repos and packages
add-apt-repository -y ppa:libretime/libretime
apt-get -q update
apt-get install -y \
  ffmpeg \
  liquidsoap \
  liquidsoap-plugin-faad \
  liquidsoap-plugin-lame \
  liquidsoap-plugin-mad \
  liquidsoap-plugin-vorbis \
  python3-setuptools \
  silan

# Making log directory for PHP tests
mkdir -p $LIBRETIME_LOG_DIR
chown runner:runner $LIBRETIME_LOG_DIR
