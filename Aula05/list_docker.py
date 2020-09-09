#!/usr/bin/env python3

import docker

docker_con = docker.DockerClient('192.168.1.9:2376')

for container in docker_con.containers.list(all=True):
    print(container) 