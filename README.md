# autoDocker
Automatically setup docker containers on the host machines network


## Requirements:
* Python3
* =< Docker 18.06.0-ce

## Arguments
```
usage: auto_docker.py [-h] [--host] [--name NAME] [--dns DNS] [--repo REPO]
                      [--volume VOLUME] [--volume_target VOLUME_TARGET]
                      [--share_path SHARE_PATH]
                      [--share_path_target SHARE_PATH_TARGET]
                      [--command COMMAND] [--ssh-host SSH_HOST]
                      [--ssh-port SSH_PORT] [--ssh-user SSH_USER]
                      [--ssh-pass SSH_PASS]

Automatically create containers and setup networks with a CLI

optional arguments:
  -h, --help            show this help message and exit
  --host                Put the docker container on the host network
  --name NAME           Name of the container
  --dns DNS             DNS address of the container
  --repo REPO           Docker Repository to build the container from.
  --volume VOLUME       Volume to create/attach to the container.
  --volume_target VOLUME_TARGET
                        Target for volume to mount to inside the container.
                        Will default to '/root' directory.
  --share_path SHARE_PATH
                        Path to share to the container from the host machine.
  --share_path_target SHARE_PATH_TARGET
                        Path to mount host path to the container.
  --command COMMAND     Command to be ran inside the container.

< WORK IN PROGRESS >
SSH:
  Connect to an external server with docker installed while using AutoDocker

  --ssh-host SSH_HOST   Connect to server to run commands. (Default Port
                        selected is 22)
  --ssh-port SSH_PORT   Connect to server with specified port
  --ssh-user SSH_USER   Connect to server with specified user
  --ssh-pass SSH_PASS   Connect to server with specified password

```



