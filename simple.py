import os, re, requests, json, random, sys, time
from random import choice as pilih
from rich.panel import Panel as s
from rich import print as banner

##WARNA##
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

##WARNA RICH##
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

##RANDOM WARNA##
pilihan = ['\x1b[1;96m','\x1b[1;95m','\x1b[1;94m','\x1b[1;93m','\x1b[1;92m','\x1b[1;91m','\x1b[38;5;208m','\x1b[0;96m','\x1b[0;95m','\x1b[38;5;44m','\x1b[38;5;196m','\x1b[38;5;46m','\x1b[38;5;226m']
warna=pilih(pilihan)

###RANDOM WARNA PANEL###
daftar_warna=['#AF00FF','#00C8FF','#FFFF00','#00FF00','#FF0000','#FF8F00','#FF00FF','#AF00FF']
warna_panel=pilih(daftar_warna)
warna_banner=pilih(daftar_warna)
#####MULAI SCRIPT!###
ses=requests.Session()
os.system('clear')

def write_text(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)

###LOGO SCRIPT##
def bannersc():
   banner(s(f"""                    [{warna_banner}]d8b                
                    [{warna_banner}]?88 
                     [{warna_banner}]88b                {A2}█{M2}████████
[{warna_panel}]  88bd88b?88   d8P   [{warna_banner}]888888b   88bd88b  {A2}█{M2}████████
[{warna_panel}]  88P'  `d88   88    [{warna_banner}]88P `?8b  88P' ?8b {A2}█{P2}████████
[{warna_panel}] d88     ?8(  d88   [{warna_banner}]d88   88P d88   88P {A2}█{P2}████████
[{warna_panel}]d88'     `?88P'?8b [{warna_banner}]d88'   88bd88'   88b {A2}█
                [{warna_panel}])88                     {A2}█
               [{warna_panel}],d8P                     {A2}█
            [{warna_panel}]`?888P'
""",width=54,style=f'{warna_panel}'))
   write_text(f'{warna}╭─────────────────╮ ╭───────────╮╭─────────────────╮\n│ {P}Facebook Author {warna}│{P}:{warna}│ {P}Rayhan 27 {warna}││ {P}Rayhan Business {warna}│\n╰{P}╭─{warna}───────────────╯ ╰───────────╯╰─────────────────╯\n {P}│{warna}  ╭──────────────────────╮╭───────────────────────╮\n {P}╰─>{warna}│ {P}fb.com/Rayhan.27.Xyz {warna}││ {P}fb.com/RayhanBusiness {warna}│\n    ╰──────────────────────╯╰───────────────────────╯')

bannersc()

####LOGIN SCRIPT####
def login():
	banner(s(f" {P2}Masukan Cookie Untuk Login",subtitle=f'{P2}╭─',subtitle_align='left',width=30,padding=0,style=f'{warna_panel}'))
	cookie = input(f"{P}   ╰──> : {H}")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		os.system('clear');bannersc();banner(s(f'{H2}Login Berhasil Cookie Valid',width=31,style=f'{warna_panel}'));menu()
	except:
		banner(s(f"{M2}Maaf Login Gagal Cek Kembali Cookie Anda",width=44,style=f'{warna_panel}'));time.sleep(4);os.system('python simple.py')
		

