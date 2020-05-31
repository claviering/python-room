import rsa
import binascii
with open('./RSA/pkcs1-private.pem', mode='rb') as privatefile:
  keydata = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata)

with open('./RSA/pkcs1-public.pem', mode='rb') as publicfile:
  keydata = publicfile.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata)

# rsa公钥加密
def rsaPublicEncrypt(str):
    content = str.encode('utf-8')
    crypto = rsa.encrypt(content, pubkey)
    return crypto

# rsa私钥解密
def rsaPrivateDecrypt(str):
    content = rsa.decrypt(str, privkey)
    con = content.decode('utf-8')
    return con

# rsa私钥加密
def rsaPriavteEncrypt(str):
    content = str.encode('utf-8')
    crypto = rsa.encrypt(content, privkey)
    return crypto

# rsa公钥解密
def rsaPublicDecrypt(str):
    content = rsa.decrypt(str, pubkey)
    con = content.decode('utf-8')
    return con


def runPublic():
  print('公钥加密, 私钥解密')
  str = rsaPublicEncrypt("hello")
  print('加密后密文：')
  # hex 格式
  print(binascii.hexlify(str))
  content = rsaPrivateDecrypt(str)
  print('解密后明文：')
  print(content)

def runPrivate():
  print('私钥加密, 公钥解密')
  str = rsaPriavteEncrypt("hello")
  print('加密后密文：')
  # hex 格式
  print(str)
  # print(str)
  # content = rsaPublicDecrypt(str)
  # print('解密后明文：')
  # print(content)

runPrivate()