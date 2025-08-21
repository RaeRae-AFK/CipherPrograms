#@RaeRae-AFK

# Define base rows
row_letters_left  = "qwertyuiop"
row_letters_right = "zxcvbnm,./"
row_digits        = "1234567890"
row_home_letters  = "asdfghjkl;"

#shifted digits if home row letters are uppercase
row_digits_shifted = "!@#$%^&*()"

cipher_map = {}

#qwerty row <-> zxcvbnm row
for a, b in zip(row_letters_left, row_letters_right):
    cipher_map[a] = b #flip the mapping
    cipher_map[b] = a
    #uppercase handling
    if a.isalpha() and b.isalpha():
        cipher_map[a.upper()] = b.upper()
        cipher_map[b.upper()] = a.upper()

#digits row <-> home row
for d, h, ds in zip(row_digits, row_home_letters, row_digits_shifted):
    #lowercase letters
    cipher_map[d] = h
    cipher_map[h] = d
    #uppercase letters
    cipher_map[h.upper()] = ds
    cipher_map[ds] = h.upper()

#reverse map
reverse_map = {v: k for k, v in cipher_map.items()}

def encrypt(message: str) -> str:
    return ''.join(cipher_map.get(ch, ch) for ch in message)

def decrypt(message: str) -> str:
    return ''.join(reverse_map.get(ch, ch) for ch in message)

if __name__ == "__main__":  # main guard
    while True:
        choice = input("\nType 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").strip().lower()

        if choice == 'e':
            plain = input("Enter a message to encrypt: ")
            enc = encrypt(plain)
            print(f"Encrypted Message: {enc}")

        elif choice == 'd':
            cipher = input("Enter a message to decrypt: ")
            dec = decrypt(cipher)
            print(f"Decrypted Message: {dec}")

        elif choice == 'q':
            print("BAI BAIII!")
            break

        else:
            print("Invalid choice. Please type 'e', 'd', or 'q'.")

