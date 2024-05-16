from DES_tools import DES_encrypt, DES_decrypt, DES_tools

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

def encrypt(key, plain_text, rounds):
    binary_text = DES_tools.to_binary(plain_text)
    blocks = DES_tools.slice_text(binary_text, 12)

    cipher_text = []
    for block in blocks:
        for _ in range(rounds):
            block = DES_encrypt.DES(key, block).zfill(BLOCK_SIZE)
        cipher_text.append(block)

    return "".join(cipher_text)

def decrypt(key, cipher_text, rounds):
    pass

#plaintext = input("Enter the plain text: ")
#key = input("Enter the key (8 bits): ")
#rounds = int(input("Enter the number of rounds for DES: "))

plaintext = "test"
key = "10101010"
rounds = 5

# Encrypt the plain text
cipher_text = encrypt(key, plaintext, rounds)
print(f"The binary cipher text is: {cipher_text}")
print(f"The printable cipher text is: {binary_string_to_text(cipher_text)}")

# Decrypt the cipher text
#plain_text = decrypt(key, cipher_text, rounds)
#print(f"The plain text is: {plain_text}")

