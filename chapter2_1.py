#!/usr/bin/env python

import pexpect

devices = {'iosv-1' : {'prompt':'lax-edg-r1#', 'ip':'10.32.1.201'},
        'iosv-2': {'prompt': 'lax-edg-r2#', 'ip':'10.32.1.202'}}
username = 'cisco'
password = 'cisco'

for device in devices.keys():
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline('show version | i V')
    child.expect(device_prompt)
    print(child.before)
    child.sendline('exit')

