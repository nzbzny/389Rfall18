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
&nbsp;&nbsp;&nbsp;&nbsp;Salt: k  
&nbsp;&nbsp;&nbsp;&nbsp;Password: neptune  
&nbsp;&nbsp;&nbsp;&nbsp;Hash: 9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458e  
Hash 2:  
&nbsp;&nbsp;&nbsp;&nbsp;Salt: p  
&nbsp;&nbsp;&nbsp;&nbsp;Password: pizza  
&nbsp;&nbsp;&nbsp;&nbsp;Hash: 70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f  
Hash 3:  
&nbsp;&nbsp;&nbsp;&nbsp;Salt: u  
&nbsp;&nbsp;&nbsp;&nbsp;Password: loveyou  
&nbsp;&nbsp;&nbsp;&nbsp;Hash: d39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267  
Hash 4:  
&nbsp;&nbsp;&nbsp;&nbsp;Salt: m  
&nbsp;&nbsp;&nbsp;&nbsp;Password: jordan  
&nbsp;&nbsp;&nbsp;&nbsp;Hash: c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8  

### Part 2 (40 Pts)
Looking at the formatting of the message after trying it manually a few times, I saw that it was always "Find me the \[hash type\] hash of [value]", so I was able to find the hash type and value through regex. After that I figured out which type of hash it was and performed that hash (just through a bunch of ifs and elifs), and sent it to the server. Then I repeated that process until the flag was found and the \"while True\" loop broke because the flag didn't match the regex.
The flag is: CMSC389R-{H4sh-5l!ngInG-h@sH3r}
