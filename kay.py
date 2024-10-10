import tkinter as tk
from tkinter import filedialog
import YcMesajKutusu

# Global değişken
current_file = None

def open_file(pad):
    global current_file
    current_file = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Metin Dosyaları", "*.txt"),
                                                         ("Tüm Dosyalar", "*.*")])
    if current_file:
        try:
            with open(current_file, "r", encoding="utf-8") as file:
                pad.delete(1.0, tk.END)  # Mevcut metni temizle
                pad.insert(tk.END, file.read())  # Dosya içeriğini ekle
        except UnicodeDecodeError:
            try:
                with open(current_file, "r", encoding="latin-1") as file:
                    pad.delete(1.0, tk.END)  # Mevcut metni temizle
                    pad.insert(tk.END, file.read())  # Dosya içeriğini ekle
            except Exception as e:
                YcMesajKutusu.mesaj(baslik="Hata", msj=f"Dosya okunamadı: {e}")
    return current_file  # Dosya yolunu geri döndür

def save_file(pad):
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(pad.get(1.0, tk.END))
        YcMesajKutusu.mesaj(baslik="Dosya Kaydet", msj="Dosya kaydedildi.")
    else:
        current_file = save_as_file(pad)
    return current_file  # Dosya yolunu geri döndür

def save_as_file(pad):
    global current_file
    current_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Metin Dosyaları", "*.txt"),
                                                             ("Tüm Dosyalar", "*.*")])
    if current_file:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(pad.get(1.0, tk.END))
        YcMesajKutusu.mesaj(baslik="Farklı Kaydet", msj="Dosya kaydedildi.")
    return current_file  # Dosya yolunu geri döndür

def new_file(pad):
    global current_file
    pad.delete(1.0, tk.END)  # Mevcut metni temizle
    current_file = None  # Dosya yolunu sıfırla
