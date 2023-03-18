!/usr/bin/env python3

"""
A simple script used for testing python github action
"""

import requests

response = requests.get('https://www.google.com')

print(response.text)
