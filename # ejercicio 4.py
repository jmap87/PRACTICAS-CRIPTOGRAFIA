# ejercicio 4

import jwt

print(" --- inicio ---")

encoded_jwt = jwt.encode({"mas": "complicado", "profe":"jajaja"}, "Con KeepCoding aprendemos", algorithm="HS256")

encoded_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE" 

print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"Con KeepCoding aprendemos", algorithms="HS256")

print(decode_jwt)

# Resultado

# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtYXMiOiJjb21wbGljYWRvIiwicHJvZmUiOiJqYWphamEifQ.xVEJIvfMrJMVeNDAH5xvPpTU8-WWLpdyg7VWpaW3y04

# ejercicio

# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE

# 'usuario': 'Don Pepito de los palotes', 'rol': 'isNormal', 'iat': 1667933533


# Segunda parte del ejercicio



print(" --- inicio ---")

encoded_jwt2 = jwt.encode({"mas": "complicado", "profe":"jajaja"}, "Con KeepCoding aprendemos", algorithm="HS256")

encoded_jwt2 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI" 

print(encoded_jwt2)

decode_jwt2 = jwt.decode(encoded_jwt2,"Con KeepCoding aprendemos", algorithms="HS256")

print(decode_jwt2)

# El hacker quiere obtener informacion para interntar escalar privilegios
# Da fallo en la verirficacion de la firma

