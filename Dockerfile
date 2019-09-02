FROM python:3
MAINTAINER Laurie Harding-Russell

RUN apt-get update && apt-get install -y blender
