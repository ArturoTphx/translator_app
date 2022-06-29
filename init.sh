#!/bin/bash
sudo chmod 666 /var/run/docker.sock
docker image build -t translator .
docker run -p 5000:5000 -d translator
