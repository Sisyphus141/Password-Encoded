import hashlib

#take a key
key = str(input("KEY>>> "))
#take a message
password = str(input("MESSAGE>>> "))
#function does does something 

#make this more complex or something IDK
password = (key + password + key)

hash1 = hashlib.new("sha256")

password = password.encode("utf-8")
print(password)

hash1.update((password))
print(hash1.hexdigest())
