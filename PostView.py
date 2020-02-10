import json,re,sys,os
import argparse
from time import sleep
try:
   import colorama
   from colorama import Fore, Back, Style
   colorama.init(autoreset=True)
   hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
   res = Style.RESET_ALL
   abu2 = Style.DIM+Fore.WHITE
   ungu2 = Style.NORMAL+Fore.MAGENTA
   ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
   hijau2 = Style.NORMAL+Fore.GREEN
   yellow2 = Style.NORMAL+Fore.YELLOW
   yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
   red2 = Style.NORMAL+Fore.RED
   red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
except:
   print ("Hmm Sepertinya Modul Colorama Belum Terinstall\n\n\n")
   sys.exit()

try:
   import requests
   from bs4 import BeautifulSoup
except:
   print ("Hmm Sepertinya Modul Requests Dan BS4 Belum Terinstall\n\n\n")
   sys.exit()

from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError


parser = argparse.ArgumentParser(description='Script AllTeleBot Premium.\nScript Ini Di Gunakan Untuk Mengotmasi Alexacrypto')
parser.add_argument(
    '-p','--phone',
    help='Enter Your Phone Number.\nExemple +6285*********',required=True
)

argument = parser.parse_args()
banner = Style.NORMAL+Fore.MAGENTA+"""       __       _       __
      / /__    (_)___ _/ /______ _
 __  / / _ \  / / __ `/ //_/ __ `/
/ /_/ /  __/ / / /_/ / ,< / /_/ /
\____/\___/_/ /\__,_/_/|_|\__,_/
         /___/                   """+Style.DIM+Fore.WHITE+"""PostView
"""+Style.NORMAL+Fore.GREEN+"""=========================================================
"""+Style.BRIGHT+Fore.GREEN+"""Author By  """+Style.DIM+Fore.WHITE+""" :"""+Style.RESET_ALL+""" Kadal15
"""+Style.BRIGHT+Fore.GREEN+"""Channel Yt"""+Style.DIM+Fore.WHITE+"""  : """+Style.RESET_ALL+"""Jejaka Tutorial"""

if not os.path.exists("session"):
    os.makedirs("session")

c = requests.Session()

if not os.path.exists(".password"):
    os.makedirs(".password")

print("\033[1;32mSilahkan Ambil Password Pada Link Di Bawah Ini\033[1;0m\nhttp://jejakainc.com/Password/")
pw = c.get("http://jejakainc.com/Password/Passw.txt")
if not os.path.exists(".password/password.txt"):
    f = open(".password/password.txt", "w+")
    f.write("wkwkwkwkw")
    f.close()

for i in range(99):
    f = open(".password/password.txt", "r")
    if f.readlines()[0] == pw.text:
        sys.stdout.write('\r                                                \r')
        sys.stdout.write('\rUsing Exiting Password....!')
        break
    pwin = input("\033[1;32mEnter Password \033[1;30m:\033[1;0m ")
    if pwin == pw.text:
        f = open(".password/password.txt", "w+")
        f.write(pwin)
        f.close()
        break
    else:
        print("\033[1;31mPassword Salah...!")
        if i > 1:
            print("\033[1;33mSilahkan Check Password Pada Link Di Bawah Ini\n\033[1;0mhttp://jejakainc.com/Password/")
            sys.exit()



def login(nomor):
  global client
  api_id = 717425
  api_hash = '322526d2c3350b1d3530de327cf08c07'
  phone_number = nomor

  client = TelegramClient("session/"+phone_number, api_id, api_hash)
  client.connect()
  if not client.is_user_authorized():
    try:
      client.send_code_request(phone_number)
      me = client.sign_in(phone_number, input('\n\n\n\033[1;0mEnter Yout Code : '))
    except SessionPasswordNeededError:
      passw = input("\033[1;0mYour 2fa Password : ")
      me = client.start(phone_number,passw)
  myself = client.get_me()
  os.system("clear")
  print (banner)
  print (f"{hijau}Telegram Number{res}",nomor)
  print (f"{hijau}Welcome To AlexaCryptoBot{res}",myself.first_name,f"\n{hijau}Bot Ini Di Gunakan Untuk Menuyul Bot AlexaCrypto Di Telegram\n\n")

def tunggu(x):
      sys.stdout.write("\r")
      sys.stdout.write("                                                               ")
      for remaining in range(x, 0, -1):
          sys.stdout.write("\r")
          sys.stdout.write("{}[{}|{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
          sys.stdout.flush()
          sleep(0.125)
          sys.stdout.write("\r")
          sys.stdout.write("{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
          sys.stdout.flush()
          sleep(0.125)
          sys.stdout.write("\r")
          sys.stdout.write("{}[{}-{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
          sys.stdout.flush()
          sleep(0.125)
          sys.stdout.write("\r")
          sys.stdout.write("{}[{}\{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
          sys.stdout.flush()
          sleep(0.125)
          sys.stdout.write("\r")
          sys.stdout.write("{}[{}|{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
          sys.stdout.flush()
          sleep(0.125)
          sys.stdout.write("\r")
          sys.stdout.write("{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
          sys.stdout.flush()
          sleep(0.125)
          sys.stdout.write("\r")
          sys.stdout.write("{}[{}-{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
          sys.stdout.flush()
          sleep(0.125)
          sys.stdout.write("\r")
          sys.stdout.write("{}[{}\{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
          sys.stdout.flush()
          sleep(0.125)
      sys.stdout.write("\r                                                 \r")
      sys.stdout.write(f"\r{abu2}[{yellow2}!{abu2}] {yellow}Getting Reward")


login(argument.phone)
channel_entity = client.get_entity("@AlexCryptoDOGEbot")
channel_username = "@AlexCryptoDOGEbot"
for i in range(5000000):
    client.send_message(entity=channel_entity, message="Back 🔙")
    client.send_message(entity=channel_entity, message="📄")
    sleep(3)
    posts = client(
        GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0,
                          hash=0))
    if posts.messages[0].message.find("No Post Promotions found for you right now.. Why don't you create one?") != -1:
        print(f"\n{abu2}[{red2}x{abu2}] {red}Iklan Sudah Habis Coba Lagi Besok")
        break
    id = posts.messages[1].id
    tunggu(20)
    try:
        client(GetBotCallbackAnswerRequest(
            channel_username,
            id,
            data=posts.messages[1].reply_markup.rows[0].buttons[1].data
        ))
    except KeyboardInterrupt:
        print(f"\n{abu2}[{red2}x{abu2}] {red}Exit")
        sleep(1)
        sys.exit()
    except:
        sleep(3)
        posts = client(
            GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0,
                              add_offset=0,
                              hash=0))
        sys.stdout.write("\r"+posts.messages[0].message+"\n")
