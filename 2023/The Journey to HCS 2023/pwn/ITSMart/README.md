# ITSMart
Category: Pwn

# Description
katanya ITS baru buka minimarket baru ya? <br>
coba deh belanja, tau tau dapat hadiah nanti xixixixi <br>
`nc <ip> <port>`
# Solution
When running `nc <ip> <port>` and trying the program, there is something interesting. <br><br>
![POC 1](images/POC%201.png) <br> 

The "uang" or money value is negative, so we can exploit it using this [code](./solve/solve.py) <br>
Then found the flag<br>
Flag: `HCS{m1nus_dikit_g4_ngaruh}`
