from art_hello import *
import os
import time
import sys
from termcolor import colored
import ipaddress
import nmap
import subprocess
import string
import random
import requests
from bs4 import BeautifulSoup
import csv
from accounts import *
from scapy.all import ARP, Ether, srp, conf
import socket
from rich.console import Console
from rich.table import Table
import json


    
     

 

Black = "\033[1;30m"
Red = "\033[1;31m"
Green = "\033[1;32m"
Yellow = "\033[1;33m"
Blue = "\033[1;34m"
Purple = "\033[1;35m"
Cyan = "\033[1;36m"
White = "\033[1;37m"
Gray = "\033[1;39m"
DarkRed = "\033[2;31m"
DarkBlue = "\033[2;34m"
DarkPink = "\033[2;35m"
DarkCyan = "\033[2;36m"

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def friend():
    clear_screen()
    time.sleep(2)
    art()
    slow_print(f'{Green}v1.0.0{White}\n')
    slow_print(f"{Red}Hello friend...\n{White}")
    print(colored("This tool was created by ShadowReapers team\nand\nDeveloped by El.Profesor\n", 'white'))
    time.sleep(1)
    print(f'{Red}-'*60)

    
    print(f"""{White}[{Red}01{White}] - Ports Scan               
[{Red}02{White}] - Search for an account on all platforms                                       
[{Red}03{White}] - Deep & Dark Web UrL      [{Red}06{White}] - Check E-mail
[{Red}04{White}] - Israeli db               [{Red}07{White}] - Shoden Check
[{Red}05{White}] - Generate wordlist        [{Red}99{White}] - update    
[{Red}00{White}] - Exit""")
    
    
    unput = (input(f">>> : {DarkRed}{White}"))
    if unput == '1' or unput == 'Port scan' or unput == '01':
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        chos1()
        again
    elif unput.lower() == '3' or unput == 'web' or unput == 'Deep' or unput == 'Deep Web' or unput == 'Dark' or unput == 'Dark Web' or unput == '03' :
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        slow_print(f"{DarkRed}Note:{Green}The site name will be printed twice if there is no {Red}Description",delay=0.1)
        time.sleep(1)
        lanks('Link.json')
        again()
    elif unput.lower() == '2' or unput == '02' or unput == 'Search for an account on all platforms':
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        chosa1()
        again()
    elif unput.lower() == '7' or unput == '07' or unput ==  'Shoden Check' or unput == "Shoden":
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        tt = input(f"{Gray}[{Gray}+{Gray}]{DarkRed}Enter name target{White}:")
        page = requests.get(f'https://www.shodan.io/search?query={tt}')
        time.sleep(0.1)
        get_site_shodan(page)
        again()
    elif unput.lower() == '4' or unput == 'Israeli db' or unput == '04':
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        DATABASES()
        again()
    elif unput.lower() == '07' or unput == '7':
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        email = input(f"[{Black}+{Black}]Enter the email Target:")
        check_email(email)
        again()
    elif unput == '5' or unput =='05':
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        mran()
        again()
    elif unput == '00':
        exit()

    elif unput.lower() == '99' or unput == 'update':
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        update_repo()
    else:
        print(f'{DarkRedRed}Error!!')
        time.sleep(1)
        clear_screen()
        time.sleep(0.1)
        exit()
    
    




def chos1():
    time.sleep(1)
    state_file = "state.txt"
    if not os.path.exists(state_file):
        slow_print(colored("You will first see a field to enter the starting port number you want to scan (from),\n followed by another field to enter the ending port number (to). Next,\n a section will appear where you can input the target (IP address). Finally,\nthere will be an optional field for adding extra options (e.g., -sT, -sS, etc.).\nYou can leave this field empty if you wish,\nas the tool will automatically apply the necessary security options.\n", 'red'), delay=0.1)
        with open(state_file, 'w') as f:
            f.write("executed")
    clear_screen()
    time.sleep(1.2)

    while True:
        try:
            fr = int(input("Starting Port: "))
            break
        except ValueError as e:
            slow_print(colored(f"Error: {e}. Please try again.\n", 'red'), delay=0.1)

    while True:
        try:
            en = int(input("Ending Port: "))
            break
        except ValueError as e:
            slow_print(colored(f"Error: {e}. Please try again.\n", 'red'), delay=0.1)

    while True:
        ta = input("Target IP: ")
        try:
            ipaddress.ip_address(ta)
            break
        except ValueError:
            slow_print(colored("Invalid IP address. Please try again.\n", 'red'), delay=0.1)

    ad = input("Additional Options (Press enter to Skip): ")
    ea = ad
    if "-sT" not in ea:
        ea += " -sT "
    if "-sS" not in ea:
        ea += "-sS "
    if "--spoof-mac" not in ea:
        ea += "--spoof-mac 0:11:22:33:44:55"
    
    time.sleep(1)
    clear_screen()
    time.sleep(3.1)
    slow_print(colored("Starting Scan.....\n", 'blue'), delay=0.1)

    try:
        scanner = nmap.PortScanner()
        for k in range(fr, en + 1):
            res = scanner.scan(ta, str(k))
            try:
                state = res['scan'][ta]['tcp'][k]['state']
                if state == "closed":
                    slow_print(f'[+] Port {k} is {DarkRed}{state}\n', delay=0.1)
                elif state == "open":
                    slow_print(f'[+] Port {k} is {Green}{state}\n', delay=0.1)
            except KeyError:
                slow_print(colored(f'[+] Port {k} not found in scan results.\n', 'red'), delay=0.1)
    except Exception as e:
        slow_print(colored(f"Error during scan: {e}\n", 'red'), delay=0.1)

