from User import User
from Password import Password
#import hashlib

password = b"bobo"

user1 = User()
user1.set_name("Bert")

p=Password()

hashed_password = p.hash_password(password)

user1.set_password(hashed_password)
hashed_password = user1.get_password()

p.hash_check(password, hashed_password)

#typical bandit findings
#>>> bandit -r <folder>
#password="123_x&5s" 
#hash_object = hashlib.md5(b'123_x32&')