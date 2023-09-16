# Simple 2FA TOTP achieved by python(CLI)

Input the secret key and then get verification code.

Especially made for Github 2FA, but can be used anywhere else as long as you are able to access secret key.

```
usage: 2FA.py [-h] [-k KEY]

options:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  The setup key provided for manually configuring the authenticator app
```

EXAMPLES:

```
hero@debian:~/2FA$ docker run -it --rm huangqizigailee/2fa
next time you can use like this:


usage: 2FA.py [-h] [-k KEY]

options:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  The setup key provided for manually configuring the authenticator app


Paste the setup key here: AAAABBBBCCCCDDDD
-------------------------------------
Your verification code is down below

ATTENTION!!!
Your two-factor secret is:  AAAABBBBCCCCDDDD
Your two-factor secret is:  AAAABBBBCCCCDDDD
Your two-factor secret is:  AAAABBBBCCCCDDDD

PLEASE KEEP IT SAFE
You can take down the key to a piece of paper,
and keep it for future use.

Your verification code is down below
the code is generated every 30 seconds
press Ctrl+C to exit

141109
723071
545819
433354
941675
783769
117562
727541
927834
^CTraceback (most recent call last):
  File "/2FA/2FA.py", line 58, in <module>
    time.sleep(timer)
KeyboardInterrupt
```

OR

```
hero@debian:~/2FA$ docker run -it --rm huangqizigailee/2fa -k AAAABBBBCCCCDDDD
-------------------------------------
Your verification code is down below

ATTENTION!!!
Your two-factor secret is:  AAAABBBBCCCCDDDD
Your two-factor secret is:  AAAABBBBCCCCDDDD
Your two-factor secret is:  AAAABBBBCCCCDDDD

PLEASE KEEP IT SAFE
You can take down the key to a piece of paper,
and keep it for future use.

Your verification code is down below
the code is generated every 30 seconds
press Ctrl+C to exit

944824
672934
046953
351288
010717
030788
904237
^CTraceback (most recent call last):
  File "/2FA/2FA.py", line 58, in <module>
    time.sleep(timer)
KeyboardInterrupt
hero@debian:~/2FA$
```
