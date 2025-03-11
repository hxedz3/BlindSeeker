import requests
import time

WEBSITES = [
    "https://github.com/{}",
    "https://twitter.com/{}",
    "https://instagram.com/{}",
    "https://www.reddit.com/user/{}",
    "https://www.pinterest.com/{}",
    "https://www.tiktok.com/@{}",
    "https://www.snapchat.com/add/{}",
    "https://steamcommunity.com/id/{}",
    "https://www.linkedin.com/in/{}",
    "https://www.youtube.com/c/{}",
    "https://facebook.com/{}",
    "https://www.pinterest.com/{}",
    "https://www.snapchat.com/add/{}",
    "https://www.twitch.tv/{}",
    "https://discord.com/users/{}",
    "https://open.spotify.com/user/{}",
    "https://soundcloud.com/{}",
    "https://www.tiktok.com/@{}",
    "https://medium.com/@{}",
    "https://www.deviantart.com/{}",
    "https://www.quora.com/profile/{}",
    "https://stackoverflow.com/users/{}",
    "https://gist.github.com/{}",
    "https://vine.co/u/{}",
    "https://myspace.com/{}",
    "https://kik.me/{}",
    "https://www.pscp.tv/{}",


]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def print_banner():
    """Prints a designed banner with the name 'blindSeeker'."""
    banner = """
      ▄▄▄▄    ██▓     ██▓ ███▄    █ ▓█████▄  頭|Headz 
▓█████▄ ▓██▒    ▓██▒ ██ ▀█   █ ▒██▀ ██▌       
▒██▒ ▄██▒██░    ▒██▒▓██  ▀█ ██▒░██   █▌       
▒██░█▀  ▒██░    ░██░▓██▒  ▐▌██▒░▓█▄   ▌       
░▓█  ▀█▓░██████▒░██░▒██░   ▓██░░▒████▓        OSINT username finder.
░▒▓███▀▒░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒        
▒░▒   ░ ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒        
 ░    ░   ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░        
 ░          ░  ░ ░           ░    ░           
      ░                         ░             
  ██████ ▓█████ ▓█████  ██ ▄█▀▓█████  ██▀███  
▒██    ▒ ▓█   ▀ ▓█   ▀  ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒███   ▒███   ▓███▄░ ▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒▓█  ▄ ▒▓█  ▄ ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░▒████▒░▒████▒▒██▒ █▄░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░     ░      ░   ░ ░░ ░    ░     ░░   ░ 
      ░     ░  ░   ░  ░░  ░      ░  ░   ░     

                                                                    
    """
    print(banner)

def check_username(username):
    """Checks if a username exists across multiple websites."""
    time.sleep(1)
    print(f"\nSearching for '{username}'...\n")

    try:
        for site in WEBSITES:
            url0 = site.format(username)
            response = requests.get(site, headers=HEADERS, timeout=5)
            if response.status_code == 200:
                time.sleep(1.5)
                print(f"\n[✔] Found match at: {url0}\n")
            elif response.status_code == 400:
                time.sleep(1)
                print(f"\n[✘] No match found at: {url0}\n")
    except requests.RequestException:
        print("\n[!]An error occurred, Please try again later. \n")

def main():
    print_banner() 
    username = input("[#]Enter the 'username': ").strip()
    check_username(username)

if __name__ == "__main__":
    main()











 



 