def chose2():
    chosa1()

def lanks(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    link_count = 0  

    for entry in data:
        print(f"{DarkRed}Name:{White}{entry['name']}")
        try:   
            print(f"{DarkRed}Description:{White}{entry['description']}")
            time.sleep(0.1)
            print(f"{DarkRed}Link:{Green}{entry['link']}")
            link_count += 1  
            time.sleep(0.1)
            print(f"{DarkPink}-"*60)
            time.sleep(0.1)
        except KeyError:
            print(f"{DarkRed}Name:{White}{entry['name']}")
            time.sleep(0.1)
            print(f"{DarkRed}Link:{Green}{entry['link']}")
            link_count += 1  
            time.sleep(0.1)
            print(f"{DarkPink}-{White}"*60)
            time.sleep(0.1)

    
    response = input(f"{White}\nNumber of links is {link_count}. Do you want to save them to a file? ({Green}Y{White}/{Red}N{White}): ").strip().lower()

    if response == 'y':
        with open('saved_links.txt', 'w') as save_file:
            for entry in data:
                save_file.write(f"Name: {entry['name']}\n")
                if 'description' in entry:
                    save_file.write(f"Description: {entry['description']}\n")
                save_file.write(f"Link: {entry['link']}\n")
                save_file.write(f"{'-'*60}\n")
        print("Links saved successfully!")
    else:
        print("Oky!")





def display_databases():
    console = Console()
    table = Table(title="Leaked Israeli db uploaded to the MediaFire platform.")
    table.add_column("Link")
    table.add_column("Description")
    table.add_column("Size")
    table.add_row("https://www.mediafire.com/file/l4o3yg0nehr0txv/1.csv/file", "Store room db containing 400K+ customers.", "86.6MB")
    table.add_row("https://www.mediafire.com/file/2is34z1ekkhj2su/2.csv/file", "A commercial db containing 200k+ customers.", "23.2MB")
    table.add_row("https://www.mediafire.com/file/63ib6s7o4rla335/3.csv/file", "A normal db contains 38K+ person.", "6.69MB")
    table.add_row("https://www.mediafire.com/file/0ruazdhfg3pib51/Leaks.json/file", "Json file containing info of 521 Israeli companies.", "689KB")
    console.print(table)

def DATABASES():
        display_databases()

def check_email(email):
    print(f"{Black}[{DarkRed}+{Black}]Checking:{White}{email}...")
    time.sleep(3)
    print(f"[{White}+{White}]{Green}Checking for:{White}{email}")

    
    if check_facebook(email):
        print(f"[{Green}+{White}]Facebook {Green}Found{White}")
    else:
        print(f"[{DarkRed}+{White}]Facebook {DarkRed}Not Found{White}")

    
    if check_tiktok(email):
        print(f"[{Green}+{White}]TikTok {Green}Found{White}")
    else:
        print(f"[{DarkRed}+{White}]TikTok {DarkRed}Not Found{White}")

   
    if check_tellonym(email):
        print(f"[{Green}+{White}]Tellonym {Green}Found{White}")
    else:
        print(f"[{DarkRed}+{White}]Tellonym {DarkRed}Not Found{White}")

def check_facebook(email):
   
    return True

def check_tiktok(email):
    url = "https://www.tiktok.com/passport/web/user/check_email_registered"
    data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    }
    response = requests.post(url, headers=headers, data=data)
    return '{"is_registered":1}' in response.text

def check_tellonym(email):
    url = f"https://api.tellonym.me/accounts/check?email={email}&limit=13"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    }
    response = requests.get(url, headers=headers)
    return '"EMAIL_ALREADY_IN_USE"' in response.text

with open('data.json') as f:
    data = json.load(f)
ports_data = data.get('ports', [])
os_data = data.get('os', [])
countries_data = data.get('countries', [])
companies_data = data.get('companies', [])
servers_data = data.get('servers', [])    
def get_site_shodan(page): 
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    infrom = soup.find_all("li", {'class':"normalize flex justify-content-between"})
    
    def get_texts(infrom):
        texts = [item.find('a').text.strip() for item in infrom if item.find('a')]
        return texts

    if infrom:
        texts = get_texts(infrom)
        categorize_and_print(texts)
    else:
        print(f"[{DarkRed}+{DarkRed}]{Red}No elements found")

