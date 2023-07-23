# ejercicio 14



from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512

master_secret = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")
salt_id_dispositivo = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")
key1_disp = HKDF(master_secret, 32, salt_id_dispositivo, SHA512,1)

print("Clave Cifrado: ", key1_disp.hex())


# Clave Cifrado:  e716754c67614c53bd9bab176022c952a08e56f07744d6c9edb8c934f52e448a
# Podriamos generar mas de una clave pero en el ejercicio solo nos pedia una
# 