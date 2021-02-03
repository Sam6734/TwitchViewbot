import concurrent.futures, time, random, os

#desired channel url
channel_url = 'https://www.twitch.tv/yourchannelname'
#number of viewer bots
botcount = 10
#path to proxies.txt file
proxypath = "C:\Proxy\proxy.txt"
#path to vlc
playerpath = r'"C:\Program Files\VideoLAN\VLC\vlc.exe"'

#takes proxies from proxies.txt and returns to list
def create_proxy_list(proxyfile, shared_list):
    with open(proxyfile, 'r') as file:
        proxies = [line.strip() for line in file]
    for i in proxies:
        shared_list.append((i))
    return shared_list

#takes random proxies from the proxies list and adds them to another list
def randproxy(proxylist, botcount):
    randomproxylist = list()
    for _ in range(botcount):
        proxy = random.choice(proxylist)
        randomproxylist.append(proxy)
        proxylist.remove(proxy)
    return (randomproxylist)

#launches a viewer bot after a short delay
def launchbots(proxy):
    time.sleep(random.randint(5, 20))
    os.system(f'streamlink --player={playerpath} --player-no-close --player-http  --hls-segment-timeout 30 --hls-segment-attempts 3 --retry-open 1 --retry-streams 1 --retry-max 1 --http-stream-timeout 3600 --http-proxy {proxy} {channel_url} worst')

#calls the launchbots function asynchronously
def main(randomproxylist):
    with concurrent.futures.ThreadPoolExecutor() as executer:
        executer.map(launchbots, randomproxylist)

if __name__ == "__main__":
    main(randproxy(create_proxy_list(proxypath, shared_list=list()), botcount))
