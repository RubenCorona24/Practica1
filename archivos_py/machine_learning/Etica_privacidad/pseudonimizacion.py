#Pseudonimización
#Reemplacar datos identificables con pseudónimos
import uuid #Genera psudónimos
import pandas as pd
#Generamos un df

users = ['Sandra','Lenin','Fabiola']
id_pseudo = {u:str(uuid.uuid4()) for u in users} #Genera un diccinario con pseudónimos
print("-------UUID------------")
print(f"Pseudonimización por uuid: {id_pseudo}\n")

#Hashing (convertir datos en cadena de carácteres)
import hashlib
#Función para hashear dato
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
users = ['Diana','Lucia','Noria','Celia']
pseudonyms_hash = [hash_data(u) for u in users]
print("-------HASHLIB")
print(f"Pseudonimización por hashlib: {pseudonyms_hash}\n")

#Tokenización: reemplaza datos por tokens, pero se puede volver a recuperar el dato
tokens_table = {}
#Función para tokenizar un dato
def tokenizar(dato):
    token = str(uuid.uuid4())
    tokens_table[token] = dato
    return token
#Función para recuperar dato mediante token
def recuperar_dato(token):
    return tokens_table.get(token,'Token no Disponible')
dato_original = '123-456-789' #Creamos un dato original ej: número
token= tokenizar(dato_original)
print("----TOKENIZACIÓN-----")
print(f"Token: {token}")
print(f"Dato recuperado: {recuperar_dato(token)}\n")

#--------EJEMPLO DE PSEUDONIMIZACIÓN CON UN DATO---------
print(f"--------------Ejemplo aparte de pseudonimización---------------")
dato = "usuario@example.com"

# 1. UUID
pseud_uuid = str(uuid.uuid4())

# 2. HASH
pseud_hash = hashlib.sha256(dato.encode()).hexdigest()

# 3. TOKENIZACIÓN
tabla_tokens = {}
token = str(uuid.uuid4())
tabla_tokens[token] = dato

print("UUID:", pseud_uuid)
print("HASH:", pseud_hash)
print("TOKEN:", token)
print("Tabla tokens:", tabla_tokens)
