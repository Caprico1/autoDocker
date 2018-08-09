# autoDocker
Automatically setup docker containers on the host machines network


## Arguments
```
$ python auto_docker.py -h
usage: auto_docker.py [-h] [--host HOST] [--name NAME] [--dns DNS]
                      [--repo REPO] [--volume VOLUME]

Automatically create containers and setup networks with a CLI

optional arguments:
  -h, --help       show this help message and exit
  --host HOST      Put the docker container on the host network
  --name NAME      Name of the container
  --dns DNS        DNS address of the container
  --repo REPO      Docker Repository to build the container from
  --volume VOLUME  Volume to create/attach to the container
```

## Requirements:
* Python3
* =< Docker 18.06.0-ce


