# def xorEncode(plaintext, key):
#     keyLength = len(key)
#     encoded = [c ^ ord(key[i % keyLength]) for i, c in enumerate(plaintext)]
#     return encoded

# # Original plaintext string
# plaintext = "CTF{B0und_Ch3ck_!$_4lw@ys_R3c00m3nd3d}"

# # The key used for XOR encoding
# xorKey = "k3Y4L!nux0v3rfl0W"

# # Encoding the plaintext string
# encodedText = xorEncode([ord(c) for c in plaintext], xorKey)

# print(f"Encoded Text: {encodedText}")

# def xorDecode(encoded, key):
#     keyLength = len(key)
#     decoded = ''.join([chr(c ^ ord(key[i % keyLength])) for i, c in enumerate(encoded)])
#     return decoded

# # Decoding the XOR-encoded string
# decodedText = xorDecode(encodedText, xorKey)

# print(f"Decoded Text: {decodedText}")

def xorDecode(encoded, key):
    keyLength = len(key)
    # decoded = ''.join([chr(c ^ ord(key[i % keyLength])) for i, c in enumerate(encoded)])
    # Define an empty string to store the decoded characters
    decoded = ''

    # Iterate through the encoded bytes and their indices
    for i, c in enumerate(encoded):
        # Calculate the position of the key character to use by taking the modulo
        # of the current index with the length of the key. This is to ensure that
        # the key repeats cyclically if it is shorter than the encoded message.
        keyIndex = i % keyLength
        # print(c);
        # Retrieve the ASCII value of the corresponding character in the key
        keyValue = ord(key[keyIndex])
        # print(keyValue);
        # Perform the XOR operation between the encoded byte and the key character's ASCII value
        decodedCharValue = c ^ keyValue
        # print(decodedCharValue);
        # Convert the resulting ASCII value back to a character
        decodedChar = chr(decodedCharValue)
        # print(decodedChar);#exit();
        # Append the decoded character to the decoded string
        decoded += decodedChar
    return decoded

# XOR-encoded string in hexadecimal format
encodedHex = [62, 55, 56, 44, 0, 23, 74, 16, 93]

# The key used for XOR encoding
xorKey = "key"

# Decoding the XOR-encoded string
decodedText = xorDecode(encodedHex, xorKey)

print(f"Decoded Text: {decodedText}")
