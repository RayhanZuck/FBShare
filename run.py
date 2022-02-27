import sys, os, subprocess, platform, struct

while True :
  try :
    import pwinput, requests, bs4, beautifultable, termcolor
  except ImportError as e:
    os.system('python -m pip install '+e.name)
  else:
    break
os.system('git pull')
os.system('python rayshre.so')
