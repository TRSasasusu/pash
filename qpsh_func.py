# coding: utf-8

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
    result = subprocess.run(list(filter(lambda x: x != '', command.split(' '))), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
