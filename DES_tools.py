class DES_tools:

    def to_binary(text):
        # Convert text to binary
        binary = ""
        for char in text:
            binary += format(ord(char), '08b')
        return binary

    def slice_text(text, size):
        # Slice the text into blocks of size 'size' and return a list of blocks
        blocks = []
        for i in range(0, len(text), size):
            # Padding is following RFC 2898 recommendation https://www.rfc-editor.org/rfc/rfc2898#section-6.1.1
            padding = ""
            if i+size > len(text):
                padding += (i+size - len(text)) * "0"
                #padding_value = (i + size - len(text)) & 0xFF
                #padding = DES_tools.to_binary(chr(padding_value)) * (i + size - len(text))
                #print(hex(padding_value))
                #print(padding)
            blocks.append(text[i:i+size] + padding)

        return blocks

class DES_encrypt:

    S1 = [["101", "010", "001", "110", "011", "100", "111", "000"],
          ["011", "100", "110", "010", "000", "111", "101", "011"]]

    S2 = [["100", "000", "110", "101", "111", "001", "011", "010"],
          ["101", "011", "000", "111", "110", "010", "001", "100"]]

    def S_boxes(block):
        left_half = block[:len(block)//2]
        right_half = block[len(block)//2:]

        # Apply S-box 1
        lines = int(left_half[0])
        columns = int(left_half[1:], 2)
        s1 = DES_encrypt.S1[lines][columns]

        # Apply S-box 2
        lines = int(right_half[0])
        columns = int(right_half[1:], 2)
        s2 = DES_encrypt.S2[lines][columns]

        return (s1, s2)

    def expander(block):
        return block[:2] + block[3] + block[2:4] + block[2] + block[4:]

    def feistel(key, right_half):
        # Apply expansion permutation
        expanded = DES_encrypt.expander(right_half)
        # XOR with key
        xored_block = bin(int(expanded, 2) ^ int(key, 2))[2:].zfill(len(expanded))
        # Apply S-boxes
        (s1, s2) = DES_encrypt.S_boxes(xored_block)
        return s1 + s2

    def DES(key, block):
        L_i = block[:len(block)//2]
        R_i = block[len(block)//2:]
        return R_i + bin(int(L_i, 2) ^ int(DES_encrypt.feistel(key, R_i), 2))[2:]

class DES_decrypt:

    S1 = [["101", "010", "001", "110", "011", "100", "111", "000"],
          ["011", "100", "110", "010", "000", "111", "101", "011"]]

    S2 = [["100", "000", "110", "101", "111", "001", "011", "010"],
          ["101", "011", "000", "111", "110", "010", "001", "100"]]

    def reverse_S_boxes():
        pass

    def reverse_expander():
        pass

    def reverse_feistel():
        pass

    def reverse_DES():
        pass