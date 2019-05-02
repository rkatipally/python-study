class EvenOdd:
    def __init__(self):
        print('EvenOdd object is being created!!!')

    def is_even(self, num):
        if num % 2:
            return False
        return True

    def start(self):
        while(True):
            user_input = input('Please enter a number\n')
            if not user_input.isdigit():
                user_input = input('Please enter a valid number\n')
                continue
            else:
                user_input = int(user_input)
                print('Number you have entered {0} is an {1} number!'.format(user_input, 'Even' if self.is_even(user_input) else 'Odd'))

            is_continue = input('Do you want to continue?\n').upper() == 'Y'
            if is_continue:
                continue
            else:
                break


even_odd = EvenOdd()
even_odd.start()
