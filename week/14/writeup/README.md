Writeup 10 - Crypto II
=====

Name: *Noah Zbozny*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Noah Zbozny*

## Assignment 10 Writeup

### Part 1 (70 Pts)
I started off by just navigating around the website trying to find any input boxes to be able to do a SQL injection (since the hint was "sql"). When I couldn't find any inpt boxes, I looked further and noticed that the url for the item pages ended with "id=[val]", which made me think that it may have been vulnerable to a SQL injection. I then trying doing various things like entering into the search bar "http://cornerstoneairlines.co:8080/idem?id=0 and 1=1" to attempt a SQL injection. I was having occassional issues with my browser causing the server to disconnect, so I moved over to the terminal and began using wget to execute the injection attempts. I continued trying a bunch of similar things to what I mentioned above, sometimes getting the page for "id=0" (which I assume was the default response) and sometimes getting an Internal Server Error. Then I realized that my SQL injection was slightly off: I shouldn't have been using "and 1=1" I should have been using "or 1=1". So I continued trying it with "or 1=1" and was still getting errors. Then I remembered how the SQL statement would have been formatted, so I tried closing the single quotes around the id and opening them around the "1=1" to let it finish the statement, and it worked.  
The final command I used was *wget "http://cornerstoneairlines.co:8080/item?id=0' or '1 = 1"*  
The flag was CMSC38R-{y0U-are\_the\_5ql\_n1nja}  


### Part 2 (30 Pts)
Level 1: This level was easy, I just had to insert "<script>alert('test')</script> into the query box  
Level 2: This level required a little more thought. I couldn't just insert the script into the status box because it was guarded against that, so what I had to do was insert an image and use the onload event handler (which is an option with the img tag in html) to get it to display the alert when the image loaded (onload="alert('test');")  
Level 3: This level was fairly easy once I was in the mindset from the previous level. I looked at the html for the page and saw that it was creating html code by adding the value of the url (1, 2, or 3) to identify which image to show. So I modified this html code by setting the end of the url equal to *1.jpg' onload="alert('test');"/> <!--* to get it to display the alert upon the image being loaded   
Level 4: This one also wasn't bad once I realized I could escape the ' in the JavaScript code to end the function. I just had to end the function, run the alert, and start the function again, so my input to the timer box was *'); alert('test'); startTimer('3*  
Level 5: Again, I navigated the website to see what was going on. I saw that in the url for signup had a "next=confirm" at the end of it. Because the next parameter was set in the url, I figured I could do another injection with that. I looked at the html and saw that it had an href to get to the next page, so I just replaced the "next=confirm" with "next=javascript:alert('test');", reloaded the page, and got the alert.  
Level 6: The hardest part about this level was figuring out where to host the file. I tried writing a js file that only contained the words "alert('test');" and uploading it to my GitHub, but it wasn't able to load that gadget. Looking at the regex and their restriction to prevent http or https urls from being loaded it was easy to see that the regex wasn't case sensitive, so it would be fine accepting "Https". I figured it wasn't working with my GitHub because there was more than just the raw content (even when I selected the raw option), so I tried pastebin to see what would happen and that ended up working. I just changed the /static/gadget.js url to the pastebin url and changed the "https" in the pastebin url to "Https" and it worked.
