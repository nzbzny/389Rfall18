#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re
import time

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    # receive some data
    data = s.recv(1024)
    print(data)

    m = re.search('Find me the ([A-Za-z0-9]*) hash of ([A-Za-z0-9]*)', data)

    #md5, sha1, sha224, sha256, sha384, sha512

    h = m.group(1)
    x = m.group(2)

    if h == 'md5':
        val = hashlib.md5(x).hexdigest()
    elif h == 'sha1':
        val = hashlib.sha1(x).hexdigest()
    elif h == 'sha224':
        val = hashlib.sha224(x).hexdigest()
    elif h == 'sha256':
        val = hashlib.sha256(x).hexdigest()
    elif h == 'sha384':
        val = hashlib.sha384(x).hexdigest()
    elif h == 'sha512':
        val = hashlib.sha512(x).hexdigest()
    else:
        print('failed: h = %s' % h)
        break

    s.send(val + '\n')

    #time.sleep(1)
    #data = s.recv(1024)
    #time.sleep(1)
    #print(data)

# close the connection
s.close()
