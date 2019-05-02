class CharInputTester:
    def __init__(self):
        print('CharInputTester is created')

    def start(self):
        user_dict = {}

        while True:
            name = input('Please enter your name:\n')
            print('Your name is ' + name)
            age = input('Please enter your age:\n')
            while True:
                if not age.isdigit():
                    print('You have entered an invalid age, please enter valid input\n')
                    age = input('Please enter your age:\n')
                else:
                    print('Your age is ' + age)
                    break

            user_dict.setdefault(name + ' (' + str(age) + ')', 100-int(age))
            to_continue = input('Do you want to continue? (Y/N):\n')
            if to_continue.upper() != 'Y':
                break

        for k, v in user_dict.items():
            print(k + ' needs ' + str(v) + ' more years to hit a century!')


char_input_tester = CharInputTester()
char_input_tester.start()


