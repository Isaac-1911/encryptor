#!/bin/bash

# === VARIABEL ===
INSTALL_DIR="/usr/local/bin"
MAN_DIR="/usr/share/man/man1"
PROJECT_DIR="$(pwd)"
MAIN_SCRIPT="encryptor"
MAN_PAGE_FILE="encryptor.1"

echo "[+] Memulai proses instalasi Encryptor..."

# === Cek main script ===
if [ ! -f "$MAIN_SCRIPT" ]; then
    echo "[-] File $MAIN_SCRIPT tidak ditemukan di $PROJECT_DIR"
    exit 1
fi

# === Buat launcher ===
echo "[+] Membuat launcher /usr/local/bin/encryptor"
sudo bash -c "cat > $INSTALL_DIR/encryptor" <<EOF
#!/bin/bash
cd "$PROJECT_DIR"
./$MAIN_SCRIPT "\$@"
EOF

sudo chmod +x $INSTALL_DIR/encryptor

# === Tambahkan man page ===
if [ -f "$MAN_PAGE_FILE" ]; then
    echo "[+] Menambahkan man page ke $MAN_DIR"
    gzip -f "$MAN_PAGE_FILE"
    sudo cp "${MAN_PAGE_FILE}.gz" "$MAN_DIR"
else
    echo "[!] File man page tidak ditemukan. Lewat..."
fi

echo "[✔] Instalasi selesai. Coba jalankan: encryptor -h"
