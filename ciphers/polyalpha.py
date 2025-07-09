def vigenere_char_encrypt(char, key_char):
    base = ord('A') if char.isupper() else ord('a')
    key_shift = ord(key_char.lower()) - ord('a')
    return chr((ord(char) - base + key_shift) % 26 + base)

def encrypt(text, key1, key2):
    result = ''
    key1 = key1.lower()
    key2 = key2.lower()
    k1_index = 0
    k2_index = 0

    for i, char in enumerate(text):
        if char.isalpha():
            if i % 2 == 0:
                key_char = key1[k1_index % len(key1)]
                k1_index += 1
            else:
                key_char = key2[k2_index % len(key2)]
                k2_index += 1

            result += vigenere_char_encrypt(char, key_char)
        else:
            result += char

    return result
