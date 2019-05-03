from math import sqrt
def do_list():
    square_list = list(map(lambda x: x*x, range(1,11)))
    print(square_list)
    square_list = [n*n for n in range(1,11)]
    print(square_list)
    filterd_list  = list(filter(lambda n: n%2, map(lambda n:n*n, range(1,11))))
    print(filterd_list)
    filterd_list = [n*n for n in range(1,11) if n%2]
    print(filterd_list)
do_list()

def nested_compr():
    items = 'ABCDE'
    tuple_list = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]
    print(tuple_list)
nested_compr()

def py_triple():
    n = 10
    legs = [(a,b, sqrt(a*a + b*b)) for a in range(1, n) for b in range(a, n)]
    print(legs)
    after_filter = list(filter(lambda triple: triple[2].is_integer(), legs))
    print(after_filter)
    print([(a,b,int(c)) for a,b,c in legs if c.is_integer()])
py_triple()
