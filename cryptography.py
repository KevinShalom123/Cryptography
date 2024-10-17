from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Example usage:
# Generate a key
key = generate_key()

# Data to be encrypted
original_data = "Hello, this is a secret message."

# Encrypt the data
encrypted_data = encrypt_data(key, original_data)
print("Encrypted data:", encrypted_data)

# Decrypt the data
decrypted_data = decrypt_data(key, encrypted_data)
print("Decrypted data:", decrypted_data)
