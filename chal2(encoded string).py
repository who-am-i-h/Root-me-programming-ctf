import socket 
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "challenge01.root-me.org"
port = 52023
s.connect((host, port))

while True:
    contents = s.recv(1024).decode()
    print(contents)
    contents = (contents.split())
    for i in contents:
        
        if i.endswith("."):
            l = ""
            for j in range(1, len(i) - 2):
                l+= i[j]          
            l = base64.b64decode((l)).decode()
            print(l)
            l += "\n"
            print("fg")
            l = l.encode()
            s.send(l)
            # print(s.recv(1024).decode())
            break
    break

    
    
    

import socket 
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "challenge01.root-me.org"
port = 52023
s.connect((host, port))

# while true:
contents = s.recv(1024).decode()
print(contents)
contents = (contents.split())
for i in contents:
    
    if i.endswith("."):
        l = ""
        for j in range(1, len(i) - 2):
            l+= i[j]          
        l = base64.b64decode((l)).decode()
        print(l)
        l = str(l + "\n").encode() # Added newline
        s.send(l)
        # print(s.recv(1024).decode())
        break

contents = s.recv(1024).decode()
print(contents)