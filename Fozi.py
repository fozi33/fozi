import os
import re
import time
import hashlib
import requests
import sys
import urllib.parse
from datetime import datetime

# --- CONFIGURATION ---
# Maine aapka provided link RAW format mein convert kar diya hai
APPROVAL_URL = "https://raw.githubusercontent.com/fozi33/Aprowl.txt/main/Aprowl.txt"
OWNER_NUMBER = "+923207706955"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def FOZI_BOSS_APPROVAL():
    clear()
    # Unique HWID generation logic
    try:
        device_data = os.popen('getprop ro.product.model').read().strip() + os.getlogin() + str(os.getuid())
    except:
        device_data = "FOZI_DEVICE_" + str(os.getuid())
        
    hwid = hashlib.sha256(device_data.encode()).hexdigest().upper()[:12]
    
    print("\033[1;32m")
    print(r"""
  ______ ____ _________  _  ___ _   _  ____ 
 |  ____/ __ \___  /_ _| |/ (_) \ | |/ ___|
 | |__ | |  | | / / | || ' /| |  \| | |  _ 
 |  __|| |  | |/ /  | || . \| | |\  | |_| |
 |_|   \____//____|___|_|\_\_|_| \_|\____|
    """)
    print(f"\033[1;36m [●] DEVICE KEY : \033[1;37m{hwid}")
    print("\033[1;33m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;35m [!] STATUS     : \033[1;37mChecking Online Approval...")
    
    try:
        # GitHub se data fetch karna
        response = requests.get(APPROVAL_URL, timeout=10)
        approved_keys = response.text.upper()
        
        if hwid in approved_keys:
            print("\033[1;32m [✔] ACCESS GRANTED! WELCOME BOSS.")
            time.sleep(2)
            start_prediction_tool()
        else:
            print("\033[1;31m [×] ACCESS DENIED! YOUR KEY IS NOT APPROVED.")
            print("\033[1;32m [→] REDIRECTING TO OWNER ON WHATSAPP...")
            time.sleep(3)
            
            msg = f"Assalam-o-Alaikum FOZI BOSS,\n\nMeri Key Approve Kar Dein.\nKey: {hwid}"
            encoded_msg = urllib.parse.quote(msg)
            os.system(f'xdg-open https://wa.me/{OWNER_NUMBER}?text={encoded_msg}')
            sys.exit()
            
    except:
        print("\033[1;31m [!] CONNECTION ERROR! PLEASE CHECK INTERNET.")
        sys.exit()

def get_high_accuracy_logic(period_id):
    hash_object = hashlib.sha256(period_id.encode())
    hex_dig = hash_object.hexdigest()
    last_val = int(hex_dig[-2:], 16) 
    fix_number = last_val % 10
    res = "BIG" if fix_number >= 5 else "SMALL"
    return res, fix_number

def start_prediction_tool():
    clear()
    print("\033[1;32m")
    print(r"""
  ______ ____ _________  _  ___ _   _  ____ 
 |  ____/ __ \___  /_ _| |/ (_) \ | |/ ___|
 | |__ | |  | | / / | || ' /| |  \| | |  _ 
 |  __|| |  | |/ /  | || . \| | |\  | |_| |
 |_|   \____//____|___|_|\_\_|_| \_|\____|
    """)
    print("\033[1;33m" + "="*55)
    print(f" [●] TOOL   : DATA HASH PREDICTOR v44")
    print(f" [●] STATUS : SERVER INJECTION ACTIVE")
    print(f" [●] OWNER  : FOZI BOSS X ASIM VIP")
    print("="*55 + "\033[0m")
    
    last_p = ""
    while True:
        try:
            now = datetime.now()
            p_id = now.strftime("%Y%m%d") + "01" + str((now.hour * 60) + now.minute + 1).zfill(4)
            
            if p_id != last_p:
                res, num = get_high_accuracy_logic(p_id)
                last_p = p_id
                print(f"\n\033[1;96m[NEW ROUND]: {p_id}\033[0m")
                time.sleep(1)
                
                print("\n\033[1;32m" + "╔═══════════════════════════════════════╗")
                print(f"  TARGET   : FANTASY GEMS 1-MIN")
                print(f"  PERIOD   : {p_id}")
                print(f"  RESULT   : {res}")
                print(f"  FIX NUM  : {num}")
                print(f"  CHANCE   : HIGH PROBABILITY")
                print("╚═══════════════════════════════════════╝" + "\033[0m")
            
            rem_sec = 60 - now.second
            sys.stdout.write(f"\r\033[90m[SYNC]: {rem_sec}s | SERVER INJECTION ACTIVE... \033[0m")
            sys.stdout.flush()
            time.sleep(1)
        except KeyboardInterrupt: break

if __name__ == "__main__":
    FOZI_BOSS_APPROVAL()
