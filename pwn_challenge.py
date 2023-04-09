#!/usr/bin/python3
import codecs
import base64
from pwn import *
from Crypto.PublicKey import RSA    
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import inverse
import binascii
print("hello")

io = process(['curl', '13.234.19.132', '8000'])


context.log_level = 'DEBUG'

io.recvline().decode('utf-8')

w = io.recvline().decode('utf-8')

if 'rot_13' in w:
    s = w[34:]
    d = s.strip()
    e = codecs.encode(d, 'rot_13').decode('utf-8')
    io.sendline(e)

if 'decimal' in w:
    s = w[35:]
    m = s.split()
    c = [chr(int(d)) for d in m]
    r = ''.join(c)
    io.sendline(r)

if 'base64' in w:
    s = w[34:]
    d = base64.b64decode(s).decode('utf-8')
    io.sendline(d)

io.recvline().decode('utf-8')
io.recvline().decode('utf-8')
io.recvline().decode('utf-8')

o=io.recvline().decode('utf-8')
print("hello")


'''
def decrypt_vigenere(ciphertext, key):
    plaintext = ''
    key_length = len(key)
    key_pos = 0
    for v in ciphertext:
        if v.isalpha():
            key_char = key[key_pos]
            key_char_value = ord(key_char.upper()) - ord('A')
            if v.isupper():
                plaintext += chr((ord(v) - ord('A') - key_char_value) % 26 + ord('A'))
            else:
                plaintext += chr((ord(v) - ord('a') - key_char_value) % 26 + ord('a'))
            key_pos = (key_pos + 1) % key_length
        else:
            plaintext += v
    return plaintext

ciphertext = 'KOGPC BFVGS'
key = 'DORAEMON'

plaintext = decrypt_vigenere(ciphertext, key)


io.sendline(plaintext)

io.recvline().decode('utf-8')
io.recvline().decode('utf-8')
io.recvline().decode('utf-8')
io.recvline().decode('utf-8')

c=18167415270437429537561356386562779447469464022155874069515963318140212013529
n=47844259602799928024551309782664639583637896226311879436939149632896771229867
e=65537

p=191614070605110952231794677677612716251
q= 249690742708556448598543277120764053617
phi= (p - 1) * (q - 1)

d = inverse(e, phi)
priv = RSA.construct((n, e, d))

pubkey =
msg=b'18167415270437429537561356386562779447469464022155874069515963318140212013529'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)


cipher = PKCS1_OAEP.new(priv)   
msg = cipher.decrypt(str(c)).decode()

msg ='R5A_c4n_b3_3xpl0it3d'
io.sendline(msg)'''

io.interactive()
