Overview

This project demonstrates secure data transmission using authentication, hashing, encryption, and digital signatures. The application allows a user to log in, encrypt a message, verify its integrity, and validate authenticity using cryptographic techniques.

Features
User login with role-based access
SHA-256 hashing for integrity verification
AES symmetric encryption for confidentiality
Message decryption
Hash comparison validation
Digital signatures using RSA public/private keys
CIA Triad Implementation

Confidentiality
Confidentiality is achieved using AES encryption. Only users with the encryption key can decrypt the message.

Integrity
Integrity is ensured through SHA-256 hashing. The hash of the original message is compared with the decrypted message to detect tampering.

Availability
The system allows authenticated users to reliably access encryption and verification functions through a login system.

Entropy and Key Generation

Cryptographic strength depends on randomness (entropy). Encryption keys and RSA key pairs are generated using secure random number generators provided by the cryptography library. High entropy makes keys unpredictable and resistant to brute-force attacks.

Digital Signatures

Digital signatures use a private key to sign a message and a public key to verify it. In this application:

The private key signs the message.
The public key verifies authenticity.
This demonstrates how identity and data authenticity are validated in secure communications.
