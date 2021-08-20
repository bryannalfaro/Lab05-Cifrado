from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

def EncryptCBC(data, keys = None):
    if not keys:
        key = get_random_bytes(16)
    else:
        key = keys
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = iv,ct,key
    return result

def DecryptCBC(result):
    try:
        iv = b64decode(result[0])
        ct = b64decode(result[1])
        cipher = AES.new(result[2], AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt
    except:
        print("Incorrect decryption")

def EncryptCFB(data):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB)
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = iv,ct,key
    return result

def DecryptCFB(result):
    try:
        iv = b64decode(result[0])
        ct = b64decode(result[1])
        cipher = AES.new(result[2], AES.MODE_CFB, iv=iv)
        pt = cipher.decrypt(ct)
        return pt
    except:
        print("Incorrect decryption")

def EncryptOFB(data):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_OFB)
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = iv,ct,key
    return result

def DecryptOFB(result):

    try:

        iv = b64decode(result[0])
        ct = b64decode(result[1])
        cipher = AES.new(result[2], AES.MODE_OFB, iv=iv)
        pt = cipher.decrypt(ct)
        return pt
    except:
        print("Incorrect decryption")

#CTR DONT USE IV
def EncryptCTR(data):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CTR)
    ct_bytes = cipher.encrypt(data)
    nonce = b64encode(cipher.nonce).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = nonce,ct,key
    return result

def DecryptCTR(result):
    try:
        nonce = b64decode(result[0])
        ct = b64decode(result[1])
        cipher = AES.new(result[2], AES.MODE_CTR, nonce=nonce)
        pt = cipher.decrypt(ct)
        return pt
    except:
        print("Incorrect decryption")

def EncryptTextFile(key,text1, text2):
    file = open(text1,'r')
    texto =bytes(file.read(),'utf-8')
    cifrado = EncryptCBC(texto,key)
    f = open(text2,'w')
    f.write(cifrado[0]+'\n')
    f.write(cifrado[1]+'\n')

    f.close()
    file.close()


def DecryptTextFile(key,text1,text2):
    result  = []
    file = open(text1,'r')
    for line in file.readlines():
        result.append(line)

    result.append(key)
    descifrado = DecryptCBC(tuple(result))
    f = open(text2,'w')
    f.write(descifrado.decode('utf-8'))

    f.close()
    file.close()