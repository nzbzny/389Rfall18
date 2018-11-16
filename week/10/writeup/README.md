Writeup 10 - Crypto II
=====

Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 10 Writeup

### Part 1 (70 Pts)
The first thing I tried was netcatting the server to see what it did. I saw that it gave the hash of a secret plus the message you input, so I then looked at stub.py to see how to start decoding it. I saw that a lot of the work was already done in the stub.py file, and that I just had to figure out the padding and how to send it to the server. I used code similar to the code from last week to set up the sockets automate that process, and looped from 6 to 15 because the length of the secret was unknown. Once I was able to make the hash the same, the server gave me the flag below.  
CMSC389R-\{i\_still\_put\_the\_M\_between\_the\_DV\}


### Part 2 (30 Pts)
To generate your own public key, you can use the command *gpg --gen-key*  
To import a public key, use the command *gpg --import \[publickey file\]*  
For encrypting a message and dumping it into a file, use the command *gpg -e -u "Your Name" -r "Other Person's Name" [file]*  

