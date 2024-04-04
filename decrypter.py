import os
import pyaes

# Nome do arquivo criptografado
file_name = 'teste.txt.ransomwaretroll'

# Abrir o arquivo criptografado
with open(file_name, 'rb') as file:
    file_data = file.read()

# Chave de descriptografia
key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Nome do novo arquivo descriptografado
new_file_name = 'teste.txt'

# Criar o novo arquivo descriptografado
with open(new_file_name, 'wb') as new_file:
    new_file.write(decrypt)
