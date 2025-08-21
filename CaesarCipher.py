#@RaeRae-AFK

def caesar_encrypt(message: str, shift: int) -> str:
    result = []
    for c in message:
        if c.isalpha():
            # Preserve case
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)  #leaving non-letters unchanged
    return ''.join(result)


def caesar_decrypt(message: str, shift: int) -> str:
    return caesar_encrypt(message, -shift)


if __name__ == "__main__":  #main guard
    while True:
        choice = input("\nType 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").strip().lower()

        if choice == 'e':
            plain = input("Enter a message to encrypt: ")
            shift = int(input("Enter shift value: "))
            enc = caesar_encrypt(plain, shift)
            print(f"Encrypted Message: {enc}")

        elif choice == 'd':
            cipher = input("Enter a message to decrypt: ")
            shift = int(input("Enter shift value used for encryption: "))
            dec = caesar_decrypt(cipher, shift)
            print(f"Decrypted Message: {dec}")

        elif choice == 'q':
            print("BAIBAIII!")
            break

        else:
            print("Invalid choice. Please type 'e', 'd', or 'q'.")
