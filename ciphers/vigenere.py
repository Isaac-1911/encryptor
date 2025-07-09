def encrypt(text, keyword):
    result = ''
    keyword = keyword.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_char = keyword[key_index % len(keyword)]
            key_shift = ord(key_char) - ord('a')
            shifted = (ord(char) - base + key_shift) % 26
            result += chr(base + shifted)
            key_index += 1
        else:
            result += char  # Biarkan karakter non-alfabet
    return result
