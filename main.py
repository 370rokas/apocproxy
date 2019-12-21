import requests

#Proxyes from Apoc, check out his website: apoc.club

print("On which website to check:\n1.google\n2.netflix\n3.spotify")

b = input()

web = ""

if b == '1':
    web = "https://google.com"
elif b == '2':
    web = "https://netflix.com"
elif b == '3':
    web = "https://spotify.com"


socks4response = requests.get('https://proxy.apoc.club/socks4/')
socks4 = []
socks4.extend(socks4response.text.splitlines())

socks5response = requests.get('https://proxy.apoc.club/socks5/')
socks5 = []
socks5.extend(socks5response.text.splitlines())

httpresponse = requests.get('https://proxy.apoc.club/http/')
http = []
http.extend(httpresponse.text.splitlines())

socks4proxy = []
for x in socks4:
    proxys = {
        "socks4": x
    }
    a = requests.get(web, proxies=proxys)
    if a.status_code == 200:
        socks4proxy.append(x)
        print("socks4",x,": working")
    else:
        print("socks4",x,": not working")
        
        
socks5proxy = []
for x in socks5:
    proxys = {
        "socks5": x
    }
    a = requests.get(web, proxies=proxys)
    if a.status_code == 200:
        socks5proxy.append(x)
        print("socks5",x,": working")
    else:
        print("socks5",x,": not working")

httpproxy = []
for x in http:
    proxys = {
        "http": x
    }
    a = requests.get(web, proxies=proxys)
    if a.status_code == 200:
        httpproxy.append(x)
        print("http",x,": working")
    else:
        print("http",x,": not working")
        
print("Socks4: ",len(socks4proxy),'/',len(socks4))

print("Socks5: ",len(socks5proxy),'/',len(socks5))

print("Http/s: ",len(httpproxy),'/',len(http))

print("Save proxies to file? (y/n)")

c = input()

if c == 'y':
    with open('socks4.txt', 'w') as f:
        for item in socks4proxy:
            f.write("%s\n" % item)
    with open('socks5.txt', 'w') as f:
        for item in socks5proxy:
            f.write("%s\n" % item)
    with open('http.txt', 'w') as f:
        for item in httpproxy:
            f.write("%s\n" % item)


