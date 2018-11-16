#!/usr/bin/env python2
# from the git repo
import md5py
import re
import socket
import time

host = "142.93.118.186"
port = 1234

#####################################
### STEP 1: Calculate forged hash ###
#####################################
message = 'message'    # original message here


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(1024)
s.send('1\n')
data = s.recv(1024)
s.send(message + '\n')
data = s.recv(1024)

m = re.search('Your hash: ([a-z0-9]*)', data)
legit = m.group(1)

#legit = '7d2a3a8f9b9b6491736c785c68ce02c1'      # a legit hash of secret + message goes here, obtained from signing a message

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'malicious message'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
#print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

for i in range(6, 16):
    mesg_len = (len(message) + i) * 8
    padding = '\x80' + '\x00' * (((448 - mesg_len) - 1) / 8) + chr(mesg_len) + '\x00' * 7
    payload = message + padding + malicious
    s.send('2\n')
    data = s.recv(1024)
    s.send(fake_hash + '\n')
    time.sleep(1)
    data = s.recv(1024)
    s.send(payload + '\n')
    time.sleep(1)
    data = s.recv(1024)
    print('i: %d' % i)
    print(data)
    print('\n\n\n\n\n')
    """
    m = re.search('[a-f0-9]{32}', data)
    print(data)
    if (m.group(1) == m.group(2)):
        print(data)
        data = s.recv(1024)
        print(data)
        s.close()
        break
    """

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash

print(repr(payload))

print(len(payload) - len(malicious))

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
