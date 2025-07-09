def pseudo_xor(c, key):
    return chr((ord(c) + key) % 126) if c.isprintable() else c

def encrypt(text, key1, key2, key3):
    result = ''
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            step1 = chr((ord(char) - base + key1) % 26 + base)           # Caesar
            step2 = chr((ord(step1) - base + (i * key2) % 26) % 26 + base) # Posisi
            step3 = pseudo_xor(step2, key3)                              # XOR-like
            result += step3
        else:
            result += char
    return result
