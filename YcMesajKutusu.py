from sys import exit

try:
	import customtkinter as ctk
except:
	print("Hata: Bağımlılıklar bulunamadı\nLütfen Customtkinter kütüphanesini indirin\n\npip install customtkinter")
	input()
	exit()

def mesaj(msj="",baslik="",renk=""):
	kutu = ctk.CTk()
	kutu.minsize(240,100)
	kutu.geometry("240x100+30+10")
	if baslik == "":
		kutu.title("Mesaj kutusu")
	else:
		kutu.title(baslik)

	mesaj = ctk.CTkLabel(kutu,text=msj,font=("italic",20))
	mesaj.pack(pady=40)

	if renk == "":
		pass
	elif renk == "siyah":
		mesaj.configure(text_color="black")
	elif renk == "kırmızı":
		mesaj.configure(text_color="red")
	elif renk == "mavi":
		mesaj.configure(text_color="blue")


	kutu.mainloop()


