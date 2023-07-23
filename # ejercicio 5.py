# ejercicio 5

# El siguiente hash se corresponde con un SHA3 Keccak del texto “En KeepCoding aprendemos 
# cómo protegernos con criptografía”.
# bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe
# ¿Qué tipo de SHA3 hemos generado?

# Generamos un SHA3-256 por la longitud del codigo 


#Y si hacemos un SHA2, y obtenemos el siguiente resultado:
#4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f
#6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833
#¿Qué hash hemos realizado?

# un SHA2-512


#Genera ahora un SHA3 Keccak de 256 bits con el siguiente texto: “En KeepCoding aprendemos cómo protegernos con criptografía.”
#¿Qué propiedad destacarías del hash, atendiendo a los resultados anteriores?

# Destacariamos que un minimo cambio en un byte este caso el punto del final del texto produciria un cambio total en el hash


import hashlib

s = hashlib.sha3_256()
print(s.name)
print(s.digest_size)
s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.","UTF-8"))
print(s.hexdigest())