###MASUK DALAM SCRIPT###
def menu():
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}
		nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
	except:
		login()
	banner(s(f'{P2}Masukkan [{warna_banner}]Link Postingan {P2}Anda, Pastikan Postingan Anda Bersifat Publik, Ketik [{warna_panel}]Def{P2}/[{warna_panel}]Default {P2}Untuk Share Link Bawaan, Atau Ketik {M2}Out {P2}Untuk {M2}Hapus Cookie {P2}Dan {H2}Ganti Akun',subtitle=f'{P2}╭─[ Selamat Datang [{warna_banner}]{nama}{P2}! ]',subtitle_align='left',width=70,padding=1,style=f'{warna_panel}'))
	linkpost = input(f"{P}   ╰──> : {H}")
	if linkpost == 'def' or linkpost == 'Def' or linkpost == 'DEF' or linkpost == 'default' or linkpost == 'Default' or linkpost == 'DEFAULT':
	     print(f'{warna}╭───────────────────────╮╭──────────────────────────╮\n│ [{U}1 {P}Profile{warna}] {P}Rayhan 27 {warna}││ [{U}2 {P}Post{warna}] {P}Rayhan Business {warna}│\n╰──{P}╭─ {warna}──────────────────╯╰──────────────────────────╯')
	     pilihzz = input(f"{P}   ╰──> : {H}")
	     if pilihzz == '1' or pilihzz == '01':
	        os.system('clear')
	        bannersc()
	        banner(s(f'https://www.facebook.com/photo.php?fbid=4390440514384239&set=a.106722446089422&type=3&app=fbl',subtitle=f'{P2}╭─[ Menjalankan ♾️  {P2}Share ]',subtitle_align='left',width=70,padding=1,style=f'{warna_banner}'));print('   │')
	        try:
		        n = 0
		        header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
		        for x in range(99999999):
			        n+=1
			        post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link=https://www.facebook.com/photo.php?fbid=4390440514384239&set=a.106722446089422&type=3&app=fbl&published=0&access_token={token}",headers=header, cookies=cookie).text
			        data = json.loads(post)
			        if "id" in post:
				        print(f'{P}\r   ╰──────> {P}{n}. {warna}{data["id"]}',end='');sys.stdout.flush()
			        else:
				        print("\n")
				        banner(s(f'{P2}Auto Share Berhenti, Cek Link Atau Cookie',width=34,padding=0,style='red'));exit()
		        print('');banner(s(f'{P2}Auto Share Sudah Mencapai Target',width=36,style=f"{warna_panel}"))
	        except requests.exceptions.ConnectionError:
		        print('');banner(s(f'{P2} Periksa Koneksi Internet Anda!',width=34,padding=0,style='red'));exit()
	     if pilihzz == '2' or pilihzz == '02':
	        os.system('clear')
	        bannersc()
	        banner(s(f'https://www.facebook.com/100000541003355/posts/5340593442635303/?app=fbl',subtitle=f'{P2}╭─[ Menjalankan ♾️  {P2}Share ]',subtitle_align='left',width=70,padding=1,style=f'{warna_banner}'));print('   │')
	        try:
		        n = 0
		        header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
		        for x in range(99999999):
			        n+=1
			        post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link=https://www.facebook.com/100000541003355/posts/5340593442635303/?app=fbl&published=0&access_token={token}",headers=header, cookies=cookie).text
			        data = json.loads(post)
			        if "id" in post:
				        print(f'{P}\r   ╰──────> {P}{n}. {warna}{data["id"]}',end='');sys.stdout.flush()
			        else:
				        print("\n")
				        banner(s(f'{P2}Auto Share Berhenti, Cek Link Atau Cookie',width=34,padding=0,style='red'));exit()
		        print('');banner(s(f'{P2}Auto Share Sudah Mencapai Target',width=36,style=f"{warna_panel}"))
	        except requests.exceptions.ConnectionError:
		        print('');banner(s(f'{P2} Periksa Koneksi Internet Anda!',width=34,padding=0,style='red'));exit()
	if linkpost == 'out' or linkpost == 'Out' or linkpost == 'OUT':
	     os.system('rm cookie.txt token.txt');banner(s(f'{P2}Berhasil Menghapus Cookie, Enter Untuk Keluar',width=49,style=f"{warna_panel}"))
	     out=input('')
	     if out == 'out':
	         exit()
	     else:
	         exit()
	banner(s(f'{P2} Masukkan Limit Share',subtitle=f'{P2}╭─',subtitle_align='left',width=24,padding=0,style=f'{warna_panel}'))
	limit = int(input(f"{P}   ╰──> : {H}"))
	os.system('clear')
	bannersc()
	banner(s(f'{linkpost}',subtitle=f'{P2}╭─[ Menjalankan [{warna_banner}]{limit} {P2}Share ]',subtitle_align='left',width=70,padding=1,style=f'{warna_banner}'));print('   │')
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
		for x in range(limit):
			n+=1
			dontdelete=ses.post(f"https://graph.facebook.com/v13.0/me/feed?link=https://www.facebook.com/photo.php?fbid=4390440514384239&set=a.106722446089422&type=3&app=fbl&published=0&access_token={token}",headers=header, cookies=cookie).text
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={linkpost}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				print(f'{P}\r   ╰──────> {P}{n}. {warna}{data["id"]}',end='');sys.stdout.flush()
			else:
				print("\n")
				banner(s(f'{P2}Auto Share Berhenti, Cek Link Atau Cookie',width=34,padding=0,style='red'));exit()
		print('');banner(s(f'{P2}Auto Share Sudah Mencapai Target',width=36,style=f"{warna_panel}"))
	except requests.exceptions.ConnectionError:
		print('');banner(s(f'{P2} Periksa Koneksi Internet Anda!',width=34,padding=0,style='red'));exit()
		
menu()
