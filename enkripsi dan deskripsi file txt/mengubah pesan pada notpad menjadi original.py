from cryptography.fernet import Fernet

#Untuk mendapatkan kunci dari file 
file = open('key.key', 'rb')  
key = file.read()  
file.close()

# Membuka file untuk di encrypt
with open('dpr.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Menulis encrypted file
with open('dpr.txt.encrypted', 'wb') as f:
    f.write(encrypted)
    
original_massage = decrypted.decode()
print (original_massage)
