import random                     # Import the random module to generate random strings.
import socketserver               # Import the socketserver module for creating a TCP server.
import socket, os                 # Import socket and os modules for network and operating system interactions.
import string                     # Import the string module to access common string constants.

flag = open('flag.txt', 'r').read().strip()  # Read the content of the 'flag.txt' file and remove any leading/trailing whitespace.

def send_message(server, message):          # Define a function to send a message to the client.
    enc = message.encode()                  # Encode the message into bytes.
    server.send(enc)                        # Send the encoded message to the client via the server socket.

def setup(server, key):                     # Define a setup function to XOR the flag with the given key.
    flag = 'CTF{thisisafakeflag}'           # A hardcoded flag (presumably for testing or placeholder purposes).
    xored = ""                              # Initialize an empty string to hold the XORed result.

    for i in range(0, len(flag)):           # Loop over each character in the flag.
        xored += chr(ord(flag[i]) ^ ord(key[i % len(key)]))  # XOR each character of the flag with the key (repeated as necessary).

    hex_encoded = xored.encode().hex()      # Convert the XORed result to a hexadecimal string.
    return hex_encoded                      # Return the hexadecimal encoded string.

def start(server):                          # Define the start function to initialize and run the challenge.
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=6))  # Generate a random 5-character key. (changed the key length)
    key = str(res)                          # Convert the random selection into a string to use as the key.
    hex_encoded = setup(server, key)        # Call the setup function to XOR the flag with the generated key.
    send_message(server, "This XOR encoded text has flag 1: " + hex_encoded + "\\n")  # Send the XORed flag to the client.

    send_message(server, "What is the encryption key? ")  # Ask the client to guess the encryption key.
    key_answer = server.recv(4096).decode().strip()       # Receive the client's response, decode, and remove any extra whitespace.

    try:                                                 # Start a try block to check the client's answer.
        if key_answer == key:                            # If the client's answer matches the key:
            send_message(server, "Congrats! That is the correct key! Here is flag 2: " + flag + "\\n")  # Send the second flag as a reward.
            server.close()                               # Close the server connection.
        else:                                            # If the client's answer is incorrect:
            send_message(server, 'Close but not quite. Try again!\\n')  # Notify the client that the answer is incorrect.
    except:                                              # If any exception occurs:
        send_message(server, 'An error occurred.\\n')    # Send an error message to the client.
        server.close()                                   # Close the server connection.
