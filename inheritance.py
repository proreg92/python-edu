class Vehicle:
    speed = 0
    age = 0

    def move(self):
        return f'Moving with speed {self.speed}'


class Car(Vehicle):
    def __init__(self):
        # print(self.speed)
        self.speed = 10

    def move(self):
        s = super().move()
        print('Previous:', s)
        # return f'Driving car with speed {self.speed}'
        s += ' [it is a car]'
        return s


class Ship(Vehicle):
 
    def __init__(self):
        self.tubes = 3

    def sound(self):
        return f'Tu tu from {self.tubes} tubes'


class SportCar(Car):
    speed = 50

    def __init__(self):
        print('Current speed is', self.speed)
        super().__init__()
        print('And now current speed is', self.speed)
        self.speed = 70


class ECar(Car):
    charge = 50

    def state(self):
        return 'Needs charge' if self.charge < 10 else 'OK'


class PlaybackError(Exception):
    pass    


class MorePlayErrors(PlaybackError):
    pass


class SportECar(SportCar, ECar):

    def play(self):
        print('Trying to play')
        raise PlaybackError

    def play2(self):
        raise MorePlayErrors


e_car = ECar()
e_car.charge = 7
print(e_car.state())

se_car = SportECar()
print(se_car.speed, se_car.charge, se_car.state())
print(se_car.__class__)
print(isinstance(se_car, Vehicle))

try:
    se_car.play2()
except MorePlayErrors:
    print('No play 2')
except PlaybackError:
    print('No play 1')

# v = Vehicle()
# car = Car()
# ship = Ship()
# ship.tubes = 2
# s_car = SportCar()
#
# print(v.move())
# print(car.move())
# print(ship.sound())
# print(s_car.move())
# print(Car, Car.__bases__, car, car.__class__.__class__)
