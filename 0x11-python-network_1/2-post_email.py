import urllib.request
import urllib.parse
import sys

"""
Script to send a POST request with an email parameter to a given URL
and display the body of the response.
Usage: python script.py <URL> <email>
"""

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')  # Data should be bytes

try:
    # Send a POST request with the email parameter
    with urllib.request.urlopen(url, data=data) as response:
        # Decode and print the body of the response
        print(response.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
