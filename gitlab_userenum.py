#!/usr/bin/env python3

import requests
import argparse
import time
from requests.exceptions import ConnectTimeout, ConnectionError, ReadTimeout

def main():
    parser = argparse.ArgumentParser(description='GitLab User Enumeration')
    parser.add_argument('--url', '-u', type=str, required=True, help="The URL of the GitLab's instance")
    parser.add_argument('--wordlist', '-w', type=str, required=True, help='Path to the username wordlist')
    parser.add_argument('-v', action='store_true', help='Enable verbose mode')
    parser.add_argument('--delay', type=float, default=60.0, help="Delay (seconds) between retries")
    parser.add_argument('--output', type=str, default="valid_users.txt", help="PATH to output file for valid users")
    args = parser.parse_args()

    print('GitLab User Enumeration in python')

    counter = 0
    users = []
    with open(args.wordlist, 'r') as f:
        content = f.readlines()
        total = len(content)
        for line in content:
            counter += 1
            username = line.strip()
            if not username:
                continue
            if args.v:
                print(f'[{counter}/{total}] Trying username {username}...')
            attempt = 0
            while True:
                try:
                    response = requests.head(f'{args.url}/{username}', timeout=5)
                    http_code = response.status_code
                    if http_code == 200:
                        print(f'[+] The username {username} exists!')
                        users.append(username)
                    elif http_code == 0:
                        print('[!] The target is unreachable.')
                        break
                    break
                except (ConnectTimeout, ConnectionError, ReadTimeout) as e:
                    attempt += 1
                    print(f'[!] Connection error  {e} (attempt {attempt}, delay {args.delay*attempt})')
                    time.sleep(args.delay*attempt)
                    print('[*] Retrying...')
                        
    
    with open(args.output, 'w') as f:
        f.writelines(users)

if __name__ == '__main__':
    main()
