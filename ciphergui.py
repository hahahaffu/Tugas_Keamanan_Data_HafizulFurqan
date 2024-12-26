from customtkinter import *

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def encrypt_text():
    plain_text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = enkripsi(plain_text, shift)
    result_label.configure(text=f"Hasil Enkripsi: {encrypted_text}")
    entry_text.delete(0, "end")  # Kosongkan kotak input
    entry_text.insert(0, encrypted_text)  # Isi kotak input dengan teks terenkripsi

def decrypt_text():
    cipher_text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = deskripsi(cipher_text, shift)
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
entry_shift_label = CTkLabel(master=app, text="Kunci:")
entry_shift_label.place(relx=0.5, rely=0.4, anchor="center")

# Entry untuk kunci enkripsi
entry_shift = CTkEntry(master=app, placeholder_text="Masukkan jumlah kunci...", width=300, text_color="#FFCC70")
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