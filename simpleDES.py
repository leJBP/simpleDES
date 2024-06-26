from DES_tools import DES, DES_tools, BLOCK_SIZE

def help():
    print("\nUsage: python simpleDES.py")
    print("This program encrypts and decrypts a plaintext using the simple DES algorithm.")
    print("The program will prompt the user to enter the plaintext, key, and the number of rounds for DES.")
    print("The key must be 8 bits long and the plaintext can be any length.")
    print("The number of rounds must be a positive integer.")
    print("The program will then output the encrypted and decrypted plaintext in binary and printable format.")
    exit()

def binary_string_to_text(binary_str):
    # Ensure the binary string length is a multiple of 8
    if len(binary_str) % 8 != 0:
        binary_str = binary_str[:-(len(binary_str) % 8)]

    # Split the binary string into chunks of 8 bits
    n = 8
    chunks = [binary_str[i:i + n] for i in range(0, len(binary_str), n)]

    # Convert each chunk to its corresponding ASCII character
    text = ''.join([chr(int(chunk, 2)) for chunk in chunks])

    return text

# simple DES encryption
def encrypt(keys, plaintext, rounds):
    binary_text = DES_tools.to_binary(plaintext)
    blocks = DES_tools.slice_text(binary_text, 12)

    ciphertext = []
    for block in blocks:
        for i in range(rounds):
            block = DES.encrypt(keys[i], block)
        ciphertext.append(block)

    return "".join(ciphertext)

# simple DES decryption
def decrypt(keys, ciphertext, rounds):
    blocks = DES_tools.slice_text(ciphertext, 12)

    plaintext = []
    for block in blocks:
        for i in range(rounds):
            block = DES.decrypt(keys[i], block)
        plaintext.append(block)

    return "".join(plaintext)

rounds = 0
plaintext = ""
key = ""

try:
    plaintext = input("Enter the plain text: ").strip()
    key = input("Enter the key (8 bits): ").strip()
    rounds = int(input("Enter the number of rounds for DES: "))
except Exception:
    help()

# Verify if the number of rounds is a positive integer
if rounds <= 0:
    rounds = -rounds
    print("The number of rounds must be a positive integer. Using the absolute value instead.")

# Verify if the key is 8 bits only composed of 0s and 1s
if not all(bit in '01' for bit in key) or len(key) != 8:
    help()

# Schedule the keys
print(f"Keys scheduled for {rounds} rounds")
keys = DES.key_schedule(key, rounds)

print(f"\nThe original binary plaintext is: {DES_tools.to_binary(plaintext)}")
print(f"The original plaintext is: {plaintext}\n")

# Encrypt the plain text
ciphertext = encrypt(keys, plaintext, rounds)
print(f"The encrypted binary ciphertext is: {ciphertext}")
print(f"The encrypted printable ciphertext is: {binary_string_to_text(ciphertext)}\n")


# Decrypt the cipher text
plaintext = decrypt(keys[::-1], ciphertext, rounds)
print(f"The decrypted binary plaintext is: {plaintext}")
print(f"The decrypted printable plaintext is: {binary_string_to_text(plaintext)}\n")

