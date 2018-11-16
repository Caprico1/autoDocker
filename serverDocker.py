import socket
import sys
from paramiko.py3compat import u

try:
    import terminos
    import tty

    has_terminos = True
except ImportError:
    has_terminos = False


"""
:param file
:returns string

runs the docker command to create a container and connect to it and mount a volume if it is provided.
"""


def server_host_docker(repo, ssh, dns=None, name="", volume=None, volume_target="/root", share_path=None, share_path_target="/root"):
    if dns is None:
        if volume is not None:
            if volume_target is not None:
                ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, volume, volume_target))
            else:
                ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, volume, volume_target))
        elif share_path is not None:
            if share_path_target is not None:
                ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
            else:
                ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
    else:
        if volume is not None:
            ssh.exec_command("docker volume create {0}".format(volume))
            if volume_target is not None:
                ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, volume, volume_target))
            else:
                ssh.exec_command("docker run -it --network host --name {0}  -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, volume, volume_target))
        elif share_path is not None:
            if share_path_target is not None:
                ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
            else:
                ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                          .format(name, repo, share_path, share_path_target))
        else:
            ssh.exec_command("docker run -it --network host --name {1} {2} /bin/bash".format(dns, name, repo))


def server_non_host_docker(repo, ssh, name="", volume=None, volume_target="/root", share_path=None, share_path_target="/root"):
    if volume is not None:
        if volume_target is not None:
            stdin, stdout, stderr = ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                      .format(name, repo, volume, volume_target))
            interactWithServer(stdout=stdout, stdin=stdin, stderr=stderr)
    elif share_path is not None:
        if share_path_target is not None:
            stdin, stdout, stderr = ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                      .format(name, repo, share_path, share_path_target))
            interactWithServer(stdout=stdout, stdin=stdin, stderr=stderr)

        else:
            stdin, stdout, stderr = ssh.exec_command("docker run -it --network host --name {0} -v {2}:{3} {1} /bin/bash"
                      .format(name, repo, share_path, share_path_target))
            interactWithServer(stdout=stdout, stdin=stdin, stderr=stderr)

    else:
        # stdin, stdout, stderr = ssh.exec_command("sudo docker create --name {0} {1}".format(name, repo))
        stdin, stdout, stderr = ssh.exec_command("sudo docker pull caprico/kali-top10")
        for line in stdout:
            print(line)


def interactWithServer(stdout, stdin, stderr):
    while not stdout.exit_status_ready():
        if stdout.channel.recv_ready():
            alldata = stdout.channel.recv(2048)
            while stdout.channel.recv_ready():
                alldata += stdout.channel.recv(2048)

            print(str(alldata, "utf8"))

    stdout.close()
    stdin.close()
    stderr.close()
