from utils import clear, init_panel
from colorama import init, Fore
from time import sleep, strftime

init()

def main() -> None:
    hour = strftime("%H:%M:%S")
    print(f"""{Fore.RED}
███▄    █  ██▓▒██   ██▒  ██████   █████   █    ██  ▄▄▄      ▓█████▄ 
██ ▀█   █ ▓██▒▒▒ █ █ ▒░▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▒████▄    ▒██▀ ██▌
▓██  ▀█ ██▒▒██▒░░  █   ░░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ░██   █▌
▓██▒  ▐▌██▒░██░ ░ █ █ ▒   ▒   ██▒░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ░▓█▄   ▌
▒██░   ▓██░░██░▒██▒ ▒██▒▒██████▒▒░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒░▒████▓ 
░ ▒░   ▒ ▒ ░▓  ▒▒ ░ ░▓ ░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░ ▒▒▓  ▒ 
░ ░░   ░ ▒░ ▒ ░░░   ░▒ ░░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░ ░ ▒  ▒ 
░   ░ ░  ▒ ░ ░    ░  ░  ░  ░     ░   ░  ░░░ ░ ░   ░   ▒    ░ ░  ░ 
    ░  ░   ░    ░        ░      ░       ░           ░  ░   ░    
                                                    ░      
                    {Fore.RED}Current hour: {Fore.BLUE}[{hour}]{Fore.RESET}
{Fore.GREEN}⩥-----------------------------------------------------------------⩤{Fore.RED}
{Fore.GREEN}|                        {Fore.RED}complete raid tool                       {Fore.GREEN}|
{Fore.GREEN}------------------------------------------------------------------
{Fore.GREEN}|                            {Fore.RED}coded by                             {Fore.GREEN}|
{Fore.GREEN}|                             {Fore.RED}nsnt                                {Fore.GREEN}|
{Fore.GREEN}------------------------------------------------------------------
{Fore.GREEN}|                        {Fore.RED}# N I X S Q U A D                        {Fore.GREEN}|
{Fore.GREEN}⩥-----------------------------------------------------------------⩤{Fore.RESET}
    """)


if __name__ == "__main__":
    try:
        clear()
        main()
        init_panel()
    except Exception as exception:
        clear()
        main()
        init_panel()
        print(f'{exception}')