Writeup 5 - Binaries I
======

Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 5 Writeup

For both functions, I knew I would have to implement basic loop functionality, so I looked at the loop instruction to figure out how it works. I saw that it decremented the rcx register, so I moved the n value (which for both functions was passed in through rdx) into rcx. Then I had to figure out how to replace the character in the string with the character it needed to be replaced with. This part took me a little while to figure out the syntax, because I knew I needed to dereference the string with \[\], but I was copying over the entire rsi register instead of just the low bits, so I copied it over to rax and then moved al into rdi. Beyond that, there were no implementation issues or issues I found in debugging. Once I completed the memset function, strncpy was similar to implement so that was significantly easier.
