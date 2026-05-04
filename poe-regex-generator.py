import pyperclip
import os
import sys
import traceback  

def main():
    
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))

    MODS_FILE = os.path.join(application_path, 'mods.txt')
    

    def load_mods(filename):
        mods_dict = {}
        if not os.path.exists(filename):
            print(f"[-] Ошибка: Файл {filename} не найден!")
            print(f"[-] Я искал его по этому пути: {filename}")
            return mods_dict

        with open(filename, 'r', encoding='utf-8') as file:
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
        print("[-] База модов пуста или файл не найден.")
        return 
        
    print("=== PoE Map Regex Generator ===".center(65))
    print("-" * 65)
    
    for key, val in mods_db.items():
        print(f"[{key}] - {val['mod_name']}")

    print("-" * 65)
    user_input = input("Choose the mods to avoid (enter numbers separated by spaces): ")
    selected_mods = user_input.split()

    print("-" * 65)
    final_regex_list = []

    for key in selected_mods:
        if key in mods_db:
            found_regex = mods_db[key]["regex"]
            final_regex_list.append(found_regex)
            print(f"[+] Added: {found_regex}")
        else:
            print(f"[-] Mod [{key}] is an illusion, Exile. Not found!")

    print("-" * 65)   

    if final_regex_list:
        final_paste = "|".join(final_regex_list)
        formatted_result = f'"{final_paste}"'
        print(f"Your regex, Exile: [ {formatted_result} ]")
        pyperclip.copy(formatted_result)
        print("[+] Regex copied! Journey well, Exile!")
    else:
        print("[-] No valid mods selected.")
    
    print("-" * 65)


if __name__ == "__main__":
    try:
        main() 
    except Exception as e:
        
        print("\n[!!!] ПРОИЗОШЛА КРИТИЧЕСКАЯ ОШИБКА [!!!]")
        traceback.print_exc() 
        
   
    input("\nPress Enter to exit...")
