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

    proxies = requests.get(url="https://advanced.name/freeproxy/655aee4dac487").text.split('\r\n')

    for proxy in proxies:

        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            req = session().post(tiktok_url, proxies={'http': f'http://{proxy}'})

            print(Fore.RED + f'[{current_time}]' + Fore.GREEN + f' Proxy: {proxy} Report Send')
        except:
            print(Fore.RED +'Ada yang salah. Ini mungkin tidak berfungsi dengan benar :) ')
            input('Tekan Enter untuk menutup program')
            exit()
