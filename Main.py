"""
Bu program ilk başta kapalı kaynak olarak windwos için yapıştım
Linuxa geçince bu programı geliştirmeyi bırakmıştım,
ama bunun hatalarını düzeltip linux'a adapte etmeye karar verdim,
ve açık kaynk olarka yayınlamaya

Yiğit çıtak tarafından programlanmıştır.
"""
import customtkinter as ctk
import kay
from os import getenv
from os import mkdir

kullanici_dizini = getenv('HOME')
version = (1.0, "kararlı sürüm")

def system_save(
	name="",
	durum=True,
	durum2=0,
	durum3=False,
	durum4=0,
	durum5=0
	):
	if name == "tema":
		if durum == True:
			file_tema = open(f"{kullanici_dizini}/.micropad/system-save-tema.YC","w")
			file_tema.write("1")
			file_tema.close()
		elif durum == False:
			file_tema = open(f"{kullanici_dizini}/.micropad/system-save-tema.YC","w")
			file_tema.write("0")
			file_tema.close()

	elif name == "windowColor":
		if durum2 == 1:
			file_window = open(f"{kullanici_dizini}/.micropad/system-save-windowColor.YC","w")
			file_window.write("1")
			file_window.close()
		elif durum2 == 2:
			file_window = open(f"{kullanici_dizini}/.micropad/system-save-windowColor.YC","w")
			file_window.write("2")
			file_window.close()
		elif durum2 == 3:
			file_window = open(f"{kullanici_dizini}/.micropad/system-save-windowColor.YC","w")
			file_window.write("3")
			file_window.close()
		elif durum2 == 4:
			file_window = open(f"{kullanici_dizini}/.micropad/system-save-windowColor.YC","w")
			file_window.write("4")
			file_window.close()
		elif durum2 == 5:
			file_window = open(f"{kullanici_dizini}/.micropad/system-save-windowColor.YC","w")
			file_window.write("5")
			file_window.close()
		elif durum2 == 6:
			file_window = open(f"{kullanici_dizini}/.micropad/system-save-windowColor.YC","w")
			file_window.write("6")
			file_window.close()
		elif durum2 == 7:
			file_window = open(f"{kullanici_dizini}/.micropad/system-save-windowColor.YC","w")
			file_window.write("7")
			file_window.close()

	elif name == "genismi":
		if durum3 == True:
			file_genismi = open(f"{kullanici_dizini}/.micropad/system-save-genismi.YC","w")
			file_genismi.write("1")
			file_genismi.close
		elif durum3 == False:
			file_genismi = open(f"{kullanici_dizini}/.micropad/system-save-genismi.YC","w")
			file_genismi.write("0")
			file_genismi.close()

	elif name == "yaziRenk":
		if durum4 == 1:
			file_yaziRenk = open(f"{kullanici_dizini}/.micropad/system_save_yaziRenk.YC","w")
			file_yaziRenk.write("1")
			file_yaziRenk.close()
		elif durum4 == 2:
			file_yaziRenk = open(f"{kullanici_dizini}/.micropad/system_save_yaziRenk.YC","w")
			file_yaziRenk.write("2")
			file_yaziRenk.close()
		elif durum4 == 3:
			file_yaziRenk = open(f"{kullanici_dizini}/.micropad/system_save_yaziRenk.YC","w")
			file_yaziRenk.write("3")
			file_yaziRenk.close()
		elif durum4 == 4:
			file_yaziRenk = open(f"{kullanici_dizini}/.micropad/system_save_yaziRenk.YC","w")
			file_yaziRenk.write("4")
			file_yaziRenk.close()

def system_save_tema():
	file_tema = open(f"{kullanici_dizini}/.micropad/system-save-tema.YC","r")
	veri = file_tema.read()
	return veri
	file_tema.close()

def system_save_windowColor():
	file_tema = open(f"{kullanici_dizini}/.micropad/system-save-windowColor.YC","r")
	veri = file_tema.read()
	return veri
	file_tema.close()

def system_save_genismi():
	file_genismi = open(f"{kullanici_dizini}/.micropad/system-save-genismi.YC","r")
	veri = file_genismi.read()
	return veri
	file_genismi.close()

def system_save_yaziRenk():
	file_yaziRenk = open(f"{kullanici_dizini}/.micropad/system_save_yaziRenk.YC","r")
	veri = file_yaziRenk.read()
	return veri
	file_yaziRenk.close()

