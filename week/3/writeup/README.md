Writeup 3 - OSINT II, OpSec and RE
======

Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 3 Writeup

### Part 1 (100 pts)
The first suggestion I would provide Fred would be to close any port on his server that don't need to be open. For instance, if he's not running a website, he shouldn't have port 80 open, because that's just an open route for attackers to get in through. Similarly, if he doesn't need to be able to SSH into the server (if the only way he accesses it is through port 1337), then he should disable SSH and close port 22.\
Additionally, Fred should make his password significantly more secure. His password is 7 characters long and all lowercase letters, which any brute force or dictionary attack could crack extremely quickly. Additionally, none of his social media is private (which, in my opinion, it should always be as a general rule), so it would have also been easy to find the password just by looking at his instagram and seeing all of the pictures of pokemon. For similar reasons, if he really wanted to be secure he should avoid using the same username for professional and personal accounts, since that makes it easy to connect the two which makes a targeted attack on him significantly easier.\
Lastly, depending on how he uses the server (if it's only an internal server or only he needs to access it), he could create a whitelist of certain IP addresses to stop intruders. Or, if that's not an option because he doesn't know which IP addresses will need to access it, he could set up an Intrusion Detection System (IDS) to monitor his network for malicious activity / intrusion attempts. I would personally recommend avoiding solely signature-based IDS's, since they can only identify known attacks, and would go with a heuristic-based IDS with signature detection to provide the most up-to-date security.
