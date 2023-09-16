#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import pyotp
from argparse import ArgumentParser, Namespace

help = """

usage: 2FA.py [-h] [-k KEY]

options:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  The setup key provided for manually configuring the authenticator app

"""

parser = ArgumentParser()

parser.add_argument('-k', '--key',
                    help='The setup key provided for manually configuring the authenticator app',
                    type=str)

args: Namespace = parser.parse_args()

if args.key is not None:
    key = args.key
else:
    print("next time you can use like this: ")
    print(help)
    key = input("Paste the setup key here: ")


print("-------------------------------------")
print("Your verification code is down below")
print("")
print("ATTENTION!!!")
print("Your two-factor secret is: ", key)
print("Your two-factor secret is: ", key)
print("Your two-factor secret is: ", key)
print("")
print("PLEASE KEEP IT SAFE")
print("You can take down the key to a piece of paper,")
print("and keep it for future use.")
print("")
print("Your verification code is down below")
print("the code is generated every 30 seconds")
print("press Ctrl+C to exit")
print("")

totp = pyotp.TOTP(key)

while True:
    print(totp.now())
    time.sleep(30)


