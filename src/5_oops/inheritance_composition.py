class Engine():
    def start_engine(self):
        print("Engine started", self)
    def stop_engine(self):
        print("Engine stopped", self)

class Car():
    #engine_ = Engine() # belongs to class
    def __init__(self):
        self.engine_ = Engine() #belongs to instance of the class
    def start(self):
        self.engine_.start_engine()
    def stop(self):
        self.engine_.stop_engine()


car = Car()
car.start()
car.stop()

car = Car()
car.start()
car.stop()

class RaceCar(Car):
    engine_ = Engine()
    def __init__(self):
        print(self)

race_car = RaceCar()
race_car.start()
race_car.stop()

class F1Car(RaceCar):
    pass

def check_classes():
    car = Car()
    race_car = RaceCar()
    f1_car = F1Car()
    cars = [(car, 'Car'), (race_car, 'RaceCar'), (f1_car, 'F1Car')]
    class_types = [Car, RaceCar, F1Car]

    def is_instance():
        for instance, name in cars:
            for class_type in class_types:
                belongs = isinstance(instance, class_type)
                msg = 'Is a' if belongs else 'Is not  a'
                print(name, msg, class_type.__name__)
    def is_subclass():
        for class_1 in class_types:
            for class_2 in class_types:
                is_sub = issubclass(class_1, class_2)
                msg = '{0} a subclass of'.format('Is' if is_sub else 'Is not ')
                print(class_1.__name__, msg, class_2.__name__)
    return (is_instance(), is_subclass)

check_classes()
check_classes()[1]()
