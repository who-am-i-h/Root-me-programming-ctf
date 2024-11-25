from pwn import *
import zlib
import base64
host = "challenge01.root-me.org"
port = 52022
io = remote(host=host, port=port)
try:
    contents = io.recvuntil(b'?').decode()
except:
    print(io.recv(1024).decode())

def solve(contents):
    # contents = io.recvuntil(b'?').decode()
    contents = contents.split("my string is")[1].split(".")[0]
    print(contents)
    contents = base64.b64decode(contents)
    contents = zlib.decompress(contents)
    contents = contents.decode('utf-8')
    print(contents)
    io.sendline(contents.encode())
    try:
        nom = io.recvuntil(b'?').decode()
    except:
        print(io.recv(1024).decode())
        return 1


    if (nom.startswith(" my string")):
        print(nom)
        solve(nom)
    else:
        print(nom)

solve(contents=contents)

# contents = " my string is 'eJzzz/LzqLAodo4sNTIIDQnIz8swLXc3dXYHAGRKB9Y='. What is your answer ?"
# contents = contents.split("my string is")[1].split(".")[0]
# print(contents)

