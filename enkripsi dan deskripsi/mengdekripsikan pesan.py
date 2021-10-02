from cryptography.fernet import Fernet

#Untuk mendapatkan kunci dari file 
file = open('key.key', 'rb')  
key = file.read()  # The key will be type bytes
file.close()

massage = "dewan perwakilan mahasiswa fakultas ilmu komputer"
encoded = massage.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)

file = open('key.key', 'rb') 
key2 = file.read()  # The key will be type bytes
file.close()

f2 = Fernet(key)
decrypted = decrypted = f2.decrypt(encrypted)

original_massage = decrypted.decode()
print (original_massage)
