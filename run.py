import sys, os, subprocess, platform, struct

if struct.calcsize("P")*8==64:
  Rayhan = "rayshre.py"

null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:
  os.system('pkg install play-audio -y &> /dev/null')

while True :
  try :
    import pwinput, requests, bs4, beautifultable, termcolor
  except ImportError as e:
    os.system('python -m pip install '+e.name)
  else:
    break

os.system(f'chmod 777 python {Rayhan}')
