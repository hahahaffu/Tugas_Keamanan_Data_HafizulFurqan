from customtkinter import *
from PIL import Image
import binascii
import io

# Fungsi untuk menyembunyikan pesan dalam gambar
def encode_message_to_image(image_path, message):
    # Mengubah pesan menjadi byte
    message_bytes = message.encode('utf-8')
    message_bin = ''.join(format(byte, '08b') for byte in message_bytes)
    
    # Membuka gambar
    image = Image.open(image_path)
    image = image.convert('RGB')  # Pastikan gambar dalam mode RGB
    pixels = image.load()
    
    # Menyembunyikan pesan pada pixel gambar
    data_index = 0
    for i in range(image.width):
        for j in range(image.height):
            pixel = list(pixels[i, j])
            for color in range(3):  # R, G, B
                if data_index < len(message_bin):
                    # Menyembunyikan bit pesan pada least significant bit
                    pixel[color] = (pixel[color] & ~1) | int(message_bin[data_index])
                    data_index += 1
            pixels[i, j] = tuple(pixel)
            if data_index >= len(message_bin):
                break
        if data_index >= len(message_bin):
            break
    
    # Menyimpan gambar baru dengan pesan yang disembunyikan
    encoded_image_path = 'encoded_image.png'
    image.save(encoded_image_path)
    return encoded_image_path

# Fungsi untuk mengambil pesan dari gambar
def decode_message_from_image(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = image.load()
    
    # Mengambil bit-bit dari pixel gambar
    message_bin = ''
    for i in range(image.width):
        for j in range(image.height):
            pixel = pixels[i, j]
            for color in range(3):
                message_bin += str(pixel[color] & 1)
    
    # Mengubah bit menjadi byte
    message_bytes = [message_bin[i:i+8] for i in range(0, len(message_bin), 8)]
    message = ''.join(chr(int(byte, 2)) for byte in message_bytes)
    
    # Menghapus karakter null (biasanya ada di akhir pesan)
    return message.split('\x00')[0]

def encode_text():
    message = entry_text.get()
    image_path = entry_image_path.get()
    
    if message == "" or image_path == "":
        result_label.configure(text="Pesan atau gambar tidak boleh kosong!")
        return
    
    encoded_image_path = encode_message_to_image(image_path, message)
    result_label.configure(text=f"Pesan disembunyikan dalam gambar.\nSimpan gambar: {encoded_image_path}")

def decode_text():
    image_path = entry_image_path.get()
    
    if image_path == "":
        result_label.configure(text="Gambar tidak boleh kosong!")
        return
    
    decoded_message = decode_message_from_image(image_path)
    result_label.configure(text=f"Pesan Tersembunyi: {decoded_message}")

# GUI
app = CTk()
app.geometry("500x400")
app.title("Program Steganografi Teks dalam Gambar")
set_appearance_mode("dark")

label = CTkLabel(master=app, text="Program Steganografi Teks dalam Gambar", font=("Poppins", 18), text_color="#FFCC70")
label.place(relx=0.5, rely=0.1, anchor="center")

# Label untuk teks yang akan dienkripsi
entry_text_label = CTkLabel(master=app, text="Pesan Teks:")
entry_text_label.place(relx=0.5, rely=0.22, anchor="center")

# Entry untuk pesan teks
entry_text = CTkEntry(master=app, placeholder_text="Masukkan pesan yang ingin disembunyikan...", width=300, text_color="#FFCC70")
entry_text.place(relx=0.5, rely=0.3, anchor="center")

# Label untuk path gambar
entry_image_path_label = CTkLabel(master=app, text="Path Gambar (untuk menyembunyikan pesan):")
entry_image_path_label.place(relx=0.5, rely=0.4, anchor="center")

# Entry untuk path gambar
entry_image_path = CTkEntry(master=app, placeholder_text="Masukkan path gambar...", width=300, text_color="#FFCC70")
entry_image_path.place(relx=0.5, rely=0.48, anchor="center")

# Label hasil steganografi
result_label = CTkLabel(master=app, text="Hasil Steganografi", font=("Poppins", 12))
result_label.place(relx=0.5, rely=0.6, anchor="center")

# Tombol untuk menyembunyikan pesan dalam gambar
btn_encode = CTkButton(master=app, text="Sembunyikan Pesan", corner_radius=30, fg_color="#FFCC70", text_color="#000000", hover_color="#4158D0", command=encode_text)
btn_encode.place(relx=0.35, rely=0.8, anchor="center")

# Tombol untuk mengambil pesan dari gambar
btn_decode = CTkButton(master=app, text="Ambil Pesan", corner_radius=30, fg_color="#FFCC70",  text_color="#000000", hover_color="#4158D0", command=decode_text)
btn_decode.place(relx=0.65, rely=0.8, anchor="center")

app.mainloop()
