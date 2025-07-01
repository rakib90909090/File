
import os
import re
import sys
import time
import json
import string
import requests


R = "\x1b[38;5;196m"
G = "\x1b[38;5;46m"
W = "\x1b[97m"
P = "\x1b[38;5;203m"



#_______________| color list 3 |_______________#
 
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'


#_____________[ tool version]_____________#
try:
    version = requests.get("https://raw.githubusercontent.com/Napaextra007/Napaextra/refs/heads/main/Version.txt").text
except:
    print('No Internet Connection');exit()
version = version.strip()
session = requests.Session()
logo=f"""
{G1}    __ __ _____   ________
{G2}   / //_//  _/ | / / ____/
{G3}  / ,<   / //  |/ / / __  
{G4} / /| |_/ // /|  / /_/ /  
{G5}/_/ |_/___/_/ |_/\____/  卝{R}𝐑{G1}𝐀{X}𝐅{M}𝐈 ツ
{M}════════════════════════════════════════════════
{R}[{G1}𓇬{R}]{S} 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 {R}〆{S} 𝐊𝐈𝐍𝐆 𝐑𝐀𝐅𝐈
{R}[{G1}𓇬{R}]{S} 𝐓𝐎𝐎𝐋𝐒 𝐅𝐎𝐑 {R}〆 \x1b[38;5;196m\033[47m𝐅𝐈𝐋𝐄 \x1b[0m{Y}┼︎\x1b[38;5;196m\033[47m𝐂𝐑𝐄𝐀𝐓𝐄 \x1b[0m
{R}[{G1}𓇬{R}]{S} 𝐕𝐄𝐑𝐒𝐈𝐎𝐍   {R}〆{G1} 𝐕{R}/{S}{version}
{R}[{G1}𓇬{R}]{S} 𝐒𝐓𝐀𝐓𝐔𝐒    {R}〆{Y} 𝐏𝐑𝐄𝐌𝐈𝐔𝐌
{M}════════════════════════════════════════════════"""

