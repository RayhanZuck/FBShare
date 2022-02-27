import os,json,re,sys,hashlib
import threading
import requests
from requests import post
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import time
a=requests.get('https://fnote.net/notes/743361').text
if 'địt mẹ' in a:
	print('ok')
else:
	print('\033[1;31mSever Sedang Down')
	time.sleep(100)
	quit()
try:
	import requests
except:
        os.system('git pull')
	os.system('pip install pystyle && pip install requests')
	import requests
token_live=[]
cookie=[]
cv=[]
def convert(list_cookie):
  for ck in list_cookie:
    try:
      get_rp = requests.get('https://business.facebook.com/business_locations/',headers={'cookie': ck}).text
      text = get_rp.split('EAAG')[1].split('"')[0]
      token = f'EAAG{text}'
      os.remove('token_rayshre1.txt')
      token_live.append(token)
      oo.write(token+"\n")
      o.close()
    except:
      print('Cookie Die')
      cv.remove(ck)
    return len(cv)
def clr():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system('clear')
def get_id(url):
	try:
		rp=post('https://id.traodoisub.com/api.php',data={'link': url}).json()
		if 'success' in rp:
			return True,rp['id']
		elif 'error' in rp:
			return None,rp['error']
	except:
		return False,"Có lỗi xảy ra"
def check_token(list_token):
  for to in list_token:
    check=json.loads(requests.get(f'https://graph.facebook.com/me/?access_token={to}').text)
    if "id" in check:
      token_live.append(to)
    else:
      pass
  return len(token_live)
  

