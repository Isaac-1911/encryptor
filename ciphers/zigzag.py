def encrypt(text, rails):
    if rails <= 1:
        return text

    # Buat array kosong sejumlah rel
    fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1  # 1 = turun, -1 = naik

    for char in text:
        fence[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(fence)
