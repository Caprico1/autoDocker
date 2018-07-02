import os
import sys



def main():

    print("-------------------------------------")
    print("USAGE: auto_docker.py <repository> --host --dns=<DNS SERVER IP> --name=<NAME OF CONTAINER>\n")

    print("--host                :   Setup docker container to use host network. If not set "
          "the container will be set to the docker network")

    print("--dns=<DNS SERVER IP> :   Set the docker container's dns address\n")

    print("-------------------------------------")

    # set global variables
    host = False
    dns = None
    name = ""
    repo = ""

    # set values from command line arguments
    if len(sys.argv) != 1:
        repo = sys.argv[1]

        # check for any options
        if sys.argv[2]:
            if "--host" in sys.argv[2]:
                host = True
        if sys.argv[3]:
            dns = sys.argv[3].split('=')[1]
        if sys.argv[4]:
            name = sys.argv[4].split('=')[1]
    else:
        print("No repository or options specified")
        exit()

    if host:
        host_docker(repo, dns, name)

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

runs the docker command to create a 
"""


def host_docker(repo, dns="1.1.1.1", name=""):

        os.system("docker run -it --network=host --dns={0} --name {1} {2} /bin/bash".format(dns, name, repo))

def non_host_docker(repo, name=""):

        os.system("docker run -it --name {0} {1} /bin/bash".format(name, repo))

main()

