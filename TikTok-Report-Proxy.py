import time
from datetime import datetime
from colorama import *
import requests
from requests.sessions import session

print(Fore.RED + '''
████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗   ██████╗  █████╗ ███╗   ██╗
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝   ██╔══██╗██╔══██╗████╗  ██║
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝    ██████╔╝███████║██╔██╗ ██║
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗    ██╔══██╗██╔══██║██║╚██╗██║
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗██╗██████╔╝██║  ██║██║ ╚████║
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                                         GitHub: ANKEALcode                                  
''')

tiktok_url = input("Request Link: ")

while True:
    with open("proxy.txt", "r") as file:
        proxies = file.read().splitlines()

    for proxy in proxies:
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            req = session().post(tiktok_url, proxies={'https': f'https://{proxy}'})
            print(Fore.RED + f'[{current_time}]' + Fore.GREEN + f' Proxy: {proxy} Report Send')
        except:
            print(Fore.RED + 'Ada yang salah. Ini mungkin tidak berfungsi dengan benar.')
            input('Tekan Enter untuk menutup program')
            exit()

        # Add a delay between requests (e.g., 1 second)
        time.sleep(1)
