from User import User
from Password import Password
import hashlib

#Example to trigger a sonar vulnerability
#import socket
#ip = '127.0.0.1'
#sock = socket.socket()
#sock.bind((ip, 9090))

#typical bandit findings
#>>> bandit -r <folder>
#deprecated md5 will not be found by sonar...
password="123_x&5s" 
hash_object = hashlib.md5(b'123_x32&')

password = b"bobo"

user1 = User()
user1.set_name("Bert")

p=Password()

hashed_password = p.hash_password(password)

user1.set_password(hashed_password)
hashed_password = user1.get_password()

p.hash_check(password, hashed_password)


