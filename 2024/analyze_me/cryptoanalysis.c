#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 2024
#define BUFFER_SIZE 1024

// Function to XOR encrypt the flag with the given key
void xor_encrypt(char *flag, char *key, char *output) {
    int flag_len = strlen(flag);
    int key_len = strlen(key);
    
    for (int i = 0; i < flag_len; i++) {
        output[i] = flag[i] ^ key[i % key_len];
    }
}

// Function to convert the XORed output to a hexadecimal string
void to_hex(char *input, int len, char *output) {
    for (int i = 0; i < len; i++) {
        // Format as hex without spaces or newlines
        sprintf(output + (i * 2), "%02x", (unsigned char)input[i]);
    }
}

// Function to handle client communication
void handle_client(int client_socket) {
    char flag[] = "CTF{BrUt3_ForC1nG_XOR_cAn_B3_FuN_nO?}";  // The hardcoded flag for demonstration
    char key[6];                           // Key will be 5 characters + null terminator
    char xor_output[BUFFER_SIZE];
    char hex_output[BUFFER_SIZE * 2];      // Since hex encoding will double the size
    char buffer[BUFFER_SIZE];

    // Generate a random 5-character key
    const char charset[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    for (int i = 0; i < 5; i++) {
        key[i] = charset[rand() % (sizeof(charset) - 1)];
    }
    key[5] = '\0';  // Null terminate the key

    // Ensure key is printed without newlines or extra spaces
    // printf("KEY is: %s\n", key);

    // XOR the flag with the key
    xor_encrypt(flag, key, xor_output);

    for (int i = 0; i < strlen(flag); i++) {
        printf("%02x", (unsigned char)xor_output[i]);
    }
    // printf("\n");

    // Convert XOR output to hexadecimal (no spaces or newlines)
    to_hex(xor_output, strlen(flag), hex_output);

    // Send the XORed and hex-encoded flag to the client
    snprintf(buffer, sizeof(buffer), "This XOR encoded text has flag 1: %s\n", hex_output);
    send(client_socket, buffer, strlen(buffer), 0);

    // Ask the client to provide the encryption key
    snprintf(buffer, sizeof(buffer), "What is the encryption key? ");
    send(client_socket, buffer, strlen(buffer), 0);

    // Receive the client's response
    int valread = read(client_socket, buffer, sizeof(buffer));
    buffer[valread - 1] = '\0';  // Remove the newline character

    // Check if the client's key matches
    if (strcmp(buffer, key) == 0) {
        snprintf(buffer, sizeof(buffer), "Congrats! That is the correct key! Here is flag 2: %s\n", flag);
        send(client_socket, buffer, strlen(buffer), 0);
    } else {
        snprintf(buffer, sizeof(buffer), "Close but not quite. Try again!\n");
        send(client_socket, buffer, strlen(buffer), 0);
    }

    close(client_socket);  // Close the client socket
}

int main() {
    srand(time(NULL));  // Seed the random number generator

    int server_fd, client_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);

    // Create socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attach socket to the port
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Bind the socket to the network address and port
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Start listening for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("Listen");
        exit(EXIT_FAILURE);
    }

    while (1) {
        printf("\n");
        printf("Waiting for a connection...\n");

        // Accept incoming connections
        if ((client_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0) {
            perror("Accept");
            exit(EXIT_FAILURE);
        }

        printf("Connection accepted.\n");
        handle_client(client_socket);  // Handle the client in a separate function
    }

    return 0;
}
