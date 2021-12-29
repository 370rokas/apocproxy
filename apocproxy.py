#!/usr/bin/python3
"""
   ______________             __
  |__  /__  / __ \_________  / /______ ______
   /_ <  / / / / / ___/ __ \/ //_/ __ `/ ___/
 ___/ / / / /_/ / /  / /_/ / ,< / /_/ (__  )
/____/ /_/\____/_/   \____/_/|_|\__,_/____/

ApocProxy

Gets the latest proxies from https://lambda.black/

Author: 370rokas <https://github.com/370rokas/>
Created: 29th December, 2021
"""

import sys
import getopt
import requests
from colorama import Fore


def main():
    print(Fore.MAGENTA + '''
   ______________             __
  |__  /__  / __ \_________  / /______ ______
   /_ <  / / / / / ___/ __ \/ //_/ __ `/ ___/
 ___/ / / / /_/ / /  / /_/ / ,< / /_/ (__  )
/____/ /_/\____/_/   \____/_/|_|\__,_/____/

ApocProxy
Author: 370rokas <https://github.com/370rokas/apocproxy>
    ''' + Fore.RESET)

    argv = sys.argv[1:]
    options = "hu:t:f:"
    l_options = ["help", "url", "type", "filename"]

    check_url = ""
    proxy_type = ""
    filename = ""

    try:
        args, vals = getopt.getopt(argv, options, l_options)

        for c_arg, c_val in args:
            if c_arg in ("-h", '--help'):
                print(Fore.WHITE + "apocproxy.py -t <https/socks4/socks5> -u <url to check proxies> -f <filename>" + Fore.RESET)
                sys.exit()

            elif c_arg in ("-u", "--url"):
                print(Fore.WHITE + "[i] Checking proxies with " + c_val + Fore.RESET)
                check_url = c_val

            elif c_arg in ("-f", "--filename"):
                filename = c_val

            elif c_arg in ("-t", "--type"):
                if c_val == "https" or c_val == "socks4" or c_val == "socks5":
                    print(Fore.WHITE + "[i] Getting " + c_val + " proxies." + Fore.RESET)
                    proxy_type = c_val
                else:
                    print(Fore.RED + "[err] Invalid proxy type " + c_val + " please select https/socks4/socks5." + Fore.RESET)
                    sys.exit()

    except getopt.error as err:
        print(str(err))

    if check_url == "":
        print(Fore.WHITE + "[i] Checking proxies with default url." + Fore.RESET)
        check_url = "https://google.com"

    if proxy_type == "":
        print(Fore.WHITE + "[i] Getting https proxies." + Fore.RESET)
        proxy_type = "https"

    response = requests.get('https://lambda.black/apps/proxy/'+proxy_type)
    proxies = []
    proxies.extend(response.text.splitlines())

    working_proxies = []

    print(Fore.WHITE + "[i] Checking proxies." + Fore.RESET)

    for proxy in proxies:
        proxy_type = {}

        if proxy_type == "https":
            proxy_arr = {
                str(proxy_type): "https://" + proxy
            }
        else:
            proxy_arr = {
                str(proxy_type): proxy
            }

        a = requests.get(check_url, proxies=proxy_arr)
        if a.status_code == 200:
            working_proxies.append(proxy)
            print(Fore.GREEN + "[+] Proxy " + proxy + " works." + Fore.RESET)
        else:
            print(Fore.RED + "[-] Proxy " + proxy + " doesn't work." + Fore.RESET)

    print(Fore.GREEN + "[i] Working proxies: " + str(len(working_proxies)) + "/" + str(len(proxies)) + Fore.RESET)

    if filename == "":
        print(working_proxies)
    else:
        with open(filename, 'w') as f:
            for proxy in working_proxies:
                f.write("%s\n" % proxy)

        print(Fore.GREEN + "Saved proxies to: " + filename + Fore.RESET)


if __name__ == '__main__':
    main()
