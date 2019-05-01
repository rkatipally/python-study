def func(a,b,c):
    print(a,b,c)

func(1,2,3)
func(a=3, c=7, b=4)


def func(a, b = 10, c = 20):
    print(a,b,c)

func(1)
func(a=3)
func(a=3, b=5)
func(30, c=90)

print("===========Variable arguments===========")
def min(*n):
    print(n)
    if n:
        min = n[0]
        for value in n[1:]:
            if value < min:
                min = value
        print("Minimum is ", min)


min(1, 2, 3, -5)
min()

def args(*n):
    print(n)

values = (1,2,3,4)
args(values)
args(*values)

print("============Variable keyword arguments==========")

def args(**options):
    print(options)
args(a = 1, b = 2)

print("=========Function arguments=========")

def func(a, b, c, d = 10, *e, **f):
    print(a, b, c, d, e, f)
func(1,2,3)
func(1,2,3,4)
func(1,2,3,4,5,6)
func(1,2,3,4,5,6,7)
func(1,2,3,4,5,6,7, x=8,y=9)
func(1,2,3,4, *(5,6,7), **{'x':8, 'y':9})

print("="*10, "Mutable Default Values", "="*10)

def defaults(a=[], b={}):
    print(a,b)
    a.append(len(a))
    b[len(b)] = len(b)

defaults()
defaults()
defaults()
defaults([1,2], {'a':1})
defaults()

print('='*100)
def args1(a,b,c):
    print(a,b,c)

values = (1,2,3)
args1(*values)
