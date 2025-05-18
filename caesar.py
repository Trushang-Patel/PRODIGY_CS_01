def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Normalize shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Shift within A-Z or a-z
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result

def main():
    print("=== Caesar Cipher ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift. Please enter an integer.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed message): {result}")

if __name__ == "__main__":
    main()
