import binascii
from Crypto import Random
from Crypto.Protocol.KDF import scrypt
from Crypto.Cipher import AES
from Crypto.Util import Counter


SALT_BYTES = 16


def derive_key(mpw, salt_param=None):
    if salt_param is None:
        salt = Random.new().read(SALT_BYTES)
    else:
        salt = salt_param
    key = scrypt(mpw.encode(), salt, 32, N=2**20, r=8, p=1)
    return key, salt


def encrypt(key, pw):
    iv = Random.new().read(AES.block_size)
    iv_int = int(binascii.hexlify(iv), 16)
    ctr = Counter.new(AES.block_size*8, initial_value=iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    enc_pw = aes.encrypt(pw.encode('utf-8'))
    return iv, enc_pw


def decrypt(key, iv, encrypted):
    iv_int = int(binascii.hexlify(iv), 16)
    ctr = Counter.new(AES.block_size*8, initial_value=iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    pw = aes.decrypt(encrypted).decode('utf-8')
    return pw
