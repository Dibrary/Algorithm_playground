
import hashlib

h = hashlib.sha1()
s = input()
h.update(s)
print(h.hexdigest())



