#!/usr/bin/python3
import pyperclip
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

MODS_FILE = os.path.join(SCRIPT_DIR, 'mods.txt')

MODS_FILE = 'mods.txt'

def load_mods(filename):
    mods_dict = {}
    
    
    if not os.path.exists(filename):
        print(f"[-] Error: {filename} not found!")
        return mods_dict

    with open(filename, 'r', encoding='utf-8') as file:
        enumerate(file, 1) 
        for index, line in enumerate(file, 1):
            line = line.strip() 
            if not line or '|' not in line:
                continue
                
            name, regex = line.split('|')
            
            mods_dict[str(index)] = {
                "mod_name": name,
                "regex": regex
            }
    return mods_dict 

mods_db = load_mods(MODS_FILE)                          
if not mods_db:
    print("Error: Data base is empty!")
else:    
    print("=== PoE Map Regex Generator ===".center(65))

    print("-"*65)

    print("Choose the mods to avoid (enter numbers separated by spaces):")

    print("-"*65)

    for key, val in mods_db.items():
        print(f"[{key}] - {val['mod_name']}")

    print("-"*65)

    user_input = input(": ")
    selected_mods = user_input.split()

    print("-"*65)

    final_regex_list = []

    for key in selected_mods:
        if key in mods_db:
            found_regex = mods_db[key]["regex"]
            final_regex_list.append(found_regex)
            print(f"[+] Added: {found_regex}")
        else:
            print(f"Mod [{key}] is an illusion, Exile. Not found!")

    print("-"*65)   

    final_paste = "|".join(final_regex_list)
    print(f"Your regex, Exile: [ {final_paste} ] \n" + "-"*65 )

    pyperclip.copy(final_paste)
    print("[+] Regex copied! Journey well, Exile!")

    print("-"*65)