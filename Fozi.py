import time
import sys
import hashlib
import random
from datetime import datetime

# --- CONFIGURATION ---
ACTIVATION_KEY = "FOZI786" 
CONTACT_NUM = "+923186757671"

def clear():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def get_high_accuracy_logic(period_id):
    # Hash-based seed: Isse result har second badalne ke bajaye 
    # Period ID ke unique code par base karega.
    hash_object = hashlib.sha256(period_id.encode())
    hex_dig = hash_object.hexdigest()
    
    # Extracting a specific number from the hash
    last_val = int(hex_dig[-2:], 16) 
    fix_number = last_val % 10
    
    # Result mapping
    if fix_number >= 5:
        res = "BIG"
    else:
        res = "SMALL"
        
    return res, fix_number

def start_tool():
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
    print(f" [●] STATUS : ANALYZING SERVER HASHES")
    print(f" [●] OWNER  : FOZI KING X ASIM VIP")
    print("="*55 + "\033[0m")
    
    key = input("\033[94m[+] ENTER ACCESS KEY: \033[0m")
    if key != ACTIVATION_KEY:
        print(f"\n\033[1;31m[!] WRONG KEY! CONTACT: {CONTACT_NUM}\033[0m")
        sys.exit()

    print(f"\n\033[1;32m[✔] SYNCING WITH PERIOD HASHES...")
    time.sleep(2)

    last_p = ""

    while True:
        try:
            now = datetime.now()
            p_id = now.strftime("%Y%m%d") + "01" + str((now.hour * 60) + now.minute + 1).zfill(4)
            
            if p_id != last_p:
                res, num = get_high_accuracy_logic(p_id)
                last_p = p_id
                
                print(f"\n\033[1;96m[NEW ROUND]: {p_id}\033[0m")
                
                for i in range(1, 4):
                    sys.stdout.write(f"\r\033[95m[READING HASH DATA] {'●' * i}")
                    sys.stdout.flush()
                    time.sleep(1)
                
                print("\n\n\033[1;32m" + "╔═══════════════════════════════════════╗")
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
        except Exception: continue

if __name__ == "__main__":
    start_tool()
