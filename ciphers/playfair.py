def generate_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []

    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None, None

def preprocess(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += 'X'
    return result

def encrypt(text, key):
    matrix = generate_matrix(key)
    text = preprocess(text)
    ciphertext = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext
