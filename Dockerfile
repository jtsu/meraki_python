# Copyright (c) 2021 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.1 (the "License"). You may obtain a copy of the
# License at
#               https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
# ########################################################################
# Basic  Docker Commands examples
# docker build -t downey .
# docker run -it downey bash

FROM python:latest
RUN apt-get update
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get install -y curl nano git 
RUN pip install requests
RUN pip install meraki


