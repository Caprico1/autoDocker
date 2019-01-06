from socket import socket, error
import paramiko

'''
:param hostname
:param port
:param username
:param password


'''
def open_client(hostname, port, username, password):
    sock = socket()
    # hostname = input("Host: ")
    # port = int(input("Port: "))
    # username = input("User: ")
    # password = input("Passphrase: ")

    try:
        sock.connect((hostname, port))


        client = paramiko.transport.Transport(sock)

        client.start_client()

        client.auth_password(username=username, password=password)
        cmd_channel = client.open_session()
        # print(cmd_channel)
        # exit()

        channel = cmd_channel.invoke_shell()

        return channel

    except Exception:
        print('[-] connection failed')
        exit(1)


