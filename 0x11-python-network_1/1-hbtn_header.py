import urllib.request
import sys

"""
Script to fetch the value of the X-Request-Id header from a given URL.
Usage: python script.py <URL>
"""

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Retrieve the value of the X-Request-Id header
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
except Exception as e:
    print("Error:", e)
