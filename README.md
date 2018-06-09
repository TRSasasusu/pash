# qpsh (Quick Python Shell commands)
Call shell commands from python shell quickly.

## Installation
```sh
pip install qpsh
```

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

### Pipe
```python
>>> cat('hello.c | grep printf')
    printf("hello\n");

>>>
```

### Alias
```python
>>> cat('~/.bashrc')
alias la='ls -a'

>>> echo('spam > .spam')
>>> ls
a.out
hello.c


>>> la
.
..
.spam
a.out
hello.c


>>> cat('.spam')
spam

>>>
```
