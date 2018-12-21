class A:
    def __init__(self, name):
        self._name = name
    def a_get_name(self):
        print(self._name)

class B(A):
    def name(self, name):
        self._name = name
    def get_name(self):
        print(self._name)

b = B("A Class")
b.a_get_name()
b.name("B Class")
b.get_name()
b.a_get_name()


class A:
    def __init__(self, name):
        self.__name = name
    def a_get_name(self):
        print(self.__name)

class B(A):
    def name(self, name):
        self.__name = name
    def get_name(self):
        print(self.__name)
        print(self.__dict__)

b = B("A Class")
b.a_get_name()
b.name("B Class")
b.get_name()
b.a_get_name()

class A:
    def __init__(self, factor):
        self.__factor = factor
    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))
class B(A):
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))

obj = B(100)
obj.op1()
obj.op2(42)
obj.op1()