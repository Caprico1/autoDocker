import os
import sys
from argparse import ArgumentParser



def main():
    # set global variables
    host = False
    dns = None
    name = ""
    repo = ""
    volume = None

    parser = ArgumentParser(description="Automatically create containers and setup networks with a CLI")

    parser.add_argument('--host', action='store_true', help="Put the docker container on the host network")
    parser.add_argument('--name', help="Name of the container")
    parser.add_argument('--dns', help="DNS address of the container")
    parser.add_argument('--repo', help="Docker Repository to build the container from")
    parser.add_argument('--volume', help="Volume to create/attach to the container")
    parser.add_argument('--volume_target', help="Target for volume to mount to inside the container." +
                                                " Will default to '~/' directory")

    args = parser.parse_args()

    host = args.host
    dns = args.dns
    name = args.name
    repo = args.repo
    volume = args.repo
    vol_target = args.volume_target

    if host:
        if volume:
            if vol_target:
                host_docker(repo, dns, name, volume, vol_target)
            else:
                host_docker(repo, dns, name, volume)
    else:
        non_host_docker(repo, name)


"""
:param string
:returns bool

Helper function to see if the path given by the user is a valid file path.
"""


def is_file(file):
    return os.path.isfile(file)


"""
:param file
:returns string

runs the docker command to create a container and connect to it and mount a volume if it is provided.
"""


def host_docker(repo, dns=None, name="", volume=None, volume_target="/root"):
        if dns is None:
            if volume is not None:
                # os.system("docker volume create {0}".format(volume))
                if volume_target is not None:
                    os.system("docker run -it --network host --name {0} -v {2}:{3} {1}   /bin/bash"
                              .format(name, repo, volume, volume_target))
                else:
                    os.system("docker run -it --network host --name {0} -v {2}:{3} {1}  /bin/bash"
                              .format(name, repo, volume, volume_target))
        else:
            if volume is not None:
                os.system("docker volume create {0}".format(volume))
                if volume_target is not None:
                    os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                              .format(name, repo, volume, volume_target))
                else:
                    os.system("docker run -it --network host --name {0}  -v {2}:{3} {1}  /bin/bash"
                              .format(name, repo, volume, volume_target))
            else:
                os.system("docker run -it --network host --dns={0} --name {1} {2} /bin/bash".format(dns, name, repo))


def non_host_docker(repo, name="", volume="", volume_target="/root"):
        if volume is not None:
            if volume_target is not None:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1}   /bin/bash"
                          .format(name, repo, volume, volume_target))
            else:
                os.system("docker run -it --network host --name {0} {1} /bin/bash"
                          .format(name, repo))

main()

