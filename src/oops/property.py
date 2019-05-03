class Person:
    def __init__(self, age):
        self.age = age
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

person = Person(10)
print(person.get_age())
person.set_age(20)
print(person.get_age())

class PersonPythonic:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 18 and age < 100:
            self._age = age
        else:
            raise ValueError('Value must be between [18,99]')


person = PersonPythonic(10)
print(person.age)
person.age = 20
print(person.age)
person.age = 110

