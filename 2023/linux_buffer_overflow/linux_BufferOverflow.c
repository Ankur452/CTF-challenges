#include <stdio.h>
#include <string.h>

// Simple XOR encryption/decryption
void bufferSize(char *input, char *output, const char *key, int length) {
    int keyLength = strlen(key);  // Getting the length of the key
    for(int i = 0; i < length; i++) {
        output[i] = input[i] ^ key[i % keyLength];  // XOR operation and handling key cycling
    }
    output[length] = '\0';  // Null terminate the decoded string
}

// Check password using a non-trivial logic
void overflowBit() {
    const char encodedFlag[] = {40, 103, 31, 79, 14, 17, 27, 27, 28, 111, 53, 91, 65, 5, 7, 111, 118, 79, 108, 109, 88, 59, 97, 23, 6, 39, 98, 69, 80, 66, 86, 1, 3, 57, 15, 0, 61, 73};

    char decodedFlag[56];

    // Decrypting the flag
    bufferSize((char *)encodedFlag, decodedFlag, "k3Y4L!nux0v3rfl0W", 55);
    decodedFlag[38] = '\0';  // Null terminate the decoded flag string

    printf("Here is your Flag: %s\n", decodedFlag);
}

void FindMe() {
    printf("Congratulations! You've triggered the buffer overflow and called this function.\n");
    overflowBit();
}

void vulnerable_function(char *str) {
    char buffer[64];  // A buffer with space for 64 characters
    strcpy(buffer, str);  // Copying the input string into the buffer without checking its length
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s <input_string>\n", argv[0]);
        return -1;
    }
    
    vulnerable_function(argv[1]);
    printf("Exiting normally.\n");
    return 0;
}
