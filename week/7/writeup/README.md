Writeup 7 - Forensics I
======

Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG Images File

2. 875 N Michigan Ave., Chicago, IL 60611 - The John Hancock Center 

3. 08-22-2018 11:33:24.801

4. iPhone 8 back camera

5. 539.5m

6. CMSC389R-\{look\_I\_f0und\_a\_str1ng}

### Part 2 (55 pts)
I began by attempting to objdump the file to see if there was anything I could quickly identify. When I saw that there wasn't anything that I could quickly see, like a flag string or anything like that, I decided to come back to the objdump and analyze that line by line if I had to, but to try other routes that might be quicker or more efficient. I also tried giving the program various inputs to see if I got a different output, but that didn't work either. I tried using gdb on the program (in case they had accidentally left the debug flag on), but that also didn't work. Then I decided to open the executable in r2, in order to get some syntax highlighting and potentially some extra information that objdump didn't give me. When I did this, the first thing I saw was that r2 was able to tell me the characters that were being moved over into the local variables (most likely a string), and I saw that they were moving in the characters "/tmp/.stego". Now the program's output, "Where is your flag?" started to make sense. I then also saw that the program was writing to the /tmp/.stego file, so I tried reading it to see if I could find anything there, but it was written in binary or otherwise obfuscated somehow, so I couldn't find anything immediately. Then I tried figuring out what type of file it was, but the command "file /tmp/.stego" just outputted "data", so I hexdumped it to look at the file signature and found that it was a JFIF file. However, because file wasn't outputting that it was a JFIF file, I figured out that the file header was corrupted, and began figuring out how to fix it. I used vim as my hex editor, and fixed the file header and the file footer to get it to have the right file signature. Then I used steghide to try to find the flag, but it was password protected, so I opened the fixed image file and saw that it was a stegosaurus, so I used the password "stegosaurus" and found the flag below.
CMSC389R-{dropping\_files\_is\_fun}
