# myfunc(10)
# myfunc()
# myfunc(10,20,30,40,50,60,70)

def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

myfunc(10,20,30,40,50,60,70)
myfunc(10)
myfunc()

values = [1,2,3,5,7,11]
myfunc(values)
myfunc(*values)

def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

myfunc2(a=10, b=20)
myfunc2()
myfunc2(a=10, b=20, c=30, d=40, e=50, f=60)


def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()

myfunc3()
myfunc3(1,2,3)
myfunc3(a=10, b=20, c=30)
myfunc3(1,2,3, a=10, b=20, c=30)
