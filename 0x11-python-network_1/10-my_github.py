#!/usr/bin/python3
"""script that uses Github API to display id, must use Github credentials"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get(url, auth=(username, token))
    print(response.json().get('id'))