class Main:
    def __init__(self):
        self.uid = []
        self.token = []
        self.user = []

    def clear(self):
        os.system('clear')
        print(logo)

    def linex(self):
        print(f"{W}------------------------------------")

    def login(self):
        self.clear()
        try:
            print(f"USE 1 MONTH OLD IDS COOKIE")
            cookie = input(f"COOKIE :{G} ")
            self.linex()
            open("/sdcard/.cokx.txt","w").write(cookie)
            with requests.Session() as aiman:
                aiman.headers.update({'Accept-Language': 'id,en;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                'Referer': 'https://www.instagram.com/',
                'Host': 'www.facebook.com',
                'Sec-Fetch-Mode': 'cors',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Dest': 'empty',
                'Origin': 'https://www.instagram.com',
                'Accept-Encoding': 'gzip, deflate'})
                response = aiman.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    open("/sdcard/.tokx.txt","w").write(token)
                    print(f"TOKEN  :{G} {token}")
                    self.linex()
                    print("LOGGED IN SUCCESSFULLY")
                else:
                    print("COOKIE ERROR BRO..!")
            self.login_check()
        except Exception as e:
            print(e)
    
    def login_check(self):
        try:
            coki = open("/sdcard/.cokx.txt","r").read()
            token = open("/sdcard/.tokx.txt","r").read()
            self.token.append(token)
            try:
                response = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+self.token[0], cookies={'cookie':coki})
                datas = json.loads(response.text)
                name = datas['name']
                ids = datas['id']
                self.Menu(name,ids)
            except requests.exceptions.ConnectionError:
                sys.exit("NETWORK CONNECTION PROBLEM...")
        except IOError:
            self.login()
    
    def Menu(self,name,ids):
        self.clear()
        print(f"{W}USERNAME  : {G}{name}")
        print(f"{W}USER UID  : {G}{ids}")
        self.linex()
        print("[1] START SIMPLE FILE DUMPING")
        print("[2] START UNLIMITED FILE DUMPING")
        print("[3] EXIT PROGRAM </>")
        self.linex()
        xxxx = input(f"{W}CHOOSE AN OPTION : ")
        if xxxx == "1":self.simple_file()
        elif xxxx == "2":self.unlimited_file()
        elif xxxx == "3":sys.exit()
        else:sys.exit("Wrong...")
    
    def simple_file(self):
        self.clear()
        try:
            coki = open("/sdcard/.cokx.txt","r").read()
            token = open("/sdcard/.tokx.txt","r").read()
        except IOError:
            print("COOKIE TOKEN NOT FOUND.LOGIN AGAIN...")
            self.login()
        print("ENTER FILE NAME : /sdcard/Sajib.txt")
        file_name = input("PUT FILE NAME : ")
        self.linex()
        print("PASTE ALL IDS HERE..")
        self.linex()
        while True:
            ids_all = input("")
            if ids_all == "":
                break
            try:
                uid = ids_all.split("|")[0]
            except:
                uid = ids_all
            self.user.append(uid)
            for user in self.user:
                try:
                    head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
                    if len(self.uid) == 0:
                        params = ({'access_token': token,'fields': "friends"})
                    else:
                        params = ({'access_token': token,'fields': "friends"})
                    response = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':coki}).json()
                    for sazib in response['friends']['data']:
                        try:
                            self.uid.append(sazib['id'])
                            open(file_name,"a").write(sazib['id']+"|"+sazib['name']+"\n")
                            tani = str(sazib['id'])
                            total = len(self.uid)
                            print(f"SUCCESSFULLY DUMP FROM : {tani}|{total}")
                        except:continue
                except requests.exceptions.ConnectionError:
                    pass
            sys.exit(self.linex())
    def unlimited_file(self):
        self.clear()
        try:
            coki = open("/sdcard/.cokx.txt","r").read()
            token = open("/sdcard/.tokx.txt","r").read()
        except IOError:
            print("COOKIE TOKEN NOT FOUND.LOGIN AGAIN...")
            self.login()
        print("ENTER FILE NAME : /sdcard/Sajib.txt")
        file_name = input("PUT FILE NAME : ")
        self.linex()
        tls = int(input("HOW MANY IDS DO YOU WANT TO ADD? : "))
        for a in range(tls):
            self.user.append(input(f"No.{a+1} Put Ids - "))
        self.linex()
        for user in self.user:
            try:
                head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
                if len(self.uid) == 0:
                    params = ({'access_token': token,'fields': "friends"})
                else:
                    params = ({'access_token': token,'fields': "friends"})
                response = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':coki}).json()
                for sazib in response['friends']['data']:
                    try:
                        self.uid.append(sazib['id'])
                        open(".temp.txt","a").write(sazib['id']+"\n")
                        total = len(self.uid)
                    except:continue
                print(f"XTRACT SUCCESSFUL : {user}|{total}")
            except requests.exceptions.ConnectionError:
                pass
        self.clear()
        try:filexx = open(".temp.txt","r").read().splitlines()
        except:filexx = []
        print(f"TOTAL IDS FROM DUMP : {total}")
        print(f"THE PROCESS HAS BEEN STARTED...")
        self.linex()
        for user in filexx:
            try:
                head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
                if len(self.uid) == 0:
                    params = ({'access_token': token,'fields': "friends"})
                else:
                    params = ({'access_token': token,'fields': "friends"})
                response = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':coki}).json()
                for sazib in response['friends']['data']:
                    try:
                        self.uid.append(sazib['id'])
                        open(file_name,"a").write(sazib['id']+"|"+sazib['name']+"\n")
                        total = len(self.uid)
                        sys.stdout.write(f"\r\r{W}SUCCESSFUL DUMP FROM -> {user}|{G}{total}")
                        sys.stdout.flush()
                    except:continue
            except KeyError:pass
            except requests.exceptions.ConnectionError:
                pass
        sys.exit(self.linex())

if __name__ == "__main__":
    os.system("rm .temp.txt")
    Main().login_check()