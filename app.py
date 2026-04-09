# ==========================================
# Secure Data Transmission Application
# Module 4 Midterm Project
# ==========================================

import json
import hashlib
from cryptography.fernet import Fernet

# Digital Signature Imports
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# ==========================================
# USER LOGIN (Authentication + RBAC)
# ==========================================

def load_users():
    with open("users.json", "r") as f:
        return json.load(f)["users"]


def login():
    users = load_users()

    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\nLogin successful! Role: {user['role']}")
            return user

    print("Login failed.")
    return None


# ==========================================
# SHA-256 HASHING (Integrity)
# ==========================================

def sha256_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()


# ==========================================
# AES ENCRYPTION (Confidentiality)
# ==========================================

def generate_key():
    return Fernet.generate_key()


def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message)
    return decrypted.decode()


# ==========================================
# INTEGRITY VERIFICATION
# ==========================================

def verify_integrity(original_hash, new_hash):
    return original_hash == new_hash


# ==========================================
# DIGITAL SIGNATURES (Outcome 4.3)
# ==========================================

# Generate RSA public/private key pair
def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


# Sign message using private key
def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


# Verify signature using public key
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False


# ==========================================
# MAIN APPLICATION FLOW
# ==========================================

def main():

    # LOGIN
    user = login()
    if not user:
        return

    print("\n--- Secure Data Transmission ---")

    # USER INPUT
    message = input("Enter message to secure: ")

    # HASH ORIGINAL MESSAGE
    original_hash = sha256_hash(message)
    print("\nOriginal SHA-256 Hash:")
    print(original_hash)

    # GENERATE AES KEY
    key = generate_key()
    print("\nEncryption Key Generated.")

    # ENCRYPT MESSAGE
    encrypted_message = encrypt_message(message, key)
    print("\nEncrypted Message:")
    print(encrypted_message)

    # DECRYPT MESSAGE
    decrypted_message = decrypt_message(encrypted_message, key)
    print("\nDecrypted Message:")
    print(decrypted_message)

    # VERIFY INTEGRITY
    new_hash = sha256_hash(decrypted_message)

    print("\nVerifying Integrity...")

    if verify_integrity(original_hash, new_hash):
        print("Integrity Verified ✅")
    else:
        print("Integrity Failed ❌")

    # ======================================
    # DIGITAL SIGNATURE DEMONSTRATION
    # ======================================

    print("\n--- Digital Signature Demonstration ---")

    private_key, public_key = generate_key_pair()

    signature = sign_message(private_key, message)
    print("Message Signed.")

    if verify_signature(public_key, message, signature):
        print("Digital Signature Verified ✅")
    else:
        print("Signature Verification Failed ❌")


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()