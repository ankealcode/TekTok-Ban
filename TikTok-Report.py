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

    proxies = requests.get(url="https://advanced.name/freeproxy/65599011927d7").text.split('\r\n') #Update Your Proxy List From This URL (https://advanced.name/freeproxy/)

    for proxy in proxies:

        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            req = session().post(tiktok_url, proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'})

            print(Fore.RED + f'[{current_time}]' + Fore.GREEN + f' Proxy: {proxy} Laporan Terkirim')
        except:
            print(Fore.RED +'Ada yang salah. Ini mungkin tidak berfungsi dengan benar :) ')
            input('Tekan Enter untuk menutup program')
            exit()