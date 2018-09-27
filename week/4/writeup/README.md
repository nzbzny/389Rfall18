
Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 4 Writeup

### Part 1 (45 pts)
The flag that I found was CMSC389R-{p1ng\_as\_a\_$erv1c3}. The first thing I did was to netct into port 45 on the server, then just input an IP address into the terminal when it requested one, to see what the command did. I saw that it seemed to just run the ping command with whatever input you gave it and then printed the output, so I ran it again and tried it with "1.1.1.1; ls", since the ";" character is used to end a command in one line and start another command on the same line, and saw that at the end of the ping output it printed the contents of the root directory. So I tried it with "; ls /home" to see if I could just eliminate the ping output, and it worked and printed "flag.txt". Then I ran the program one last time with "; cat /home/flag.txt" to print the flag. I also found the script that Krueger uses to run the program through a similar method to above, just terminating the ping command with a ";" and printing the contents of various directories until I found a bash script in /opt/container_startup.sh. In it, Krueger just creates a cmd variable with "ping -w 5 -c 2 $input" and evaluates that command, which is what makes the script vulnerable to a command injection. If Krueger wants to secure his service, he needs to do some basic checking on the input first to make sure it's just in the form of an IP address (which could be done through a regex like "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$") and not to evaluate anything that's not in the form of an IP address. Since his program only accepts IP addresses, not accepting any input that's not in the form of an IP address would be the most secure solution to avoid command injections like the one that was used in this attack.




### Part 2 (55 pts)
The code in stub.py in the writeup directory creates a shell that can remotely execute commands on the cornerstoneairlines.co server through the command injection technique described in part 1. The shell takes in user input, and when the "shell" command is entered, it begins taking in user commands to run on the server. It does so by taking the user's command and appending it to the string "; cd $PATH; " (where $PATH is the directory that the user is currently working in that the shell keeps track of while the user is inputting commands) so that the user's commands will always be executed in the correct directory. Then it just connects to the server, executes the command, and waits for a response. The shell is also able to pull a file from the server down to the local machine, and it does this similarly to how it executes commands in the interactive shell mode. The format for the pull command is "pull \<remote\_path> \<local\_path>", so it forms the command "; cat \<remote\_path>", saves out output, and then writes it to the file specified in \<local\_path> and saves the file. So it doesn't actually "pull" the file from the server in terms of downloading it, but the effect is the same. The shell also has a help menu, which just lists the 4 main commands - shell, help, pull, and quit.
