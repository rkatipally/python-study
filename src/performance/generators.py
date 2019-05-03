def get_squares():
    return [n*n for n in range(10)]
print(get_squares())

def get_squares_gen():
    for n in range(3):
        yield n*n

squares = get_squares_gen()
print(next(squares))
print(next(squares))
print(squares.__next__())
#print(next(squares)) #StopIteration exception

def do_send():
    n = 0
    while True:
        result = yield n
        print(type(result), result)
        if result == 'Q!':
            break
        n += 1

send_gen = do_send()
print(next(send_gen))
print(send_gen.send("ABC")) # can only resume the execution
print(next(send_gen))
print(next(send_gen))
#print(send_gen.send('Q!')) #Throws StopIteration
#print(next(send_gen))

def print_squares():
    yield from (n*n for n in range(5))

for n in print_squares():
    print(n)

def comp_vs_gen():
    c_list = [n*n for n in range(5)]
    print(type(c_list))
    print(list(c_list))
    g_list = (n*n for n in range(5))
    print(type(g_list))
    print(list(g_list))
    print(list(g_list))

comp_vs_gen()

def num_gen():
    num_add = map(lambda a: sum(a), zip(range(0,100), range(1,101)))
    print(list(num_add))
    num_add = (sum(n) for n in list(zip(range(0,100),range(1,101))))
    #print(next(num_add))
    #s = sum([n**2 for n in range(10**8)]) # this is killed
    s = sum(n**2 for n in range(10**8)) # this succeeds
    print(s)
num_gen()