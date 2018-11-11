Writeup 9 - Crypto I
=====

Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 9 Writeup

### Part 1 (60 Pts)
The first thing I did for this part was to look at the length of the wordlist to see how efficient the code would need to be. Since the wordlist was short, there were only 4 hashes to run through, and there were only 26 salts to run through, it was just a triple nested for loop to run through the hashes, salts, and passwords. Just concatenate the salt with the password, perform the sha512 hexdigest on it, and compare that to the hash to see if they were the same. 
Hash 1:  
  Salt: k  
  Password: neptune  
Hash 2:  
  Salt: p  
  Password: pizza  
Hash 3:  
  Salt: u  
  Password: loveyou  
Hash 4:  
  Salt: m  
  Password: jordan  

### Part 2 (40 Pts)
Looking at the formatting of the message after trying it manually a few times, I saw that it was always "Find me the \[hash type\] hash of [value]", so I was able to find the hash type and value through regex. After that I figured out which type of hash it was and performed that hash (just through a bunch of ifs and elifs), and sent it to the server. Then I repeated that process until the flag was found and the \"while True\" loop broke because the flag didn't match the regex.
The flag is: CMSC389R-{H4sh-5l!ngInG-h@sH3r}
