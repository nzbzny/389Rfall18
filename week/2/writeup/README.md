Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. Reddit: /u/kruegster1990 (Google search)\\
Twitter: kruegster1990 (Google search)\\
Instagram: kruegster1990 (inteltechniques.com)
Lives in Silver Spring, MD (on his Twitter account)\\
Went on a trip on Malaysian Airlines (on his Twitter account)\\
kruegster@tutanota.com (on his website)


3. 142.93.118.186

4. I didn't find any hidden files or directories other than the site's robots.txt, but inspecting the source code of the main site I found: CMSC389R-{h1dden\_fl4g\_in\_s0urce}
flag: CMSC389R-{fly-th3\_sk1es\_w1th\_u5} - found the site's robots.txt which disallowed /secret, so I went to cornerstoneairlines.co/secret, saw that it was blank, inspected the source code, and found the flag

5. 142.93.117.193 - found on his website, took me to a page that was "under construction"\\
216.87.155.33 - found through dnsdumpster\\
216.87.152.33 - found through dnsdumpster

6. 142.93.118.186 is a DigitalOcean server being run in New York - found through a whois lookup.\\
142.93.117.193 is also a DigitalOcean server being run in New York - also found through a whois lookup\\
216.87.155.33 is located in the U.S. - found via dnsdumpster\\
216.87.152.33 is located in the U.S. - found via dnsdumpster

7. 142.93.118.186 is running IOS 10.3 - found through nmap os scan\\
142.93.117.193 is also running IOS 10.3 - found through nmap os scan\\
216.87.155.33 is running Oracle Virtualbox - found through nmap os scan\\
216.87.152.33 is also running IOS 10.3 - found through nmap os scan

8. *(BONUS)*\\
flag: CMSC389R-{dns-txt-rec0rd-ftw} - found through dnsdumpster
flag: CMSC389R-{y0u\_found\_th3\_g1t\_repo} - found the website's .git directory through url fuzzing


### Part 2 (55 pts)
Since only the 142.\*.\*.\* addresses are currently hosting the server, I ran nmap on those addresses. After running a portscan on the ports between 1-3000, I saw that 80, 1337, and 2222 were open. I tried netcatting into all 3 and port 1337 gave me the ability to log in. I then tried running the stub.py program (and creating stub2.py and stub3.py) to crack the password with 3 different usernames: "kruegster", "krueger", and "fkrueger", and it returned that the username was "kruegster" and the password was "pokemon". From there I was able to log into the server and poke around. I went into the /home directory and then saw that there was a "flight\_records" directory, so I went into there and found a few hundred flight records. The flight record I selected was AAC27670 and the flag is *CMSC389R-{c0rn3rstone-air-27670}* because that's the flight number that was on the ticket that Krueger posted to his Instagram account.
