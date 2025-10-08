#MD5
import hashlib
result = hashlib.md5(b"Hello")
result1 = hashlib.md5(b"Fello")
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
print("The byte equivalent of hash is : ", end ="")
print(result1.digest())