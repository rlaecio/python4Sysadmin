#!/usr/bin/env python3

import docker

docker_con = docker.DockerClient('192.168.1.9:2376')

container = docker_con.containers.run(
    'debian', '/bin/bash',
    name="learn", detach=True, tty=True
)

print(container)