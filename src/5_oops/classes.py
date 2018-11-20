class Simple():
    pass

simple = Simple()
print(simple)
print(type(Simple))
print(type(simple) == Simple)

class Person():
    name = "Raj"

person1 =  Person()
print(person1.name)
person1.name = "Priya"
print(person1.name)
person1.surname = "Katipally"
print(person1.surname)
print(Person.name)
del person1.name
print(person1.name)

class Square():
    radius = 10
    def calc(self, num):
        return self.radius*num

    def price(self, num):
        return self.radius*num

square = Square()
print(square.calc(2))
square.radius = 20
print((Square.calc(square, 5)))
print(square.price(10))