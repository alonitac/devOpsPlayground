from Crypto.Cipher import AES
import base64

secret_key = '1234123412341234'
msg_text = '###############My id is 31334596'

cipher = AES.new(secret_key, AES.MODE_ECB)

msg_text_encrypted = cipher.encrypt(msg_text)

encoded = base64.b64encode(msg_text_encrypted)

# send message to destination................

msg_text_encrypted = base64.b64decode(encoded)
decoded = cipher.decrypt(msg_text_encrypted)
print(decoded)
