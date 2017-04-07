# Web-Crawler
Web crawler will scrap the data from the URL you will provide. Once entered multiple threads called spider will visit the website to extract useful data from the source code. 

There are two major libraries used 1. Urllib 2. Beautiful Soup

The use of urllib is to bring back the source code of the URL. 
There are some website that uses firewall, disallowing the programe to get the source code. For breaking such firewalls, a simple wall breaker code has been implemented which works efficently for some low level firewalls.

Once the source code has been retured Beautiful Soup will scrap them and shuffel the "a" tag for hyperlinks and "img" tag for images or videos.
The hyperlinks will be stored in a .txt file. For the images to be downloaded, the Urllib library is again called that goes to the path of image and downloads it.
