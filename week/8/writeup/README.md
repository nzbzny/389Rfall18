Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Yes, the attackers used the traceroute command on a website. One of the websites they used it on was the cornerstone airlines website (142.93.118.186). On the way, the packet was routed through the UMD CSEC website (128.8.120.43)

2. laz0rh4x and c0uchpot4doz

3. laz0rh4x: 104.248.224.85 and c0uchpot4doz: 206.189.113.189 - laz0rh4x is in North Bergen, New Jersey and c0uchpot4doz is in London, England

4. They're communicating on port 2749 - it's the port that they share in common

5. Their plans are happening "tomorrow at 1500", but that packet was sent on October 24, 2018. So their plans would have happened on October 25, 2018 at 15:00 (3:00pm)

6. They sent a google drive link to each other. https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. "Tomorrow at 1500" (October 25 at 15:00, or 3:00pm)

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. update.fpff was generated on 10-24-2018 at 20:40:07

2. laz0rh4x

3. update.fpff says that it has 9 sections. However, it actually has 11 sections

4.

ascii:  
Call this number to get your flag: (422) 537 - 7946  
words:  
\[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9\]  
coord:  
(38.991610, -77.027540)  
reference:  
0x01 0x00 0x00 0x00  
ascii:  
The imfamous security pr0s at CMSC389R will never find this!  
ascii:  
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.\[3\] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal\{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.\[4\}  
coord:  
(38.991094, -76.932802)  
png:  
an image of a plane above the clouds with a flag captioned beneath it (in the question below)  
ascii:  
AF(saSAdf1AD)Snz\*\*asd1  
ascii:  
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9  

dwords:  
\[4, 8, 15, 16, 23, 42\]  

5. CMSC389R-\{c0rn3rst0ne\_airlin3s\_to\_the\_m00n\} - found in the image file  
CMSC389R-\{PlaIN\_dIfF\_FLAG\} - found by diffing the steganography paragraph with the wikipedia article for it  
CMSC389R-\{h1dd3n-s3ct10n-1n-fil3\} - found by base64 decoding section 10, the last ascii section
