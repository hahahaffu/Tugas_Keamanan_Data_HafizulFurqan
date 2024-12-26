from customtkinter import *
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def enkripsi(plain_text, key):
    # DES membutuhkan kunci sepanjang 8 byte
    key = key.ljust(8, '0').encode()  # Pastikan kunci sepanjang 8 byte
    cipher = DES.new(key, DES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode(), DES.block_size))
    iv = binascii.hexlify(cipher.iv).decode()  # Menyimpan IV dalam bentuk hex
    cipher_text = binascii.hexlify(cipher_text).decode()  # Enkripsi dan ubah ke bentuk hex
    return iv + cipher_text  # Gabungkan IV dan ciphertext

def deskripsi(cipher_text, key):
    # Ambil IV dari cipher_text
    iv = binascii.unhexlify(cipher_text[:16])  # IV sepanjang 8 byte
    cipher_text = binascii.unhexlify(cipher_text[16:])  # Ciphertext setelah IV
    key = key.ljust(8, '0').encode()  # Pastikan kunci sepanjang 8 byte
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(cipher_text), DES.block_size).decode()
    return decrypted_text

def encrypt_text():
    plain_text = entry_text.get()
    key = entry_shift.get()  # Menggunakan key yang dimasukkan oleh pengguna
    encrypted_text = enkripsi(plain_text, key)
    result_label.configure(text=f"Hasil Enkripsi: {encrypted_text}")
    entry_text.delete(0, "end")  # Kosongkan kotak input
    entry_text.insert(0, encrypted_text)  # Isi kotak input dengan teks terenkripsi

def decrypt_text():
    cipher_text = entry_text.get()
    key = entry_shift.get()  # Menggunakan key yang dimasukkan oleh pengguna
    decrypted_text = deskripsi(cipher_text, key)
    result_label.configure(text=f"Hasil Dekripsi: {decrypted_text}")
    entry_text.delete(0, "end")  # Kosongkan kotak input
    entry_text.insert(0, decrypted_text)  # Isi kotak input dengan teks dekripsi

# GUI
app = CTk()
app.geometry("500x400")
app.title("Program Enkripsi dan Deskripsi Teks")
set_appearance_mode("dark")

label = CTkLabel(master=app, text="Program Enkripsi dan Deskripsi Teks", font=("Poppins", 18), text_color="#FFCC70")
label.place(relx=0.5, rely=0.1, anchor="center")

# Label untuk teks yang akan dienkripsi
entry_text_label = CTkLabel(master=app, text="PlainTeks:")
entry_text_label.place(relx=0.5, rely=0.22, anchor="center")

# Entry untuk teks yang akan dienkripsi
entry_text = CTkEntry(master=app, placeholder_text="Masukkan teks yang ingin dienkripsi...", width=300, text_color="#FFCC70")
entry_text.place(relx=0.5, rely=0.3, anchor="center")

# Label untuk kunci enkripsi
entry_shift_label = CTkLabel(master=app, text="Kunci (8 karakter):")
entry_shift_label.place(relx=0.5, rely=0.4, anchor="center")

# Entry untuk kunci enkripsi
entry_shift = CTkEntry(master=app, placeholder_text="Masukkan kunci 8 karakter...", width=300, text_color="#FFCC70")
entry_shift.place(relx=0.5, rely=0.48, anchor="center")

# Label hasil enkripsi
result_label = CTkLabel(master=app, text="Hasil Enkripsi atau Dekripsi", font=("Poppins", 12))
result_label.place(relx=0.5, rely=0.6, anchor="center")

# Tombol untuk enkripsi
btn_encrypt = CTkButton(master=app, text="Enkripsi", corner_radius=30, fg_color="#FFCC70", text_color="#000000", hover_color="#4158D0", command=encrypt_text)
btn_encrypt.place(relx=0.35, rely=0.8, anchor="center")

# Tombol untuk dekripsi
btn_decrypt = CTkButton(master=app, text="Dekripsi", corner_radius=30, fg_color="#FFCC70",  text_color="#000000", hover_color="#4158D0", command=decrypt_text)
btn_decrypt.place(relx=0.65, rely=0.8, anchor="center")

app.mainloop()
