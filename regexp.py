import re
message = """ Content-Type: text/x-zim-wiki
Wiki-Format: zim 0.4
Creation-Date: 2017-09-17T18:55:38-05:00
Creation-Date: 2017-09-17T18:55:38-05:00
Creation-Date: 2017-09-17T18:55:38-05:00
Creation-Date: 2017-09-17T18:55:38-05:00

====== Home ======
Created Sunday 17 September 2017

What is needed? simple program which acts as a HTTP client . Program should implement GET method and should be eought to to download files as one would with the command line program curl It should include 1) Host: Header
 2) Transfer- encoding : chunked
 3) Connection: close header, or handle persistent connections
What is to be implemented? retrieve_url function which takes url(str) as its only argument

**HTTP notes**
 
	-Network protocol of the Web
	- Knowing HTTP enables you to write Web browser, Web server and other tools
	
	__Sockets:__
	- Endpoints of a bidirectional communication channel
	- may communicate within aprocess, between processes on the same machine or between processes on different continents
	syntax:  
	To create a socket - 
	s = socket.socket (socket_family, socket_type, protocol = 0)
	
	Client side-
	s.connect() This method actively initiates TCP server connection """

regex = re.compile(r'\*\*\w+\s\w+\*\*')
mo = regex.findall(message)
equalex = re.compile(r'=+ \w+ =+')
print('mo =' + str(mo))
top = equalex.findall(message)
print(top)
