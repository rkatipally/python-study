def show_for_loop():
    for num in [1,2,3,10]:
        print(num)
    for num in range(5):
        print(num)
    for num in range(10, -10, -2):
        print(num)
    names = ['Raj', 'Priya', 'Somebody']
    for name in names:
        print(name)
    for position, name in enumerate(names):
        print(position, name)
    for position, name in enumerate(names,5):
        print(position, name)
    print("======Using Zip======")
    ages = [25,30,40]
    for name, age in zip(names, ages):
        print(name, age)
    nationalities = ['USA', 'India', 'Germany']
    for name, age, nationality in zip(names, ages, nationalities):
        print(name, age, nationality)
    for data in zip(names, ages, nationalities):
        name, age, nationality = data
        print(name, age, nationality)
    persons = zip(names, ages)
    for person in persons:
        if person[1] > 40:
            break
    else:
        print("No one is above 40")


def show_while():
    num = 39
    remainders = []
    while(num > 0):
        #remainders.append(num%2)
        #num //= 2
        num, remainder = divmod(num, 2)
        remainders.append(remainder)
    print("Remainders-", remainders)
    print("Binary code-", remainders[::-1])


show_for_loop()
show_while()


def get_prime_numbers():
    limit = 50
    prime_numbers = [2]
    for num in range(3, 50):
        for div in range(2,num):
            if num % div == 0:
                break
        else:
            prime_numbers.append(num)
    print("Prime numbers::", prime_numbers)

get_prime_numbers()

from itertools import count
def show_itertools():
    print("==========IterTools=========")
    for num in count(5,3):
        print(num)
        if num > 20:
            break


show_itertools()

from itertools import compress

def show_compress():
    print("========Compress========")
    data = range(10)
    even_selector = [1,0]*10
    odd_selector = [0,1]*10
    even_numbers = list(compress(data, even_selector))
    odd_numbers = list(compress(data, odd_selector))
    print(even_selector)
    print(odd_selector)
    print(even_numbers)
    print(odd_numbers)
    test_compress = list(compress('ABC', [5,5,3]))
    print(test_compress)


show_compress()

from itertools import permutations


def show_permutations():
    print("===============Permutations============")
    print(list(permutations('ABC')))


show_permutations()