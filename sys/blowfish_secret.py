#!usr/bin/python
"""
Usage: 
Generate random 32 chars, used for set blowfish_secret in phpmyadmin
"""

import string, random


def generate(length = 32, secret = string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(secret) for _ in range(length))

# default method call
print(generate())

# parameter method call (length, phrase)
print(generate(5, "someword"))