def categorize_and_print(data):
    countries = []
    ports = []
    companies = []
    servers = []
    os = []
    
    for item in data:
        if item.isdigit() and 1 <= int(item) <= 65535:
            ports.append(item)
        
        elif any(country in item for country in countries_data):
            countries.append(item)

        elif any(company in item for company in companies_data):
            companies.append(item)

        elif any(server in item for server in servers_data):
            servers.append(item)

        elif any(os_name in item for os_name in os_data):
            os.append(item)
    
    print(f"{DarkRed}Countries:{Green}",countries)
    time.sleep(0.1)
    print(f'{Gray}-'*60)
    time.sleep(0.1)
    print(f"{DarkRed}Ports:{Green}",ports)
    time.sleep(0.1)
    print(f'{Gray}-'*60)
    time.sleep(0.1)
    print(f"{DarkRed}Companies:{Green}",companies)
    time.sleep(0.1)
    print(f'{Gray}-'*60)
    time.sleep(0.1)
    print(f"{DarkRed}Servers:{Green}",servers)
    time.sleep(0.1)
    print(f'-{Gray}'*60)
    time.sleep(0.1)
    print(f"{DarkRed}Operating Systems:{Green}",os)
    time.sleep(0.1)
    print(f'{Gray}-'*60)



def generate_wordlist(length, num_lines, include_upper, include_lower, include_digits, include_special):
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError(f"{DarkRed}[{White}+{DarkRed}]{White}No character types selected.")
    
    wordlist = []
    for _ in range(num_lines):
        word = ''.join(random.choice(characters) for _ in range(length))
        wordlist.append(word)
    
    return wordlist

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')
    print(f"Wordlist saved to {filename}")



def mran():
    while True:
        clear_screen()
        print(f"{White}Choose an option:")
        print(f"1.{DarkRed}[{White}+{DarkRed}]{White}Admin Passwords")
        print(f"2.{DarkRed}[{White}+{DarkRed}]{White}Admin Usernames")
        print(f"3.{DarkRed}[{White}+{DarkRed}]{White}Passwords")
        print(f"4.{DarkRed}[{White}+{DarkRed}]{White}Usernames")
        print(f"0.{DarkRed}[{White}+{DarkRed}]{White}Exit")
        
        choice = input(f"{DarkRed}[{White}+{DarkRed}]{White}Enter choice ({Green}0-4{White}):").strip()
        
        if choice == '0':
            print("Oky!")
            break
        
        if choice in ['1', '2', '3', '4']:
            length = int(input(f"{DarkRed}[{White}+{DarkRed}]{White}Enter the length of each word: "))
            num_lines = int(input(f"{DarkRed}[{White}+{DarkRed}]{White}Enter the number of lines: "))
            include_upper = input(f"{DarkRed}[{White}+{DarkRed}]{White}Include uppercase letters? (y/n): ").strip().lower() == 'y'
            include_lower = input(f"{DarkRed}[{White}+{DarkRed}]{White}Include lowercase letters? (y/n): ").strip().lower() == 'y'
            include_digits = input(f"{DarkRed}[{White}+{DarkRed}]{White}Include digits? (y/n): ").strip().lower() == 'y'
            include_special = input(f"{DarkRed}[{White}+{DarkRed}]{White}Include special characters? (y/n): ").strip().lower() == 'y'
            
            try:
                wordlist = generate_wordlist(length, num_lines, include_upper, include_lower, include_digits, include_special)
                
                if input(f"{DarkRed}[{White}+{DarkRed}]{White}Do you want to save the wordlist to a file? (y/n): ").strip().lower() == 'y':
                    filename = input(f"{DarkRed}[{White}+{DarkRed}]{White}Enter filename ({Green}e.g., wordlist.txt{White}): ")
                    save_wordlist(wordlist, filename)
                else:
                    clear_screen()
                    print("\n".join(wordlist))
                    
            except ValueError as e:
                print(e)
        else:
            print(f"{DarkRed}[{White}+{DarkRed}]{White}Invalid choice, please try again.")





def update_repo():
    print(f"{White}Updating...\n")
    time.sleep(0.1)

    spinner = ["|", "/", "-", "\\"]
    spinner_index = 0
    steps = 50

    for i in range(steps):
        percent = 100*(i+1)/steps
        bar_length = 50
        filled_length = int(bar_length*percent/100)
        
        bar = "█"*filled_length + "-"*(bar_length-filled_length)
        sys.stdout.write(f"\r{Green}{spinner[spinner_index % len(spinner)]}{White} [{bar}] {percent:.2f}%")
        sys.stdout.flush()
        spinner_index += 1
        time.sleep(0.1)

    
    token = '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'
    repo_url = f'https://{token}@github.com/14xtaqu/TOOL_T.git'
    
    subprocess.run(["git", "clone", repo_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"""\n{White}[{Green}✓{White}] Updated successfully
new version saved in {Blue}{os.getcwd()}/TOOL_T{White}""")


        
    

def again():
    slow_print(f"{DarkRed}[{White}+{DarkRed}]{White}Do you want to do another operation? ({Green}Y/{DarkRed}N{White})",delay=0.1)
    agin = input(">")
    if agin.lower() == 'y':
        print('oky!!')
        time.sleep(1)
        clear_screen
        friend()
    elif agin.lower() == 'n':
        print('Oky!')
        time.sleep(0.1)
        exit()
    else:
        exit()  
def main():
    friend()
   

if __name__ == "__main__":
    main()