def generate_key_mapping(key):
    key = key.upper()
    seen = set()
    mapping = {}

    # Urutkan huruf berdasarkan kunci (tanpa duplikat)
    new_alphabet = ''
    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            new_alphabet += char

    # Lengkapi dengan huruf-huruf lain
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in seen:
            new_alphabet += char

    # Buat peta dari A-Z ke new_alphabet
    for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        mapping[char] = new_alphabet[i]

    return mapping

def encrypt(text, key):
    mapping = generate_key_mapping(key)
    result = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            mapped = mapping[char.upper()]
            result += mapped if is_upper else mapped.lower()
        else:
            result += char
    return result
