from Crypto.Cipher import AES
import base64

KEY = b'16CHARSLONGKEY!!'

def pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def encrypt(message):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(message))).decode()

def decrypt(message):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.decrypt(base64.b64decode(message)).decode().rstrip()
