# tehtävät 9.1-3

class Car:
    def __init__(self, reg_number, top_speed):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance = 0

    def print_info(self):
        print(f"Auton {self.reg_number} "
              f"huippunopeus on {self.top_speed} km/h, "
              f"ajettu on {self.distance} km, "
              f"tämänhetkinen nopeus on {self.current_speed} km/h.")

    def accelerate(self, speed_change):

        self.current_speed += speed_change
        if self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time):
        self.distance += (self.current_speed * time)

car1 = Car("ABC-123", 142)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.drive(1.5)
car1.print_info()
car1.accelerate(-200)
car1.print_info()


# tehtävät 9.4

import random

Cars = []
for i in range(10):
    Cars.append(Car("ABC-" + str(i+1), random.randint(100, 200)))
for Car in Cars:
    Car.print_info()

stop = False
laps = 0
while not stop:
    laps += 1

    for Car in Cars:
        Car.accelerate(random.randint(-10, 15))
        Car.drive(1)
        if Car.distance >= 10000:
            stop = True
            break

for Car in Cars:
    Car.print_info()
    print(laps)
