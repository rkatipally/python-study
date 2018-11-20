from time import time


def do_test():
    mx = 5000
    t = time()  # start time for the for loop
    dmloop = []
    for a in range(1, mx):
        for b in range(a, mx):
            dmloop.append(divmod(a, b))
    print('for loop: {:.4f} s'.format(time() - t))  # elapsed time
    t = time()  # start time for the list comprehension
    dmlist = [
        divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
    print('list comprehension: {:.4f} s'.format(time() - t))
    t = time()  # start time for the generator expression
    dmgen = list(
        divmod(a, b) for a in range(1, mx) for b in range(a, mx))
    print('generator expression: {:.4f} s'.format(time() - t))
    # verify correctness of results and number of items in each list
    print(dmloop == dmlist == dmgen, len(dmloop))


do_test()

def do_map():
    t = time() # start time for the for loop
    mx = 2 * 10 ** 7
    t = time()
    absloop = []
    for n in range(mx):
        absloop.append(abs(n))
    print('for loop: {:.4f} s'.format(time() - t))
    t = time()
    abslist = [abs(n) for n in range(mx)]
    print('list comprehension: {:.4f} s'.format(time() - t))
    t = time()
    absmap = list(map(abs, range(mx)))
    print('map: {:.4f} s'.format(time() - t))
    print(absloop == abslist == absmap)

do_map()