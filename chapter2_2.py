#!/usr/bin/env python

import getpass
from pexpect import pxssh

devices = {'lax-edg-r1': {'prompt': 'lax-edg-r1#', 'ip': '10.32.1.201'},
'lax-edg-r2': {'prompt': 'lax-edg-r2#', 'ip': '10.32.1.202'}}

commands = ['term length 0', 'show version','show run']

username = input('Username: ')
password = getpass.getpass('Password: ')

for device in devices.keys():
    outputFileName = device + '_output.text'
    device_prompt = devices[device]['prompt']
    child = pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)

    with open(outputFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)

    child.logout()
