#include <stdio.h>   // Required for input/output operations like printf and scanf
#include <string.h>  // Required for handling string operations like strlen and strcmp
#include <stdlib.h>  // Standard library, included for general purpose functions like memory management

// Function for simple XOR encryption/decryption
// input: the original string or the encrypted data
// output: the result of encryption or decryption
// key: the key used to XOR with the input data
// length: the length of the input data
void lock(char *input, char *output, const char *key, int length) {
    int keyLength = strlen(key);  // Get the length of the key for key cycling
    // Iterate over each character of the input string
    for(int i = 0; i < length; i++) {
        // Perform XOR operation between input[i] and the key character
        // Use modulus to cycle through the key if it's shorter than the input
        output[i] = input[i] ^ key[i % keyLength];
    }
    // Null terminate the output string to ensure it's a valid C string
    output[length] = '\0';
}

// Function to authenticate the password entered by the user
// input: the user-entered password
// returns: 1 if password matches, 0 otherwise
int authentication(const char *input) {
    // Encoded password using XOR operation ("URAGen!u$") with the key "key"
    const char encodedPassword[] = {62, 55, 56, 44, 0, 23, 74, 16, 93};  // Pre-encoded XOR result
    char decodedPassword[10];  // Buffer to store the decoded password

    // Call the lock function to decode the password using the same XOR key
    lock((char *)encodedPassword, decodedPassword, "key", 9);

    // Debugging (Optional): Uncomment the following lines for debug purposes
    // printf("Input received: %s\n", input);  // Display the user input
    // printf("Decoded password: %s\n", decodedPassword);  // Show the decoded password

    // Compare the decoded password with the user input using strcmp
    // Return 1 if they match, 0 otherwise
    return strcmp(input, decodedPassword) == 0;
}

// Function to display the CTF flag when the password is correct
void jackpot() {
    // XOR encoded CTF flag string
    const char encodedFlag[] = {19, 20, 53, 8, 71, 82, 20, 17, 16, 32, 96, 50, 1, 111, 75, 3, 48, 4, 108, 45, 27, 52, 115, 14};

    char decodedFlag[46];  // Buffer to store the decoded flag

    // Call the lock function to decode the flag using the key "P@ssw0rd4CTF2023Ev3n+"
    // which is a longer and more complex key suitable for this length of data
    lock((char *)encodedFlag, decodedFlag, "P@ssw0rd4CTF2023Ev3n+", 45);

    // Null terminate the decoded flag string at the correct position
    decodedFlag[24] = '\0';

    // Print the decoded flag to the user as their "reward"
    printf("Here is your Flag: %s\n", decodedFlag);
}

int main() {
    char password[50];  // Buffer to store user-entered password (50 chars max)

    // Prompt the user to enter the password
    printf("Enter the password: ");
    
    // Use scanf to read the password, limiting input to 49 characters to prevent buffer overflow
    scanf("%49s", password);

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
