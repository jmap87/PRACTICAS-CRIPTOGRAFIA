# ejercicio 3



from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes

textoPlano_bytes = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
print(clave.hex())
nonce_mensaje = b64decode("9Yccn/f5nJJhAt2S")
cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado = cipher.encrypt(textoPlano_bytes)
print('Mensaje cifrado en HEX = ', texto_cifrado.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado).decode('utf-8'))

decipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
plaintext = decipher.decrypt(texto_cifrado)
print('Mensaje en claro = ',plaintext.decode('utf-8'))

# Respuesta
# af9df30474898787a45605ccb9b936d33b780d03cabc81719d52383480dc3120
# Mensaje cifrado en HEX =  69ac4ee7c4c552537a00a19bcaf7f0aaed7c9c8f769956a09bce6fadef6c3535f2211c9467067cf5c4a842ab
# Mensaje cifrado en B64 =  aaxO58TFUlN6AKGbyvfwqu18nI92mVagm85vre9sNTXyIRyUZwZ89cSoQqs=
# Mensaje en claro =  KeepCoding te enseña a codificar y a cifrar

# Seria mas seguro utilizando un nonce ramdom y con un chacha20poly por que utiliza un autentificador