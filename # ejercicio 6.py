# ejercicio 6

from Crypto.Hash import HMAC, SHA256



def getHMAC(key_bytes,data_bytes):
    hmac256 = HMAC.new(key_bytes, msg=data_bytes, digestmod=SHA256)
    return hmac256.hexdigest()

def validateHMAC(key_bytes,data_bytes,hmac):
    hmac256 = HMAC.new(key_bytes,msg=data_bytes,digestmod=SHA256)
    result = "KO"
    try:
        hmac256.hexverify(hmac)
        result = "OK"
    except ValueError:
        result = "KO"
    print("result: " + result)
    return result

#----- Lo que queremos hacer ------
clave_bytes = bytes.fromhex('A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')
datos = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.", "utf8")

hmac = getHMAC(clave_bytes,datos)

print(hmac)


# Resultado HMAC

# 857d5ab916789620f35bcfe6a1a5f4ce98200180cc8549e6ec83f408e8ca0550