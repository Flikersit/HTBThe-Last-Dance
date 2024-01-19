from Crypto.Cipher import ChaCha20
import os
import binascii
def encryptMessage(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext


def writeData(data):
    with open("out.txt", "w") as f:
        f.write(data)

def decryptmessege(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=iv)
    ciphertext = cipher.decrypt(message)
    return ciphertext


message = b"Our counter agencies have intercepted your messages and a lot of your agent's identities have been exposed. In a matter of days all of them will be captured"

enc_msg = binascii.unhexlify(b"7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990")
iv = binascii.unhexlify(b'c4a66edfe80227b4fa24d431')
flag = binascii.unhexlify(b"7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7")
res = b''
for i in range(len(message)):
    res += bytes([message[i] ^ enc_msg[i]])
res2 = b''
for k in range(len(flag)):
    res2 += bytes([flag[k] ^ res[k]])
print(res2.decode('utf-8'))