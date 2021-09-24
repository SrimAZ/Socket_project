# In this project, you will develop a simple web client using Python. 
# Through this project, you will learn the basics of socket programming 
# for TCP connections in Python: 
# how to create a socket, bind it to a specific address and port, 
# as well as send and receive an HTTP packet. 
# See the detailed requirement in the project instructions 
# (you can find it by clicking the content tab, and then Projects 
# >> Project 1: Simple HTTP Client in the left menu).

# You can complete this project in groups of 3-4 people. 
# Once you have chosen your group member, you can self-enroll in one of the groups on D2L. 
# Then you will be able to submit the required web_client.py on D2L

# import necessary modules
import sys
from urllib.parse import urlparse
from socket import *
import requests

# obtain the two parameters from commend line
param_url = sys.argv[1]
param_file = sys.argv[2]

# parse the url 
url_parsed = urlparse(param_url)
print("Host name is: ", url_parsed.hostname)
# you can obtain the following attributes from url_parsed
# e.g param_url = 'http://www.eller.arizona.edu:2016/index.html'
# url_parsed.hostname: Hostname = 'www.eller.arizona.edu'
# url_parsed.port: port number = 2016
# url_parsed.path: path of the file = '/index.html'

s = socket(AF_INET, SOCK_STREAM)

##### your code goes here ... #####
# 1. Construct the address and port number

# 2. Construct the http GET request (with Host and Connection headers)
req_str = "GET " + url_parsed.path + " HTTP/1.0\r\n\r\n"
print(req_str)

# 3. Connect to the server, and read the response
s.connect((url_parsed.hostname,80))

s.send(req_str.encode())
data = s.recv(1024)
print(data)

# s.send(req_str1.encode())
# data1 = s.recv(1024)
# print(data1)

# reading the image test.png
response = requests.get("http://www.u.arizona.edu/~weichen/MIS543/test.png")
if response.status_code == 200:
    with open("/Users/ual-laptop\OneDrive - University of Arizona\MIS 543 Wei Chen/sample.jpg", 'wb') as f:
        f.write(response.content)

# 4. Save the body of the HTTP response to param_file (skip the header)
header, body = data.split(b"\r\n\r\n")
header_str = header.decode()


# 5. If the HTTP response is anything rather than 200 OK, write the response header to param_file
f = open(param_file, 'w')
f.write(str(body))

# 6. Close the connection and the file
f.close()

print("\nFinishing downloading ...")

