#!/usr/bin/env python3

import docker

docker_con = docker.DockerClient('192.168.1.9:2376')

learn_container = docker_con.containers.get("learn")
learn_container.stats(stream=False)
learn_container.start()
print(learn_container.exec_run("ls -la"))




























































































































