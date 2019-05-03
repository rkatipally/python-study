def show_map():
    some_list = map(lambda *a: a, range(3))
    print(some_list)
    some_list = list(map(lambda *a: a, range(3)))
    print(some_list)
    some_list = list(map(lambda *a: a*2, range(3), 'ABCD'))
    print(some_list)
    some_list = list(map(lambda *a: a, range(3), 'ABCD', range(4,8)))
    print(some_list)
    some_list = list(map(lambda *a: a, range(3), 'ABCD', range(4,8), ()))
    print(some_list)
show_map()

students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

def decorate(student):
    return (sum(student['credits'].values()), student['id'], student)
def undecorate(decorated_student):
    return decorated_student[2]

def sort():
    after_sorted = sorted(list(map(decorate, students)), reverse=True)
    print(after_sorted)
    after_undecorate = list(map(undecorate, after_sorted))
    print(after_undecorate)
sort()

def max_all():
    a = [5, 9, 2, 4, 7]
    b = [3, 7, 1, 9, 2]
    c = [6, 8, 0, 5, 3]
    return list(map(lambda n: max(*n), zip(a, b, c)))

print(max_all())

print("==============Filter===================")
def do_filter():
    test = [2, 5, 8, 0, 0, 1, 0]
    after_filter = list(filter(lambda x:x, test))
    print(after_filter)
    after_filter = list(filter(None, test))
    print(after_filter)
    after_filter = list(filter(lambda x: x>7, test))
    print(after_filter)

do_filter()