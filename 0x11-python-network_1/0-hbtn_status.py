#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status with urllib"""
from urllib import request

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    
    # Add headers to the request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = request.Request(url, headers=headers)

    try:
        with request.urlopen(req) as response:
            r = response.read()
            s = "Body response:\n\t- type: {}\n\t- content: {}"
            s += "\n\t- utf8 content: {}"
            print(s.format(type(r), r, r.decode('utf-8')))
    except Exception as e:
        print("An error occurred: {}".format(e))
