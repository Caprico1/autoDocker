import os
import sys
from argparse import ArgumentParser
from paramiko import SSHClient, AutoAddPolicy



def main():
    # initialize global variables
    host = False
    dns = None
    name = ""
    repo = ""
    volume = None
    vol_target = ""
    share_path = None
    share_path_target = ""

    parser = ArgumentParser(description="Automatically create containers and setup networks with a CLI")

    parser.add_argument('--host', action='store_true', help="Put the docker container on the host network")
    parser.add_argument('--name', help="Name of the container")
    parser.add_argument('--dns', help="DNS address of the container")
    parser.add_argument('--repo', help="Docker Repository to build the container from.")
    parser.add_argument('--volume', help="Volume to create/attach to the container.")
    parser.add_argument('--volume_target', help="Target for volume to mount to inside the container." +
                                                " Will default to '/root' directory.")
    parser.add_argument('--share_path', help="Path to share to the container from the host machine.")
    parser.add_argument('--share_path_target', help="Path to mount host path to the container.")
    parser.add_argument('--command', help="Command to be ran inside the container.")

    # get arguments
    args = parser.parse_args()

    # Assign Arguments to Variables
    host = args.host
    dns = args.dns
    name = args.name
    repo = args.repo
    volume = args.repo
    vol_target = args.volume_target

    share_path = args.share_path
    share_path_target = args.share_path_target

    if repo:
        if host:
            if volume:
                if vol_target:
                    host_docker(repo, dns, name, volume, vol_target)
                else:
                    host_docker(repo, dns, name, volume)
            elif share_path:
                if share_path_target:
                    host_docker(repo, dns, name, share_path=share_path, share_path_target=share_path_target)
                else:
                    host_docker(repo, dns, name, share_path=share_path)
        else:
            non_host_docker(repo, name)
    else:
        print('A repository must be given to create a container')


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


def host_docker(repo, dns=None, name="", volume=None, volume_target="/root", share_path=None, share_path_target="/root"):
    if dns is None:
        if volume is not None:
            if volume_target is not None:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, volume, volume_target))
            else:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, volume, volume_target))
        elif share_path is not None:
            if share_path_target is not None:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
            else:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
    else:
        if volume is not None:
            os.system("docker volume create {0}".format(volume))
            if volume_target is not None:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, volume, volume_target))
            else:
                os.system("docker run -it --network host --name {0}  -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, volume, volume_target))
        elif share_path is not None:
            if share_path_target is not None:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
            else:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
        else:
            os.system("docker run -it --network host --dns={0} --name {1} {2} /bin/bash".format(dns, name, repo))


def non_host_docker(repo, name="", volume="", volume_target="/root", share_path=None, share_path_target="/root"):
    if volume is not None:
        if volume_target is not None:
            os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                      .format(name, repo, volume, volume_target))
        elif share_path is not None:
            if share_path_target is not None:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
            else:
                os.system("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
        else:
            os.system("docker run -it --network host --name {0} {1} /bin/bash"
                      .format(name, repo))


main()
