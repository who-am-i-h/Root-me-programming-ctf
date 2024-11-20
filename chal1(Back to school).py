import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "challenge01.root-me.org"
port = 52002
s.connect((host, port))

while True:
    contents = s.recv(1024).decode()
    print(contents)
    nums = []
    contents = contents.split()
    for i in contents:
        try:
            i = int(i)
            nums.append(i)
        except:
            continue
    print(nums)
    sq = str(round(nums[1]**0.5 * nums[2], 2)) + "\n" 
    print(sq)
    sq = sq.encode()
    s.send((sq))
    print(s.recv(1024).decode())
    break

