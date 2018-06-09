# coding: utf-8

import subprocess
from .find_exe import find_exe


class Command:
    def __init__(self, command):
        self.command = command

    def __repr__(self):
        return qpsh(self.command, True)

    def __call__(self, arg, get_return=False):
        return qpsh('{} {}'.format(self.command, arg), get_return)


def qpsh(command, get_return=False):
    result = subprocess.run(command.split(' '), stdout=subprocess.PIPE).stdout.decode('utf8')
    if get_return:
        return result
    print(result)


for command in find_exe():
    try:
        exec('{command} = Command("{command}")'.format(command=command))
    except:
        print(command)
        import sys
        print(sys.exc_info())
        sys.exit()
