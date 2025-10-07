#SHA-256
import hashlib
str =  input("Enter the value to encode: ")
result = hashlib.sha1(str.encode())
print("The hexadecimal equivalent of hash is : ", result.hexdigest())