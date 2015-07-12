#!/usr/bin/env python
import sys
import socket
 
if(len(sys.argv) < 3):
        print("usage: smtpenumerate.py userlist IP")
        sys.exit()
 
wordFile = open(sys.argv[1], "r")
foundUsers = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[2], 25))
s.send("HELO\n")
s.recv(1024)
s.send("MAIL from:<>\n")
s.recv(1024)
 
for line in wordFile:
        s.send("RCPT to:" + line)
        response = s.recv(1024)
        if "Recipient ok" in response:
                foundUsers.append(line)
 
print("Users found: " + str(len(foundUsers)))
for user in foundUsers:
        print(user.rstrip())
