# scream
Category: Pwn

# Description
Bisa ga sih ga usah teriak teriak, ribut tau !!!!! <br>
sebagai mahasiswa aku cuma pingin tidurku tidak diganggu 😞 <br>
`nc <ip> <port>`

# Solution
Given a file named `chall` and `scream.c` and opened it. The `scream.c` file almost has no code and only comments. But there is this function below
```
void vuln(){
  char buffer[0x100];
  gets(buffer);
}
```
<br>

This shows that there is a Buffer Overflow Vulnerability that can be exploited using this [code](solve/solve.py) <br>
Then found the flag<br>
Flag: `HCS{Buff3r_0v3rfl0wwwwww}`
