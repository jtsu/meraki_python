
# Basic  Docker Commands examples

# Build container from Dockerfile in current path
# docker build -t downey .

# Run container
# docker run -it -v /Users/jtsu/Desktop/DowneyDocker/myScripts:/myScripts -w /myScripts downey bash
# -v: volume - map local host path to container path
# -w: working dir in container
# -it: interactive model
# downey bash: container_name command


FROM python:latest
RUN apt-get update
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get install -y curl nano git 
RUN pip install requests
RUN pip install meraki


