import os
import json
from argparse import ArgumentParser
from paramiko import SSHClient, AutoAddPolicy
from localDocker import host_docker, non_host_docker
from serverDocker import server_host_docker, server_non_host_docker
from client import open_client
from configs import config_file, config_manager
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
    ssh_host = None
    ssh_port = None
    ssh_user = None
    ssh_pass = None
    client = None

    print("""
    
'||''|.                '||     '||''|.          .        ,     ,    ___
 ||   ||   ...    ....  ||  ..  ||   ||   ... .||.      (\____/)   (o*o)  
 ||    ||.|  '|..|   '' || .'   ||'''|. .|  '|.||        (_oo_)     | | 
||    ||||   ||||      ||'|.   ||    ||||   ||||          (O)      ( > )
.||...|'  '|..|' '|...'.||. ||..||...|'  '|..|''|.'      __||__    /   \\

"Good. Good. Back to the rusting septic system of this FUTURISTIC SPACE SHIP!!!"

     
    """)


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

    ssh_group = parser.add_argument_group('SSH', description=" IN_DEVLOPMENT AND NOT READY FOR USE!!!\nConnect to an external server with "
                                                             "docker installed while using AutoDocker")
    ssh_group.add_argument('--ssh-host', help="Connect to server to run commands. (Default Port selected is 22)")
    ssh_group.add_argument('--ssh-port', help="Connect to server with specified port")
    ssh_group.add_argument('--ssh-user', help="Connect to server with specified user")
    ssh_group.add_argument('--ssh-pass', help="Connect to server with specified password")
    ssh_group.add_argument('--shadow', help="Lurking Container...")

    config_group = parser.add_argument_group("Configurations", description="Save and Load configured docker containers")
    config_group.add_argument('--config', action='store_true', help="Save configured docker files in a text file.")
    config_group.add_argument('--config-manager', action='store_true', help="List and select a configuration of saved configurations")
    # get arguments
    args = parser.parse_args()

    if args.config == True:
        config_file(args)

    # Assign Arguments to Variables Considering if the config manager was used.
    if args.config_manager == True:
        args = config_manager()
        host = args['host']
        dns = args['dns']
        name = args['name']
        repo = args['repo']
        volume = args['volume']
        vol_target = args['volume_target']

        share_path = args['share_path']
        share_path_target = args['share_path_target']

        ssh_host = args['ssh_host']
        ssh_port = args['ssh_port']
        ssh_user = args['ssh_user']
        if args['ssh_pass']is not None:
            ssh_pass = args['ssh_pass'].replace('\'', '')
        shadow = args['shadow']
    else:
        host = args.host
        dns = args.dns
        name = args.name
        repo = args.repo
        volume = args.volume
        vol_target = args.volume_target

        share_path = args.share_path
        share_path_target = args.share_path_target

        ssh_host = args.ssh_host
        ssh_port = args.ssh_port
        ssh_user = args.ssh_user
        if args.ssh_pass is not None:
            ssh_pass = args.ssh_pass.replace('\'', '')
        shadow = args.shadow



    # Check to see if all SSH arguments are present in memory before creating a client. Kill if partial arguments.
    # Proceed on local machine if none are present
    if ssh_host is not None and ssh_user is not None and ssh_pass is not None:
        if ssh_port is None:
            ssh_port = 22
        print("Auto Docker Running on Remote Server")

        channel = open_client(ssh_host, ssh_port, ssh_user, ssh_pass)
    # elif ssh_host is None or ssh_port is None or ssh_user is None or ssh_pass is None:
    #     print("All SSH arguments are required to use SSH.")
    #     print("Auto docker will exit now...")
    #     exit()
    else:
        print("Auto Docker Running on Local Machine")

    if client is not None:
        if repo:
            if host:
                if volume:
                    if vol_target:
                        server_host_docker(repo=repo, ssh=client, dns=dns, name=name, volume=volume,
                                           volume_target=vol_target)
                    else:
                        server_host_docker(repo=repo, ssh=client, dns=dns, name=name, volume=volume)
                elif share_path:
                    if share_path_target:
                        server_host_docker(repo=repo, ssh=client, dns=dns, name=name, share_path=share_path,
                                           share_path_target=share_path_target)
                    else:
                        server_host_docker(repo=repo, ssh=client, dns=dns, name=name, share_path=share_path)
            else:
                server_non_host_docker(repo, ssh=client, name=name)
        else:
            print('A repository must be given to create a container')
    else:
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



main()
