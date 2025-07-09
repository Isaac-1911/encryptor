import socket
import threading
from typing import Callable

# ---- Caesar Cipher ----
def caesar_encrypt(text: str, shift: int = 3) -> str:
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text: str, shift: int = 3) -> str:
    return caesar_encrypt(text, -shift)

# ---- Client setup ----
HOST = '192.168.1.69'  # ganti sesuai IP server
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print(f"[+] Connected to server {HOST}:{PORT}")

def handle_receive(sock: socket.socket, decrypt_fn: Callable[[str], str]):
    while True:
        data = sock.recv(1024).decode()
        if not data:
            print("[*] Server disconnected.")
            break
        print("Server:", decrypt_fn(data))

def handle_send(sock: socket.socket, encrypt_fn: Callable[[str], str]):
    while True:
        msg = input()
        if msg.lower() in ('exit', 'bye'):
            # encrypt + encode
            sock.sendall(encrypt_fn("bye").encode('utf-8'))
            print("[*] Closing connection.")
            sock.close()
            break
        # encrypt + encode
        sock.sendall(encrypt_fn(msg).encode('utf-8'))


threading.Thread(target=handle_receive, args=(sock, caesar_decrypt), daemon=True).start()
threading.Thread(target=handle_send, args=(sock, caesar_encrypt), daemon=True).start()


threading.Event().wait()
