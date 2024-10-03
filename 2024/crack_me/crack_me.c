#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Simple XOR encryption/decryption
void lock(char *input, char *output, const char *key, int length) {
    int keyLength = strlen(key);  // Getting the length of the key
    for(int i = 0; i < length; i++) {
        output[i] = input[i] ^ key[i % keyLength];  // XOR operation and handling key cycling
    }
    output[length] = '\0';  // Null terminate the decoded string
}

// Check password using a non-trivial logic
int authentication(const char *input) {
    const char encodedPassword[] =  {121, 18, 17, 127, 11, 116, 115, 20, 30, 9, 19, 116, 3, 119, 107, 1, 21, 116, 8, 17, 31, 121, 113, 116, 6, 1, 14, 28, 15};  // XOR encoded "2WH4N-8QGBV-H22JP-CTF24-MDWWJ"
    char decodedPassword[10];
    lock((char *)encodedPassword, decodedPassword, "KEY", 29);

    return strcmp(input, decodedPassword) == 0;
}

// Function to display the CTF flag when the password is correct
void jackpot() {
    const char encodedFlag[] = {19, 20, 53, 8, 71, 82, 20, 17, 16, 32, 20, 50, 19, 0, 92, 107, 98, 76, 31, 2, 95, 80, 93, 67, 23, 16, 50, 10, 14};


    char decodedFlag[30];

    // Decrypting the flag
    lock((char *)encodedFlag, decodedFlag, "P@ssw0rd4CTF2024Ch@ll3ng3", 30);
    decodedFlag[30] = '\0';  // Null terminate the decoded flag string

    printf("Please follow the provided instructions to access the CLA website and submit your license key: %s\n", decodedFlag);
}

int main() {
    char password[100];  // Buffer to store the user input temporarily

    printf("Enter the license KEY (MAXimum 29 characters): ");
    
    // Reading the input using fgets to handle large input and buffer overflows
    // fgets reads up to 99 characters (98 + null terminator) to avoid buffer overflow
    fgets(password, 100, stdin);
    
    // Remove the newline character from the input if present
    size_t len = strlen(password);
    if (password[len - 1] == '\n') {
        password[len - 1] = '\0';
    }

    // Check if the entered password is too long
    if (strlen(password) > 29) {
        printf("Error: License KEY too long! Please provide a valid KEY with a maximum of 29 characters.\n");
        return 1;  // Return an error code to indicate failure
    }

    // Call the authentication function to check if the entered password is correct
    if(authentication(password)) {
        // If the password is correct, grant access and call jackpot to show the flag
        printf("Access granted!\n");
        jackpot();  // Display the CTF flag
    } else {
        // If the password is incorrect, deny access
        printf("Access denied! Try again.\n");
    }

    return 0;
}
