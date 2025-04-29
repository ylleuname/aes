from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

  key = os.urandom(16)
  iv = os.urandom(16)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  
  mensagem = "Mensagem secreta"
  mensagem_bytes = mensagem.encode()
  mensagem_criptografada = cipher.encrypt(pad(mensagem_bytes, AES.block_size) print(" Mensagem Criptografada:", mensagem_criptografada.hex())
  
  #descriptografia
  decipher = AES.new(key, AES.MODE_CBC, iv)
  mensagem_descriptografada = unpad(decipher.decrypt(mensagem_criptografada), print(" Mensagem Descriptografada:", mensagem_descriptografada.decode())
