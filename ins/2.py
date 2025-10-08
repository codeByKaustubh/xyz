#rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()

print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

pubKeyPEM = pubKey.export_key()
print(pubKeyPEM.decode('utf-8'))

print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

privKeyPEM = keyPair.export_key()
print(privKeyPEM.decode('utf-8'))

msg = b'Hello Class'

encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)

print("Encrypted:", binascii.hexlify(encrypted).decode('utf-8'))
