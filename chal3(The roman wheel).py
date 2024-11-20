import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "challenge01.root-me.org"
port = 52021
s.connect((host, port))

while True:
    contents = s.recv(1024).decode()
    x = contents.split()
    mess = ""
    for i in x:
        if i.endswith("."):
            i = (i[1:len(i) - 2])
            print(i)
            for j in i:
                if ord(j) >= 65 and ord(j) <= 90:
                    if (ord(j)+13 <= 90):
                        j = chr(ord(j) + 13)
                    else:
                     # print(((ord(j)+13) % 90) + 65)
                        j = chr(((ord(j)+13) % 90) + 64)
                elif ord(j) >= 97 and ord(j) <= 122:
                    if (ord(j)+13 <= 122):
                        j = chr(ord(j) + 13)
                    else:
                        j = chr(((ord(j)+13) % 122) + 96)
                mess += j
            s.send((mess+"\n").encode())
            print(s.recv(1024).decode())

