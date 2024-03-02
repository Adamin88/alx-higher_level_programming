#!/usr/bin/python3
"""
A script to fetch and display the body of a URL using urllib.
"""

import urllib.request


def main():
    """
    Fetches the body of a URL and displays it.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", utf8_content)


if __name__ == "__main__":
    main()
