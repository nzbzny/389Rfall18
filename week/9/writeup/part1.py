#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
passwords = wordlist.read().splitlines()
wordlist.close()

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

hashes_file = open('../hashes', 'r')
hashes = hashes_file.read().splitlines()
hashes_file.close()

to_pass = False
for h in hashes:
    to_pass = False
    for p in passwords:
        for s in salts:
            if to_pass == True:
                pass
            temp_pass = s + p
            pass_hash = hashlib.sha512(temp_pass).hexdigest()
            if h == pass_hash:
                print('h: %s' % h)
                print('p: %s' % p)
                print('s: %s' % s)
                to_pass = True
