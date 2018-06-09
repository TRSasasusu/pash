# coding: utf-8

import os
import re
import subprocess
from .find_exe import find_exe


class Command:
    def __init__(self, command):
        self.command = command

    def __repr__(self):
        return '\n'.join(qpsh(self.command, True))

    def __call__(self, arg='', get_return=False):
        return qpsh('{} {}'.format(self.command, arg), get_return)


def qpsh(command, get_return=False):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    decode = lambda x: x.decode('utf8')
    if get_return:
        return decode(result.stdout), decode(result.stderr)

    if result.stdout != b'':
        print(decode(result.stdout))
    if result.stderr != b'':
        print(decode(result.stderr))


for command in find_exe():
    try:
        exec('{command} = Command("{command}")'.format(command=command))
    except:
        print(command)
        import sys
        print(sys.exc_info())
        sys.exit()

from .cd import cd


alias = subprocess.run([os.getenv('SHELL', '/bin/bash'), '-ic', 'alias'], stdout=subprocess.PIPE).stdout.decode('utf8')
for each_alias in alias.split('\n'):
    each_alias = re.search('[0-9a-zA-Z]+=[\'\"][- 0-9a-zA-Z]+[\'\"]', each_alias)
    if each_alias is not None:
        exec('{} = Command({})'.format(*each_alias.group().split('=')))
