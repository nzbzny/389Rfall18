#!/usr/bin/env python2

import sys
import struct
import datetime

SIZEOF_WORD = 4
SIZEOF_DWORD = 8
SIZEOF_DOUBLE = 8

SECTION_PNG = 0x1
SECTION_DWORDS = 0x2
SECTION_UTF8 = 0x3
SECTION_DOUBLES = 0x4
SECTION_WORDS = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_ASCII = 0x9

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

timestamp = struct.unpack("<L", data[8:12])[0]
print('timestamp: %s' % timestamp)
print(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

author = data[12:20]
print('author: %s' % author)

section_num = struct.unpack('<L', data[20:24])[0]
print('section num: %d' % section_num)

body_len = len(data) - 24

curr_loc = 24

def deal_with_body(st, sl): #stype, slen
    global curr_loc
    if st == SECTION_PNG:
        print('png:')
        png = data[curr_loc:curr_loc + sl]
        curr_loc += sl
#        header = str([0x89,0x50,0x4e,0x47,0x0d,0x0a,0x1a,0x0a])
        header = ['\211', 'P', 'N', 'G', '\r', '\n', '\032', '\n']
        f = open ('png.png', 'w+')
        for x in header:
            f.write(x)
        f.write(png)
        f.close()
    elif st == SECTION_DWORDS:
        if sl % 8 != 0:
            bork('dwords slen is incorrect: should but a multiple of 8 but received %d' % sl)
        print('dwords:')
        lst = []
        i = 0
        while (i < sl / 8):
            s = struct.unpack('<Q', data[curr_loc:curr_loc + SIZEOF_DWORD])[0]
            curr_loc += SIZEOF_DWORD
            lst.append(s)
            i += 1
        print(lst)
    elif st == SECTION_UTF8:
        print('utf8:')
        sv = data[curr_loc:curr_loc + sl]
        curr_loc += sl
        sv_decoded = sv.decode('utf-8')
        print(sv_decoded)
    elif st == SECTION_DOUBLES:
        if sl % 8 != 0:
            bork('doubles slen is incorrect: should but a multiple of 8 but received %d' % sl)
        print('doubles:')
        lst = []
        i = 0
        while (i < sl / 8):
            s = struct.unpack('<d', data[curr_loc:curr_loc + SIZEOF_DOUBLE])
            curr_loc += SIZEOF_DOUBLE
            lst.append(s)
            i += 1
        print(lst)
    elif st == SECTION_WORDS:
        if sl % 4 != 0:
            bork('words slen is incorrect: should but a multiple of 4 but received %d' % sl)
        print('words:')
        lst = []
        i = 0
        while (i < sl / 4):
            s = struct.unpack('<L', data[curr_loc:curr_loc + SIZEOF_WORD])[0]
            curr_loc += SIZEOF_WORD
            lst.append(s)
            i += 1
        print(lst)
    elif st == SECTION_COORD:
        if sl != 16 and sl != 0:
            bork('coord slen is incorrect: expected 16 but received %d' % sl)
        print('coord:')
        if sl == 0:
            return
        lat, lng = struct.unpack('<dd', data[curr_loc:curr_loc + sl])
        curr_loc += sl
        print('(%f, %f)' % (lat, lng))
    elif st == SECTION_REFERENCE:
        if sl != 4 and sl != 0:
            bork('reference slen is incorrect: expected 4 but received %d' % sl)
        print('reference:')
        if sl == 0:
            return
        sv = data[curr_loc:curr_loc + sl]
        curr_loc += sl
        #":".join("{:02x}".format(ord(c)) for c in sv)
        for c in sv:
            print c.encode('hex')
    elif st == SECTION_ASCII:
        print('ascii:')
        sv = data[curr_loc:curr_loc + sl]
        curr_loc += sl
        print(sv)


while (curr_loc < len(data)):
    stype = struct.unpack('<L', data[curr_loc:curr_loc + SIZEOF_WORD])[0]
    curr_loc += SIZEOF_WORD
    slen = struct.unpack('<L', data[curr_loc:curr_loc + SIZEOF_WORD])[0] 
    curr_loc += SIZEOF_WORD
    deal_with_body(stype, slen)

#print('stype: %d\nslen: %d' % (stype, slen))


