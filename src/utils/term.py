import os

def clear() -> None:
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print('\n'*os.get_terminal_size().columns)