#!/usr/bin/python3
import requests
import os

def download(url):
    try:
        req = requests.get(url)
    except requests.exception.MissionSchema:
        print('Invalid URL {}'.format(url))
        return

    if req.status_code == 403:
        print('You do not have the authority to access this page.')
        return
    filename = url.split('/')[-1]
    if os.path.exists(filename):
        return print('The filename is existes.')
    else:
        with open(filename,'w') as fobj:
            fobj.write(req.content.decode('utf-8'))
            print('Download over.')

if __name__ == '__main__':
    url = input("Enter a URL :")
    download(url)

