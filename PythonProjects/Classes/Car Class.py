class Car:
    def __init__(self, year, make, colour, max_speed):
        self.year = year
        self.make = make
        self.colour = colour
        self.max_speed = max_speed
        self.speed = 0
        self.mileage = 0

    def set_year(self, year):
        self.year = year

    def set_make(self, make):
        self.make = make

    def set_speed(self, speed):
        self.speed = speed

    def get_year(self):
        return self.year

    def get_make(self):
        return self.make

    def get_speed(self):
        return self.speed

    def get_mileage(self):
        return self.mileage

    def accelerate(self, acceleration):
        if self.speed + acceleration > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += acceleration
        return self.speed

    def brake(self, brake):
        if self.speed - brake < 0:
            self.speed = 0
        else:
            self.speed -= brake
        return self.speed

    def stop(self):
        self.speed = 0

    def horn(self):
        return 'Beep Beep'

    # def mileage(self, ):
    #     while self.speed > 0:
    #         if


jade_Car = Car(2019, 'Ford', 'Teal', 150)
jen_Car = Car(2020, 'aaa', 'Blue', 170)
print(f"Jade's car is currently going {jade_Car.speed} mph")
jade_Car.accelerate(160)
jen_Car.accelerate(20)
print(f"Jade car is currently going {jade_Car.get_speed()} mph")
print(f"Jen car is currently going {jen_Car.get_speed()} mph")
jade_Car.accelerate(70)
print(f"Jade car is currently going {jade_Car.get_speed()} mph")
jade_Car.set_year(1999)
jade_Car.stop()
print(jade_Car.get_speed())
