# qpsh (Quick Python Shell commands)
Call shell commands from python shell quickly.

## Usage
```python
$ python
>>> from qpsh import *
>>> ls
bar


>>> ls('-F')
bar/

>>> pwd
/foo


>>> cd('bar')
/foo/bar
>>> ls
hello.c


>>> cat('hello.c')
#include <stdio.h>

int main() {
    printf("hello\n");
    return 0;
}

>>> gcc('hello.c')
>>> ls
a.out
hello.c


>>> qpsh('./a.out')
hello

>>>
```
