from colorama import Fore, init

init(autoreset=True)

def show_banner():
    print(Fore.CYAN + "=" * 70)
    print(Fore.GREEN + r"""
   _____                          _____
  / ____|                        / ____|
 | (___   ___  ___ _   _ _ __   | (___   ___ __ _ _ __
  \___ \ / _ \/ __| | | | '__|   \___ \ / __/ _` | '__|
  ____) |  __/ (__| |_| | |      ____) | (_| (_| | |
 |_____/ \___|\___|\__,_|_|     |_____/ \___|\__,_|_|
    """)
    print(Fore.YELLOW + "              SecureScan Pro v2.0")
    print(Fore.WHITE + "      Python Cybersecurity Network Scanner")
    print(Fore.CYAN + "=" * 70)