#!/usr/bin/env python3
try: 
    import requests, os, time, re, json
    from rich.console import Console
    from rich import print
    from rich.panel import Panel
except (Exception) as e:
    exit(f"[Error] {str(e).capitalize()}!")
print("FOLLOWE MY INSTAGRAM ID....!")
os.system("xdg-open https://www.instagram.com/ali_up46")
def Banner():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )
    return ("""[bold red]● [bold yellow]● [bold green]●
[bold red],--------.      ,--.                          
'--.  .--',---. |  |,-. ,---. ,--,--, ,-----. 
   |  |  | .-. ||     /| .-. :|      \`-.  /  
[bold white]   |  |  ' '-' '|  \  \\\\   --.|  ||  | /  `-. 
   `--'   `---' `--'`--'`----'`--''--'`-----'\n\n
[bold White][•]CREATED BY  :  MAHTAB AHMAD
[•]ONE GITHUB  :  MAHTAB-12
[•]TOOLS FB    :  COOKIE  TO TOKEN\n------------------------------------------""")

class Cookies:

    def __init__(self) -> None:
        pass

    def Token(self):
        try:
            print(Banner(),f"[bold bright_black]  ")
            print(Panel(f"[bold green]COOKIE GRNET GET ACCESS TOKEN PEAST FRESH COOKIE", width=50, style="white", title=">>> CREATER MAHTAB AHMAD <<<", subtitle="╭────", subtitle_align="left"))
            cookies = Console().input("[bold bright_black]   ╰─> Cookie ")
            with requests.Session() as r:
                params = {
                    'client_id': '124024574287414',
                    'wants_cookie_data': 'true',
                    'origin': '1',
                    'input_token': '',
                    'sdk': 'joey',
                    'redirect_uri': 'https://www.instagram.com/Ali_up46/',
                }
                r.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
                response = r.get('https://www.facebook.com/x/oauth/status', params = params, cookies = {
                    'cookie': cookies
                })
                if '"access_token":' in str(response.headers):
                    self.your_token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    self.user_id = re.search('"user_id":"(\d+)"', str(response.headers)).group(1)
                else:
                    #print(Panel(f"[italic red]Maaf, Tidak Ada Akses Token Yang Ditemukan!", width=50, style="bold bright_black", title=">>> Tidak Ditemukan <<<"))
                    exit()
                os.system('clear')
                print(Banner(),f"[bold White]\n\n[•] Get Access Token ")
                print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f"[bold green]{self.your_token}")
                print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                Console().input("[bold white][[bold green]•] Copy Token[bold white]]")
                exit(f"\nYour Token : {self.your_token}\n")
        except (Exception) as e:
            print(Panel(f"[italic red]{str(e).title()}!", width=50, style="bold bright_black", title=">>> Error <<<"))
            exit()

if __name__ == '__main__':
    try:
        if os.path.exists("Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/SK-BAAP-786/Token/main/Instagram.json').text)['Link']
            os.system(f'xdg-open {instagram_url}')
            with open('Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(3.5)
        os.system('git pull')
        Cookies().Token()
    except (Exception) as e:
        print(Panel(f"[italic red]{str(e).title()}!", width=50, style="bold bright_black", title=">>> Error <<<"))
        exit()
    except (KeyboardInterrupt):
        exit()
