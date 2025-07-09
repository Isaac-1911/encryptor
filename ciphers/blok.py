def caesar(char, shift):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char

def permute_block(block, perm_key):
    # Permutasi index huruf dalam blok (0-3)
    if len(block) < 4:
        block += 'X' * (4 - len(block))  # padding
    perm_key = [int(x) % 4 for x in str(perm_key)]
    while len(perm_key) < 4:
        perm_key += perm_key  # ulangi jika pendek
    perm_key = perm_key[:4]
    return ''.join(block[i] for i in perm_key)

def encrypt(text, k1, k2, k3):
    # Normalisasi: blok-blok 4 karakter
    blocks = [text[i:i+4] for i in range(0, len(text), 4)]
    result = ''
    for block in blocks:
        shifted = ''.join(caesar(c, k1) for c in block)            # Shift Caesar
        subbed  = ''.join(caesar(c, (i * k2) % 26) for i, c in enumerate(shifted))  # Positional shift
        permuted = permute_block(subbed, k3)                       # Permutasi blok
        result += permuted
    return result
