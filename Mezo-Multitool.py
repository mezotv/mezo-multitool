import os
from colorama import Fore
import webbrowser

def ResetTool():
    while 1:
        Design()
        os.system("cls")

def Design():
    os.system("cls && title YoutubeMultiTool")
    print(f'''
    
{Fore.RED}$$\      $$\                                       $$\      $$\           $$\   $$\     $$\   $$\                         $$\ 
{Fore.RED}$$$\    $$$ |                                      $$$\    $$$ |          $$ |  $$ |    \__|  $$ |                        $$ |
{Fore.RED}$$$$\  $$$$ | $$$$$$\  $$$$$$$$\  $$$$$$\          $$$$\  $$$$ |$$\   $$\ $$ |$$$$$$\   $$\ $$$$$$\    $$$$$$\   $$$$$$\  $$ |
{Fore.RED}$$\$$\$$ $$ |$$  __$$\ \____$$  |$$  __$$\ $$$$$$\ $$\$$\$$ $$ |$$ |  $$ |$$ |\_$$  _|  $$ |\_$$  _|  $$  __$$\ $$  __$$\ $$ |
{Fore.RED}$$ \$$$  $$ |$$$$$$$$ |  $$$$ _/ $$ /  $$ |\______|$$ \$$$  $$ |$$ |  $$ |$$ |  $$ |    $$ |  $$ |    $$ /  $$ |$$ /  $$ |$$ |
{Fore.RED}$$ |\$  /$$ |$$   ____| $$  _/   $$ |  $$ |        $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$\ $$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |
{Fore.RED}$$ | \_/ $$ |\$$$$$$$\ $$$$$$$$\ \$$$$$$  |        $$ | \_/ $$ |\$$$$$$  |$$ |  \$$$$  |$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |
{Fore.RED}\__|     \__| \_______|\________| \______/         \__|     \__| \______/ \__|   \____/ \__|   \____/  \______/  \______/ \__|

                                                        {Fore.LIGHTGREEN_EX} Youtube-Multitool ;)
                                                            {Fore.LIGHTGREEN_EX} By Mezo                                                                                             

    ''')
    print("")
    print(
        f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}1{Fore.LIGHTWHITE_EX}] Youtube-Channel")
    print("")
    print("")

    youtube = input("> ")

    if youtube == "1":
        webbrowser.open_new_tab('www.youtube.com/channel/UCxZz0FVyqssrabT_kkGUgAQ?sub_confirmation=1')

    else:
        print("")
        Design()


ResetTool()

os.system("cls")
