# Function to encrypt the text using Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep any non-alphabetic characters unchanged
        else:
            result += char
    return result

# Function to decrypt the text using Caesar Cipher
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Main program logic
def main():
   
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_message = caesar_encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == 'D':
        decrypted_message = caesar_decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid choice! Please select 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
