
from Crypto.Random import get_random_bytes
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
print('HEREEE',type(result[1]),type(result[2]),type(result[0]))
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


#Encriptando archivos
key = get_random_bytes(16)
texto1 = 'texto.txt'
texto2 = 'cifrado.enc'
modes.EncryptTextFile(key,texto1,texto2)

texto3 = 'descifrado.dec'
modes.DecryptTextFile(key,texto2,texto3)