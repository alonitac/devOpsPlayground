import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

publickey = key.publickey()

encrypted = publickey.encrypt('encrypt this message', 32)

print('encrypted message:', encrypted)

decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print('decrypted', decrypted)
