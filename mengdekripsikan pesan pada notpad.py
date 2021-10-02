from cryptography.fernet import Fernet

#Untuk mendapatkan kunci dari file 
file = open('key.key', 'rb')  
key = file.read()  
file.close()

# Membuka file untuk di encrypt
with open('dpr.txt.encrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

#Menulis encrypted file
with open('dpr.txt.decrypted', 'wb') as f:
    f.write(encrypted)
print(encrypted)
