#include <stdio.h>
#include <string.h>

// XOR encryption function
void lock(const char *input, char *output, const char *key, int length) {
    int keyLength = strlen(key);  // Get the length of the key
    for (int i = 0; i < length; i++) {
        output[i] = input[i] ^ key[i % keyLength];  // XOR operation
    }
    output[length] = '\0';  // Null-terminate the output string
}

int main() {
    // The original flag that we want to XOR encode
    char originalFlag[] = "2WH4N-8QGBV-H22JP-CTF24-MDWWJ";
    int flagLength = strlen(originalFlag);  // Length of the original flag

    // Buffer to hold the encoded flag (ensure it's large enough to store the entire encoded string)
    char encodedFlag[100];  // Buffer should be large enough for the output

    // The XOR key used to encode the flag
    const char *key = "KEY";  // XOR key

    // Encoding the flag using the XOR key
    lock(originalFlag, encodedFlag, key, flagLength);

    // Output the encoded flag as integer values for each character
    printf("Encoded flag: {");
    for (int i = 0; i < flagLength; i++) {
        printf("%d", (unsigned char)encodedFlag[i]);  // Print as unsigned int to avoid negative values
        if (i < flagLength - 1) {
            printf(", ");
        }
    }
    printf("}\n");

    return 0;
}
