from cryptography.fernet import Fernet

#Untuk mendapatkan kunci dari file 
file = open('key.key', 'rb')  
key = file.read()  
file.close()

# penyandian pesan
massage = "dewan perwakilan mahasiswa fakultas ilmu komputer"
encoded = massage.encode()

# mengenkripsi pesannya
f = Fernet(key)
encrypted = f.encrypt(encoded)
print (encrypted)
