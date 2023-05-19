import random
import string
import threading
import requests
import os
import time

print("""\
WARNING: THIS GENERATOR IS ONLY FOR EDUCATIONAL AND TESTING PURPOSES.
BY USING THIS TOOL YOU MUST AGREE THAT, WE WILL NOT BE RESPONSIBLE FOR ANY
ILLEGAL USAGE OF THIS SOFTWARE.""")

time.sleep(3)
os.system('clear')

print("""\
██▓███   ██▓ ██ ▄█▀▄▄▄         ▄████ ▓█████  ███▄    █
▓██░  ██▒▓██▒ ██▄█▒▒████▄      ██▒ ▀█▒▓█   ▀  ██ ▀█   █
▓██░ ██▓▒▒██▒▓███▄░▒██  ▀█▄   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██░▓██ █▄░██▄▄▄▄██  ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░░██░▒██▒ █▄▓█   ▓██▒ ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░░▓  ▒ ▒▒ ▓▒▒▒   ▓▒█░  ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒
░▒ ░      ▒ ░░ ░▒ ▒░ ▒   ▒▒ ░   ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░        ▒ ░░ ░░ ░  ░   ▒    ░ ░   ░    ░      ░   ░ ░ 
░  ░  ░        ░  ░      ░     ░  ░         ░           """)
                                                       

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

looptimes = int(input('How many nitro codes would you like to generate?'))
check_nitro = input('Would you like to check the nitro codes generated? (y/n)')

if check_nitro == 'y':
    folder_path = "/Users/bai/Desktop/PikaGen" #CHANGE THIS TO YOUR OWN DIRECTORY!
    proxy_file = os.path.join(folder_path, "proxy.txt")
    hit_file = os.path.join(folder_path, "hit.txt")
    try:
        with open(proxy_file, 'r') as proxies:
            proxy_list = proxies.read().splitlines()
        proxies.close()
    except:
        print('Unable to open proxy file!')
        exit()

def check_nitro_code(code):
    global proxy_list
    global hit_file
    headers = {'Content-Type': 'application/json', 'authorization': code}
    try:
        proxy = random.choice(proxy_list)
        requests.get('https://discord.com/api/v9/users/@me', headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=5)
        print("VALID | " + code)
        with open(hit_file, 'a') as hits:
            hits.write(code + '\n')
        hits.close()
    except:
        print("INVALID | " + code)
        pass

def generate_codes():
    global check_nitro
    for x in range(looptimes // threads):
        code = "https://discord.gift/"+get_random_alphanumeric_string(19,0)
        if check_nitro == 'y':
            check_nitro_code(code)
        else:
            print(code)

threads = 10 # number of threads
threads_list = []
for i in range(threads):
    t = threading.Thread(target=generate_codes)
    threads_list.append(t)

for thread in threads_list:
    thread.start()

for thread in threads_list:
    thread.join()

input("Press Enter to exit.")
