import re
from pwn import *
import base64
from Crypto.Cipher import AES


def main():
    r = remote('0.cloud.chals.io', 16499)
    key = "" # as hex string
    b = 3   # bob secret key for deffie-helman exchange, just a random int

    while (True):
        line = str(r.recvline())
        print(line)
        if ("p, g" in line):
            p, g = extract_pg(line)

        elif ("A = " in line):
            A = extract_A(line)     # get alice computed key
            B = pow(g, b, p)        # generate bobs computed key to send to alice
            result = pow(A, b, p)   # calculate the shared key (alice can get the same result with with B,a,p)
            key += hex(result)[2:].zfill(2) # convert result to 2 digits hex string

        elif ("enter your number" in line):
            r.sendline(str(B))      # send to alice out computed key

        elif ("an IV:" in line):
            IV = extract_IV(line)

        elif ("flag:" in line):
            flag = extract_flag(line)
            break



    # take key, iv, and ciphertext and make AES256 decryption
    key = bytes.fromhex(key)
    iv = base64.b64decode(IV)
    enc = base64.b64decode(flag)
    

    # create the cipher config
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # decrypt the cipher text
    final_flag = cipher.decrypt(enc).rstrip().decode()
    print(final_flag)


# extract p,g from message 'p, g = (173, 110)\n'
def extract_pg(line):
    result = re.search(r"\((\d+), (\d+)\)", line)
    return [int(x) for x in result.groups()]  # convert to int

# extract A from message 'A = 154\n'
def extract_A(line):
    result = re.search(r"A = (\d+)", line)
    return int(result.group(1))


# extract IV from message 'Here is an IV: rSTZIbwu3RPKQGo2sGvVGQ==\n'
def extract_IV(line):
    result = re.search(r"IV: ([\w+/=]+)", line)
    return result.group(1)


# extract flag from message 'and an encrypted flag: KuMFGed65z1QYCAtKAGrqQ+exTU9jp0ej8nhbuq32c3YICA2pQ14GNCASiEVvlGx\n'
def extract_flag(line):
    result = re.search(r"flag: ([\w+/=]+)", line)
    return result.group(1)

main()