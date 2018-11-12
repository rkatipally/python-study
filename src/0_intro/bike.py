class Bike:
    def __init__(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material
    def brake(self):
        print('Braking!!' + self.color)

red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')


print(red_bike.color)
print(red_bike.frame_material)
red_bike.brake()