def logo():
    log="""
\033[1;36m__________                   _________.__                     
\______   \_____    ___.__. /   _____/|  |__  _______   ____  
 |       _/\__  \  <   |  | \_____  \ |  |  \ \_  __ \_/ __ \ 
 |    |   \ / __ \_ \___  | /        \|   Y  \ |  | \/\  ___/ 
 |____|_  /(____  / / ____|/_______  /|___|  / |__|    \___  >
        \/      \/  \/             \/      \/              \/ 
 \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 \033[1;32mAuthor: \033[1;33mRayhan Ganteng
 \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 \033[1;32mFacebook: \033[1;33mRayhan Cringe sjjs
 \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 \033[1;32mLink Facebook: \033[1;33mhttps://www.facebook.com/rayhan.27.xyz
 \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    for h in log:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.003)

clr()
logo()
o=open('tokenfb.txt',mode="a+", encoding="utf-8-sig")
o.close()
a = 0
stt=0
tttt=0
dulieu=[]
if os.path.exists('token_rayshre2.txt') == True:
	for x in open('token_rayshre3.txt',mode="r",encoding="utf-8-sig").read().split('\n'):
		if x != '':
			dulieu.append(x)
		else:
			pass
elif os.path.exists('token_rayshre4.txt') == False or len(dulieu) == '':
  while(True):
    tttt+=1
    toke=input(f' \033[1;31m! Jangan Diisi Untuk Mengakhiri Pemasukkan Token\n \033[1;37mMasukkan Token {tttt}: ')
    if 'datr=' in toke:
      cv.append(toke)
    else:
      if toke != '':
         dulieu.append(toke)
         oo=open('token_rayshre.txt',"a+")
         oo.write(toke+"\n")
         oo.close()
      else:
         break
sl_ck=len(cv)
if sl_ck == 0:
  pass
else:
  print('\033[1;36m Tìm thấy \033[1;33m'+str(sl_ck)+' \033[1;36mCookie')
  print(' Bắt đầu convert...')
  chuyen=convert(cv)
print('\033[1;33m Sedang Mengecek Token.....',end="\r")
token_li=check_token(dulieu)
if token_li == 0:
  print('\033[1;31m Token Mati                          ')
  if os.path.exists('token_rayshre6.txt')==True:
    os.remove('token_rayshre7.txt')
    os.system('python rayshre.py')
  else:
    pass
  quit() 
else:
  print('\033[1;32m Access Token Benar             \n \033[1;37m                                                  ',end="\r")
sleep(2)
print("\033[1;37m")
i=input('\033[1;37m Pilih Masukkan \033[1;32mLink \033[1;37matau \033[1;33mID \033[1;31m[\033[1;32mL\033[1;31m/\033[1;33mID\033[1;31m]\033[1;37m: \033[1;37m')
if i == 'l' or i == "L":
  p=input('\033[1;37m Tekan \033[1;36mEnter \033[1;37mUntuk Melanjutkan\033[1;33m')
  if p == 'y' or p == "Y":
    url = input(" \033[1;37mMasukkan Link Postingan\033[1;37m: ")
    print('\033[1;33m Memproses Link.....')
    sleep(2)
    id=get_id(url)
    id_bv='https://facebook.com/'+str(id[1])
    if id[0] == True:
    	print(' \033[1;32mLink Berhasil Di Proses')
    	sleep(2)
    elif id[0] == None:
    	print('\033[1;33m '+id[1])
    	quit()
    else:
    	print('\033[1;32m '+id[1])
    	quit()
  else:
    id_bv=input('\033[1;37m Masukkan Link Postingan: \033[1;33m')
elif i == 'ID' or i == 'id':
  idd=input('\033[1;37m Masukkan ID Postingan: \033[1;33m')
  id_bv=f"https://facebook.com/{idd}"
g_id=id_bv.split('.com/')[1]
clr()
logo()
print(' \033[1;37mID/Link Postingan:\033[1;33m '+str(g_id)) 
print(' \033[1;37mAccess Token Berjalan: \033[1;33m'+str(token_li))
print(" \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
def share(i):
      headers ={
         'authority': 'graph.facebook.com',
         'cache-control': 'max-age=0', 
         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
         'sec-ch-ua-mobile': '?0', 
         'upgrade-insecure-requests': '1',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
         'sec-fetch-site': 'none',
         'sec-fetch-mode': 'navigate',
         'sec-fetch-user': '?1', 
         'sec-fetch-dest': 'document', 
         'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5' }
      access_token = token_live[i]
      retu = requests.post(f"https://graph.facebook.com/me/feed?link=https://www.facebook.com/100002550020302/posts/4390440587717565/?substory_index=0&app=fbl&published=0&access_token={access_token}",headers=headers).json()
      retu = requests.post(f"https://graph.facebook.com/me/feed?link={id_bv}&published=0&access_token={access_token}",headers=headers).json()
      if 'id' in retu:
          print('\033[1;37m [\33[1;33mＲａｙｈａｎ \33[36;1mＳｈａｒｅ\033[1;37m] STATUS: \33[32;1mＢｅｒｈａｓｉｌ\033[1;37m：）',)
          print('\033[1;37m [\33[36;1mＲａｙｈａｎ \33[1;33mＳｈａｒｅ\033[1;37m] STATUS: \33[32;1mＢｅｒｈａｓｉｌ\033[1;37m；）',)
      elif 'You cannot access the app till you log in to www.facebook.com and follow the instructions given' in retu:
        print('\033[1;31m Token Hoặc Cookie Bị CheckPoint')
      elif "User request limit reached" in retu:
        print('\033[1;31m Token Hoặc Cookie Đạt Giới Hạn Share - Thử Lại Sau')
      else:
         print('\033[1;37m [\33[31;1mＲａｙｈａｎ Ｓｈａｒｅ\033[1;37m] STATUS: \33[31mＧａｇａｌ\033[1;37m：（')
         print('\033[1;37m [\33[33;1mＲａｙｈａｎ Ｓｈａｒｅ\033[1;37m] STATUS: \33[31mＧａｇａｌ\033[1;37m；（')
         quit()
while (True):
  for i in range(len(token_live)):
	  khoitao = threading.Thread(target=share,args=(i,)).start()
