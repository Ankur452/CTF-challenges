import binascii  # Import binascii module to handle binary to ASCII encoding and decoding

# Function to decrypt the XOR-encrypted hex string using the provided key
def xor_decrypt(hex_string, key):
    # Convert the hex-encoded string back into its original byte sequence
    encrypted_bytes = binascii.unhexlify(hex_string)

    # Ensure that the key is repeated enough to cover the entire encrypted message
    repeated_key = (key * (len(encrypted_bytes) // len(key) + 1))[:len(encrypted_bytes)]

    # XOR each byte of the encrypted message with the corresponding byte of the repeated key
    decrypted_bytes = bytes([b ^ ord(repeated_key[i]) for i, b in enumerate(encrypted_bytes)])

    # Convert the XORed byte sequence back into a string (UTF-8), ignoring decoding errors
    decrypted_message = decrypted_bytes.decode('utf-8', errors='ignore')

    return decrypted_message  # Return the fully decrypted message

# Main process for recovering the key and decrypting the message

# Prompt the user for the hex-encoded message they want to brute-force
hex_encoded_message = input("Enter the XOR encrypted hex string: ")

# Convert the hex-encoded message into a byte array for XOR operations
encrypted_bytes = binascii.unhexlify(hex_encoded_message)

# Known plaintext structure at the start of the flag, common in CTF flags
known_plaintext_start = "CTF{"  # We assume we know the flag starts with "CTF{"
known_plaintext_end = "}"  # We also assume the flag ends with a closing brace "}"

# 1. Recover the first part of the key using the known start of the flag ("CTF{").
# We XOR the first part of the ciphertext with the known plaintext to recover the key.
key = [encrypted_bytes[i] ^ ord(known_plaintext_start[i]) for i in range(len(known_plaintext_start))]

# 2. Recover the last character of the key by XORing the last character of the ciphertext with the expected "}".
# This approach works because the key is repeated, so the last character of the flag should align with the last character of the key.
for i in range(1, len(known_plaintext_end) + 1):
    key.append(encrypted_bytes[-i] ^ ord(known_plaintext_end[-i]))

# 3. Define the expected length of the key.
# We assume the key length is 5 characters based on the encryption scheme used in the C code.
key_length = 5

# 4. Check if we need to extend the key to reach the correct length.
# If the key is shorter than the expected length, we must repeat the key cyclically.
# This is done by repeating already recovered characters from the start of the key.
while len(key) < key_length:
    key.append(key[len(key) - key_length])

# 5. Convert the recovered key from a list of integers (XOR results) into a string of characters.
# Each integer corresponds to a character in the key (derived from the ASCII code).
key = ''.join([chr(k) for k in key])

# 6. Use the fully recovered key to decrypt the entire message using the XOR decryption function.
decrypted_message = xor_decrypt(hex_encoded_message, key)

# 7. Print out the recovered key and the decrypted message.
# For now, we are only printing the recovered key.
print(f"Encryption key: {key}")
# You can uncomment the next line to print the decrypted message.
# print(f"Decrypted message: {decrypted_message}")
