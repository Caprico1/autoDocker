import os
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