def program():
	try:
		mkdir(f"{kullanici_dizini}/.micropad")
		print("Bilgi: sistem kayıt dosyası oluçturuldu")
	except:
		print("Bilgi: sistem kayıt dosyası algılandı")

	global current_file
	current_file = None

	def update_current_file_save():
		global current_file
		current_file = kay.save_file(pad)

	def update_current_file_open():
		global current_file
		current_file = kay.open_file(pad)

	def update_current_file_save_as():
		global current_file
		current_file = kay.save_as_file(pad)

	def update_new_file():
		global current_file
		current_file = kay.new_file(pad)


	#dark colors:
	renk_window_dark = "#6A5ACD"
	renk_buton_dark = "#660099"
	renk_buton_secili_dark = "#800080"
	renk_secenek_dark = "#4B0082"


	window = ctk.CTk()
	window.title("Micropad")
	window.minsize(900,500)
	window.geometry("1200x700")

	try:
		if system_save_tema() == "0":
			ctk.set_appearance_mode("dark")
		elif system_save_tema() == "1":
			ctk.set_appearance_mode("light")
	except:
		ctk.set_appearance_mode("dark")

	title = ctk.CTkLabel(
		window,
		text="\nMicropad\n",
		font=("Poppins",30),
		text_color="white"
		)
	title.pack(pady=8)

	try:
		if system_save_windowColor() == "1":
			window.configure(fg_color=renk_window_dark)
			title.configure(text_color="white")

		elif system_save_windowColor() == "2":
			window.configure(fg_color="#0033FF")
			title.configure(text_color="white")

		elif system_save_windowColor() == "3":
			window.configure(fg_color="#008000")
			title.configure(text_color="white")

		elif system_save_windowColor() == "4":
			window.configure(fg_color="white")
			title.configure(text_color="black")

		elif system_save_windowColor() == "5":
			window.configure(fg_color="#696969")
			title.configure(text_color="black")

		elif system_save_windowColor() == "6":
			window.configure(fg_color="black")
			title.configure(text_color="white")

		elif system_save_windowColor() == "7":
			window.configure(fg_color="#FF00CC")
			title.configure(text_color="white")
	except:
		window.configure(fg_color=renk_window_dark)
		title.configure(text_color="white")	

	global pad
	pad = ctk.CTkTextbox(
		window,
		height=4000,
		width=1900,
		pady=10,
		padx=10,
		font=("Arial",20),
		wrap="word"
		)
	pad.pack(pady=2,padx=7)
	try:
		if system_save_yaziRenk() == "1":
			pad.configure(text_color="white")
		elif system_save_yaziRenk() == "2":
			pad.configure(text_color="red")
		elif system_save_yaziRenk() == "3":
			pad.configure(text_color="black")
		elif system_save_yaziRenk() == "4":
			pad.configure(text_color="blue")
	except:
		pass

	def dosya_icerik():
		def geri():
			dosya_buton.configure(fg_color=renk_buton_dark)
			dosya.place_forget()
			try:
				gorunum.place_forget()
			except:
				pass
			dosya_buton.configure(command=dosya_icerik)
			gorunum_buton.configure(command=gorunum_icerik)

		try:
			gorunum.place_forget()
		except:
			pass

		global dosya

		gorunum_buton.configure(fg_color=renk_buton_dark)
		dosya_buton.configure(fg_color=renk_buton_secili_dark)

		dosya = ctk.CTkScrollableFrame(
			window,
			height=20,
			width=100,
			fg_color=renk_secenek_dark
			)
		dosya.place(x=7,y=42)

		kaydet = ctk.CTkButton(
			dosya,
			text="Kaydet",
			fg_color=renk_buton_dark,
			command=update_current_file_save,
			)
		kaydet.pack(pady=5)

		farkli_ac = ctk.CTkButton(
			dosya,
			text="Farklı kaydet",
			fg_color=renk_buton_dark,
			command=update_current_file_save_as
			)
		farkli_ac.pack(pady=5)

		ac = ctk.CTkButton(
			dosya,
			text="Aç",
			fg_color=renk_buton_dark,
			command=update_current_file_open
			)
		ac.pack(pady=5)

		yeni = ctk.CTkButton(
			dosya,
			text="Yeni",
			fg_color=renk_buton_dark,
			command=update_new_file
			)
		yeni.pack(pady=5)

		dosya_buton.configure(command=geri)

		V = ctk.CTkLabel(
			dosya,
			text=f"sürüm: {version[0]}\n{version[1]}",
			font=("Arial",14),
			text_color="white"
			).pack(pady=60)

	dosya_buton = ctk.CTkButton(
		window,
		text="Dosya",
		width=2,
		fg_color=renk_buton_dark,
		command=dosya_icerik
		)
	dosya_buton.place(x=3,y=3)

	def gorunum_icerik():
		global font_boyut_1122
		font_boyut_1122 = "20"
		def geri():
			gorunum_buton.configure(fg_color=renk_buton_dark)
			gorunum.place_forget()
			try:
				dosya.place_forget()
			except:
				pass
			gorunum_buton.configure(command=gorunum_icerik)
			dosya_buton.configure(command=dosya_icerik)

		try:
			dosya.place_forget()
		except:
			pass

		global gorunum

		dosya_buton.configure(fg_color=renk_buton_dark)
		gorunum_buton.configure(fg_color=renk_buton_secili_dark)

		gorunum = ctk.CTkScrollableFrame(
			window,
			height=20,
			width=160,
			fg_color=renk_secenek_dark
			)
		gorunum.place(x=40,y=42)

		def renklendir(chuice):
			if chuice == "Beyaz":
				pad.configure(text_color="white")
				system_save(name="yaziRenk",durum4=1)
			elif chuice == "Kırmızı":
				pad.configure(text_color="red")
				system_save(name="yaziRenk",durum4=2)
			elif chuice == "Siyah":
				pad.configure(text_color="#1D1E1E")
				system_save(name="yaziRenk",durum4=3)
			elif chuice == "Mavi":
				pad.configure(text_color="blue")
				system_save(name="yaziRenk",durum4=4)
			
		font_renk = ctk.CTkComboBox(
			gorunum,
			values=["Beyaz","Kırmızı","Siyah","Mavi"],
			command=renklendir
			)
		try:
			if system_save_yaziRenk() == "1":
				font_renk.set("Yazı rengi:Beyaz")
			elif system_save_yaziRenk() == "2":
				font_renk.set("Yazı rengi:Kırmızı")
			elif system_save_yaziRenk() == "3":
				font_renk.set("Yazı rengi:Siyah")
			elif system_save_yaziRenk() == "4":
				font_renk.set("Yazı rengi:Mavi")
		except:
			font_renk.set("Yazı rengi seçin")

		font_renk.pack(pady=5)

		def temalandir(chuice):
			try:
				if chuice == "Koyu tema":
					ctk.set_appearance_mode("dark")
					system_save(durum=False,name="tema")
					pad.configure(text_color="white")
					system_save(name="yaziRenk",durum4=1)
					print(system_save_tema())
				elif chuice == "Açık tema":
					ctk.set_appearance_mode("light")
					system_save(durum=True,name="tema")
					pad.configure(text_color="#1D1E1E")
					system_save(name="yaziRenk",durum4=3)
					print(system_save_tema())
			except:
				ctk.set_appearance_mode("dark")
		Koyu_tema = ctk.CTkComboBox(
			gorunum,
			values=["Açık tema","Koyu tema"],
			command=temalandir
			)
		try:
			if system_save_tema() == "0":
				Koyu_tema.set("koyu tema")
			elif system_save_tema() == "1":
				Koyu_tema.set("Açık tema")
		except:
			Koyu_tema.set("Tema seç")
		Koyu_tema.pack(pady=20)

		def window_renklendir(chuice):
			if chuice == "Varsayılan":
				window.configure(fg_color=renk_window_dark)
				title.configure(text_color="white")
				system_save(durum2=1,name="windowColor")
			elif chuice == "Mavi":
				window.configure(fg_color="#0033FF")
				title.configure(text_color="white")
				system_save(durum2=2,name="windowColor")
			elif chuice == "Yeşil":
				window.configure(fg_color="#008000")
				title.configure(text_color="white")
				system_save(durum2=3,name="windowColor")
			elif chuice == "Beyaz":
				window.configure(fg_color="white")
				title.configure(text_color="black")
				system_save(durum2=4,name="windowColor")
			elif chuice == "Gri":
				window.configure(fg_color="#696969")
				title.configure(text_color="black")
				system_save(durum2=5,name="windowColor")
			elif chuice == "Siyah":
				window.configure(fg_color="#000500")
				title.configure(text_color="white")
				system_save(durum2=6,name="windowColor")
			elif chuice == "Pembe":
				window.configure(fg_color="#FF00CC")
				title.configure(text_color="white")
				system_save(durum2=7,name="windowColor")

		window_color = ctk.CTkComboBox(
			gorunum,
			values=["Varsayılan","Mavi","Yeşil","Beyaz","Gri","Siyah","Pembe"],
			command=window_renklendir
			)
		try:
			if system_save_windowColor() == "1":
				window_color.set("Renk:Varsayılan")
			elif system_save_windowColor() == "2":
				window_color.set("Renk:Mavi")
			elif system_save_windowColor() == "3":
				window_color.set("Renk:Yeşil")
			elif system_save_windowColor() == "4":
				window_color.set("Renk:Beyaz")
			elif system_save_windowColor() == "5":
				window_color.set("Renk:Gri")
			elif system_save_windowColor() == "6":
				window_color.set("Renk:Siyah")
			elif system_save_windowColor() == "7":
				window_color.set("Renk:Pembe")
		except:
			window_color.set("Pencere rengi")
		window_color.pack(pady=5)

		gorunum_buton.configure(command=geri)

	gorunum_buton = ctk.CTkButton(
		window,
		text="Görünüm",
		width=2,
		fg_color=renk_buton_dark,
		command=gorunum_icerik
		)
	gorunum_buton.place(x=63,y=3)

	kayit_buton = ctk.CTkButton(
		window,
		text="Kaydet",
		width=2,
		fg_color=renk_buton_dark,
		command=update_current_file_save
		)
	kayit_buton.place(x=3,y=55)

	def genislet():
			def geni_geri():
				title.configure(text="\nMicropad\n")
				kayit_buton.place(x=3,y=55)
				yeni_buton.place(x=73,y=55)
				font_boyut.place(x=160,y=55)
				genislet_buton.configure(fg_color=renk_buton_dark,command=genislet)
				system_save(name="genismi",durum3=False)
				print(system_save_genismi())

			title.configure(text="Micropad")
			genislet_buton.configure(fg_color=renk_buton_secili_dark,command=geni_geri)
			kayit_buton.place_forget()
			yeni_buton.place_forget()
			font_boyut.place_forget()
			system_save(name="genismi",durum3=True)
			print(system_save_genismi())

	genislet_buton = ctk.CTkButton(
		window,
		text="Genişlet",
		width=1,
		fg_color=renk_buton_dark,
		command=genislet
		)
	genislet_buton.place(x=180,y=3)

	yeni_buton = ctk.CTkButton(
		window,
		text="Yeni",
		width=1,
		fg_color=renk_buton_dark,
		command=update_new_file
		)
	yeni_buton.place(x=73,y=55)

	def boyutlama(chuice):
		if chuice == "10":
			pad.configure(font=("italic",10))
			font_boyut_1122 = "10"

		elif chuice == "20":
			pad.configure(font=("italic",20))
			font_boyut_1122 = "30"

		elif chuice == "30":
			pad.configure(font=("italic",30))
			font_boyut_1122 = "30"

		elif chuice == "40":
			pad.configure(font=("italic",40))
			font_boyut_1122 = "10"

		elif chuice == "50":
			pad.configure(font=("italic",50))
			font_boyut_1122 = "10"

		elif chuice == "60":
			pad.configure(font=("italic",60))
			font_boyut_1122 = "10"

		elif chuice == "70":
			pad.configure(font=("italic",70))
			font_boyut_1122 = "10"

	font_boyut = ctk.CTkComboBox(
		window,
		values=["10","20","30","40","50","60","70"],
		command=boyutlama
		)
	font_boyut.set(f"Yazı boyutu")
	font_boyut.place(x=160,y=55)


	def geni_geri01():
		title.configure(text="\nMicropad\n")
		kayit_buton.place(x=3,y=55)
		yeni_buton.place(x=73,y=55)
		font_boyut.place(x=160,y=55)
		genislet_buton.configure(fg_color=renk_buton_dark,command=genislet)
		system_save(name="genismi",durum3=False)
		print(system_save_genismi())

	try:
		if system_save_genismi() == "1":
			title.configure(text="Micropad")
			yeni_buton.place_forget()
			kayit_buton.place_forget()
			font_boyut.place_forget()
			genislet_buton.configure(command=geni_geri01,fg_color=renk_buton_secili_dark)

		elif system_save_genismi() == "0":
			title.configure("\nMicropad\n")
			yeni_buton.place(x=73,y=55)
			kayit_buton.place(x=3,y=55)
			font_boyut.place(x=160,y=55)
			genislet_buton.configure(command=genislet)
	except:
		pass

	window.mainloop()

if __name__ == "__main__":
	program()
