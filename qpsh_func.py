# coding: utf-8

import subprocess


def qpsh(command, get_return=False):
    result = subprocess.run(command.split(' '), stdout=subprocess.PIPE).stdout.decode('utf8')
    if get_return:
        return result
    print(result)
