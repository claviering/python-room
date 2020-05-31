import rsa
with open('./RSA/pkcs8-private.pem', mode='rb') as privatefile:
  keydata = privatefile.read()

print(keydata)
privkey = rsa.PrivateKey.load_pkcs1_openssl_pem(keydata)
print(privkey)

with open('./RSA/pkcs8-public.pem', mode='rb') as publicfile:
  keydata = publicfile.read()
pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(keydata)

print(pubkey)
# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    print(pubkey, privkey)
    # 明文编码格式
    content = str.encode('utf-8')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)

# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con

str, pk = rsaEncrypt("hello")
print('加密后密文：')
print(str)
print(pk)
content = rsaDecrypt(str, pk)
print('解密后明文：')
print(content)