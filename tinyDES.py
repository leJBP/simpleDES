from DES_tools import DES, DES_tools

BLOCK_SIZE = 12

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

def encrypt(key, plaintext, rounds):
    binary_text = DES_tools.to_binary(plaintext)
    blocks = DES_tools.slice_text(binary_text, 12)

    ciphertext = []
    for block in blocks:
        for _ in range(rounds):
            block = DES.encrypt(key, block).zfill(BLOCK_SIZE)
        ciphertext.append(block)

    return "".join(ciphertext)

def decrypt(key, ciphertext, rounds):
    blocks = DES_tools.slice_text(ciphertext, 12)

    print(blocks)

    plaintext = []
    for block in blocks:
        for _ in range(rounds):
            block = DES.decrypt(key, block).zfill(BLOCK_SIZE)
        plaintext.append(block)

    return "".join(plaintext)

#plaintext = input("Enter the plain text: ")
#key = input("Enter the key (8 bits): ")
#rounds = int(input("Enter the number of rounds for DES: "))

plaintext = "test"
key = "10101010"
rounds = 5

print(f"The binary plaintext is: {DES_tools.to_binary(plaintext)}\n")

# Encrypt the plain text
cipher_text = encrypt(key, plaintext, rounds)
print(f"The binary ciphertext is: {cipher_text}")
print(f"The printable ciphertext is: {binary_string_to_text(cipher_text)}\n")

# Decrypt the cipher text
plain_text = decrypt(key, cipher_text, rounds)
print(f"The binary plaintext is: {plain_text}")
print(f"The printable plaintext is: {binary_string_to_text(plain_text)}\n")

