# Made by Cathal Murphy,
# Python Version = 3.7

import binascii
from Crypto.PublicKey import RSA


def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")


private_key = RSA.import_key(open("mykey2").read())
n = private_key.n
e = private_key.e
d = private_key.d

print("n = " + str(n))
print("e = " + str(e))
print("d = " + str(d))


