from operator import itemgetter
from collections import namedtuple, defaultdict, ChainMap
import dis, timeit
def showMutable():
    print("==========Lists===========")
    list_0 = []
    list_1 = [1,2,3]
    list_tuple = [(1,2), (2,3), (4,-1), (2,5)]
    list_str = list('hello')
    list_from_tuple = list((1,2,3))
    print(list_0)
    print(list_tuple)
    print(list_str)
    print(list_from_tuple)
    print([x + 5 for x in [2, 3, 4]])

    print("========List operations=========")
    print("Append to list-", list_1.append(4)) # returns none
    print("counting occurrences- ", list_1.count(3))
    print('Extend the list with list -', list_1.extend([5,7])) # returns none
    print(list_1)
    print('Inserting into list-', list_1.insert(3,3))
    print(list_1)
    print('remove an elemnent using pop from list-', list_1.pop())
    print('remove an element using pop at position-', list_1.pop(5))
    print(list_1)
    print('remove an element using remove function', list_1.remove(2))
    print(list_1)
    print('reverse a list-', list_1.reverse())
    print(list_1)
    print('sort a list-', list_1.sort())
    print(list_1)
    print('min-', min(list_1))
    print('max-', max(list_1))
    print('sum-', sum(list_1))
    # Error, not allowed print('sum with hetro elements-', sum[1,'d',4, (5,6)])
    # print('sum with hetro elements-', sum([1,4]))
    print('list concatenation-', list_1+list_from_tuple)
    print(list_1)
    print('multiply list-', list_1*2)
    print('===========Sorting tuple list==============')
    print('sorting tuple list-', sorted(list_tuple))
    print('sorting tuple list with key and itemgetter-', sorted(list_tuple, key= itemgetter(0)))
    print('sorting tuple list with key and itemgetter-', sorted(list_tuple, key= itemgetter(0,1)))
    print('sorting tuple list with key and itemgetter-', sorted(list_tuple, key= itemgetter(1)))
    print('sorting tuple list with key and itemgetter with reverse -', sorted(list_tuple, key= itemgetter(0), reverse=True))
    print('clear a list-', list_1.clear())
    # Not allowed print('Extend the list with list -', list_1.extend(4))
    print(list_1)

    print("====================Byte Array============")
    b_array = bytearray()
    print('Empty byte array-', b_array)
    print('10 length byte array-', bytearray(10))
    print('Range byte array-', bytearray(range(5)))
    print('Byte array from value -', bytearray(b'Raj'))
    print('EndsWith on byte array-', bytearray(b'Raj').endswith(b'aj'))
    print('Count on byte array-', bytearray(b'Raj').count(b'a'))
    print('Upper on byte array-', bytearray(b'Raj').upper())

    print("===================Set=======================")

    small_primes = set()
    small_primes.add(2)
    small_primes.add(3)
    small_primes.add(5)
    small_primes.add(2)
    print("set- small_primes-", small_primes)
    print("Remove an element-", small_primes.remove(2))
    print(small_primes)
    print("membership test-", 3 in small_primes)
    # Faster creation
    big_primes = set([11,13,17,19]) # can also be string literal {11,13,17,19}
    print("set union-", small_primes | big_primes)
    print('small_promes after union-', small_primes)
    print("intersection-", small_primes & big_primes)
    print("difference", small_primes - big_primes)

    print("===================frozenSet=======================")

    small_primes = frozenset([2,3,5,7])
    big_primes = frozenset([11,13,17,19])
    # not allowed small_primes.add(2)
    # not allowd small_primes.remove(2)
    diff_frset = small_primes | big_primes
    # not allowed diff_frset.add(1)
    print('frozenSet union-', small_primes | big_primes)
    print('frozenSet intersion-', small_primes & big_primes)
    print('frozenSet difference-', small_primes - big_primes)

    print("================Dictionary====================")

    a = dict(A=1, Z=-1)
    b = {'A':1, 'Z':-1}
    c = dict(zip(['A','Z'], [1,-1]))
    d = dict([('A', 1), ('Z', -1)])
    e = dict({'Z':-1, 'A':1})
    print("Different ways to create dictionary-", a == b == c == d == e)
    print("Range-", range(1,4))
    print("zip-", list(zip('hello', range(1,6))))
    print("zip-uneven", list(zip('hello', range(1,7))))

    dict_1 = {}
    dict_1['a'] =1
    dict_1['b'] = 2
    print("Dictionary dict_1-",dict_1)
    print("check key in dict_1", 'a' in dict_1)
    print("Delet from dict_1-")
    del dict_1['a']
    print("check key in dict_1", 'a' in dict_1)
    print("Clear dictionary-", dict_1.clear())
    dict_2 = dict(zip('hello', range(1,6)))
    print("keys-", dict_2.keys())
    print("Items-", dict_2.items())
    print("Values-", dict_2.values())
    print("Check exists on item-", ('h', 1) in dict_2.items())
    print("PopItem-", dict_2.popitem())
    print("PopItem by key-", dict_2.pop('h'))
    print("Update dict-", dict_2.update({'h': 6}))
    print("Update dict-", dict_2.update(c = 8))
    print("Get value-", dict_2.get('h'))
    print("Get with default value-", dict_2.get('b', 200))
    print("Get with non-key-", dict_2.get('b'))
    print("SetDefault -", dict_2.setdefault('h',10))
    print("SetDefault -", dict_2.setdefault('x',100))
    d = {}
    d.setdefault(1, {}).setdefault(2,[]).append('a')
    print(d)
    print(dict_2)
    print("=========Named Tuple=============")

    Vision = namedtuple('Vision', ['left', 'right'])
    vision = Vision(10,20)
    print("NamedTuple-", vision.left, vision.right)
    Vision =  namedtuple('Vision', ['left', 'combined', 'right'])
    vision = Vision(10,15,20)
    print("NamedTuple-", vision.left, vision.right)

    print("==========DefaultDict==============")
    default_dict = defaultdict(int)
    print(default_dict)
    default_dict['age'] += 1
    print(default_dict)

    print("=========ChainMap============")

    default_connection = {'host': 'localhost', 'port': 4657}
    connection = {'port': 5050}
    conn = ChainMap(default_connection, connection)
    print(conn['port'])
    print(conn['host'])
    print(conn.maps)
    #del conn['port']
    print(dict(conn))
    return None

showMutable()
#dis.dis(showMutable)
min(timeit.repeat(showMutable, 5))
