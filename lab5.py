import modes

#TEXTO 1

data = b"Bryann Diego Julio"

#EJEMPLO CON MODO CBC
result = modes.EncryptCBC(data)
print(result[1])
print('Texto original: ',modes.DecryptCBC(result))

#EJEMPLO CON MODO CFB
result = modes.EncryptCFB(data)
print(result[1])
print('Texto original: ',modes.DecryptCFB(result))

#EJEMPLO CON MODO OFB

result = modes.EncryptOFB(data)
print(result[1])
print('Texto original: ',modes.DecryptOFB(result))

#EJEMPLO CON MODO CTR
result = modes.EncryptCTR(data)
print(result[1])
print('Texto original: ',modes.DecryptCTR(result))


#EJEMPLO 2
data = b"El dia de hoy juan fue a la tienda por 4 panes."

#EJEMPLO CON MODO CBC
result = modes.EncryptCBC(data)
print(result[1])
print('Texto original: ',modes.DecryptCBC(result))

#EJEMPLO CON MODO CFB
result = modes.EncryptCFB(data)
print(result[1])
print('Texto original: ',modes.DecryptCFB(result))

#EJEMPLO CON MODO OFB

result = modes.EncryptOFB(data)
print(result[1])
print('Texto original: ',modes.DecryptOFB(result))

#EJEMPLO CON MODO CTR
result = modes.EncryptCTR(data)
print(result[1])
print('Texto original: ',modes.DecryptCTR(result))

#EJEMPLO 3
data = b"Las redes sociales son populares. 1234. "

#EJEMPLO CON MODO CBC
result = modes.EncryptCBC(data)
print(result[1])
print('Texto original: ',modes.DecryptCBC(result))

#EJEMPLO CON MODO CFB
result = modes.EncryptCFB(data)
print(result[1])
print('Texto original: ',modes.DecryptCFB(result))

#EJEMPLO CON MODO OFB

result = modes.EncryptOFB(data)
print(result[1])
print('Texto original: ',modes.DecryptOFB(result))

#EJEMPLO CON MODO CTR
result = modes.EncryptCTR(data)
print(result[1])
print('Texto original: ',modes.DecryptCTR(result))