from User import User
from Password import passwordTester
import hashlib
import os
import bcrypt

password=os.getenv("123_x&5s")
hash_object = bcrypt.hashpw((b'123_x32&'),bcrypt.gensalt())

password = "bobo".encode()

user1 = User()
user1.set_name("Bert")

p = passwordTester()

hashed_password = p.hash_password(password)

user1.set_password(hashed_password)
hashed_password = user1.get_password()

p.hash_check(password, hashed_password)


