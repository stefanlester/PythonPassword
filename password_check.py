#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt
import hmac
from User import User

def hash_password(password_string):
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password

def hash_check(cleartext_password, hashed_password):
    if (hmac.compare_digest(bcrypt.hashpw(cleartext_password, hashed_password), hashed_password)):
        print("Yes")
    else:
        print("No")    

#pw = input("Passwort: ")
#password = str.encode(pw) #Conversion string to bytes

password = b"bobo"

user1 = User()
user1.set_name("Bert")

hashed_password = hash_password(password)

user1.set_password(hashed_password)
hashed_password = user1.get_password()

hash_check(password, hashed_password)