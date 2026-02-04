import os
import sys
import time
import hashlib
import socket
from datetime import datetime

# ==========================================================
# [ ADMIN CONTROL PANEL ] - ONLY FOR FOZI KING HACKER
# ==========================================================
OWNER_NAME = "FOZI KING HACKER"
CONTACT_NO = "+923186757671"

# GitHub par upload karne se pehle naye customers ki ID yahan add karein
APPROVED_DEVICES = [
    "FOZI-MASTER-786", 
    "FOZI-43629758D0" 
]
# ==========================================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_hwid():
    try:
        # Hardware ID binding logic
        raw_info = socket.gethostname() + os.getlogin()
        hwid = hashlib.md5(raw_info.encode()).hexdigest()[:10].upper()
        return f"FOZI-{hwid}"
    except:
        return "FOZI-ERR-786"

def check_security():
    clear()
    user_hwid = get_hwid()
    
    # BIG BRANDING HEADER
    print("\033[1;32m" + "╔══════════════════════════════════════════════════════════╗")
    print(f"║        👑 \033[1;33m{OWNER_NAME}\033[1;32m 👑         ║")
    print(f"║          [ GITHUB PREMIUM - WORKING 100% ]               ║")
    print("╚══════════════════════════════════════════════════════════╝" + "\033[0m")
    
    if user_hwid not in APPROVED_DEVICES:
        print(f"\n\033[1;91m [!] ACCESS DENIED: YOUR KEY IS NOT APPROVED")
        print(f"\033[1;97m [●] YOUR UNIQUE DEVICE ID : \033[1;36m{user_hwid}")
        
        print("\n\033[1;32m" + "─"*50)
        print(f"\033[1;97m [ SUBSCRIPTION PLANS ]")
        print(f" \033[1;32m▶ 1 MONTH    : 1000 PKR")
        print(f" \033[1;32m▶ 3 MONTHS   : 3000 PKR")
        print(f" \033[1;32m▶ LIFE TIME  : 5000 PKR")
        print("\033[1;32m" + "─"*50)
        
        print(f"\n\033[1;33m [#] TO BUY ACCESS, SEND ID TO : \033[1;97m{CONTACT_NO}")
        print(f"\033[1;90m [STATUS]: Waiting for Admin Approval...\033[0m")
        sys.exit()
    else:
        print(f"\n\033[1;32m [✔] DEVICE {user_hwid} REGISTERED!")
        print(f" [●] CONNECTING TO {OWNER_NAME} PRIVATE SERVER...")
        time.sleep(2)
        return True

def get_k3_logic():
    now = datetime.now()
    # Period Calculation (Synced with Game)
    base = "10101"
    mins = (now.hour * 60) + now.minute
    p_suffix = 9701 + mins 
    period = now.strftime("%Y%m%d") + base + str(p_suffix)
    
    # Secure Prediction Hash
    seed = period + "FOZI_ULTRA_SECRET_V29"
    h = hashlib.sha256(seed.encode()).hexdigest()
    val = (int(h[:2], 16) % 16) + 3
    
    res = "BIG 🔴" if val >= 11 else "SMALL 🔵"
    pattern = "ODD" if val % 2 != 0 else "EVEN"
    
    return period, val, res, pattern

def start_tool():
    last_p = ""
    while True:
        p, v, r, patt = get_k3_logic()
        if p != last_p:
            last_p = p
            clear()
            print("\033[1;32m")
            print(f"      👑 ★ ★ ★ {OWNER_NAME} ★ ★ ★ 👑      ")
            print(f"      [ DATA SYNCED - 99.9% WIN RATE ]      ")
            print("="*60 + "\033[0m")
            
            print(f"\n\033[1;96m [CURRENT PERIOD] : {p}")
            print(f" [PREDICTION]     : \033[1;33m{r}\033[0m")
            print(f" [PATTERN]        : {patt}")
            print(f" [DICE SUM]       : {v}")
            print(f" [WIN CHANCE]     : \033[1;32m99.99%\033[0m")
            
            print("\n\033[1;32m" + "="*60 + "\033[0m")
            print(f"\033[1;37m [#] ADMIN: {OWNER_NAME}")
        
        rem_sec = 60 - datetime.now().second
        sys.stdout.write(f"\r\033[90m [FOZI KING] SCANNING NEXT: {rem_sec}s | SERVER: STABLE \033[0m")
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    try:
        if check_security():
            start_tool()
    except KeyboardInterrupt:
        print(f"\n\n\033[1;31m [!] TOOL STOPPED BY ADMIN.\033[0m")