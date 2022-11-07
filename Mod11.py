# tehtävät 11.1

class Publication:
    def __init__(self, name):
        self.name = name
    def print_info(self):
        print(f"{self.name}")

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages
    def print_info(self):
        super().print_info()
        print(f"Kirjailija: {self.author}, sivuja: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja: {self.editor}")

pub1 = Magazine("Aku Ankka", "Aki Hyyppä")
pub2 = Book("Hytti n:o 6", "Rosa Liksom", 200)
pub1.print_info()
pub2.print_info()


# tehtävät 11.2

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

class ElectricCar(Car):
    def __init__(self, reg_number, top_speed, battery_capacity):
        super().__init__(reg_number, top_speed)
        self.battery_capacity = battery_capacity

class RegularCar(Car):
    def __init__(self, reg_number, top_speed, gas_tank):
        super().__init__(reg_number, top_speed)
        self.gas_tank = gas_tank

car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = RegularCar("ACD-123", 165, 32.3)
car1.accelerate(100)
car2.accelerate(100)
car1.drive(3)
car2.drive(3)
car1.print_info()
car2.print_info()


# tuntiesimerkki

'''class Vehicle:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance = 0

    def accelerate(self):
        self.speed += 1

    def print_info(self):
        print(f"{self.name}n nopeus: {self.speed}, matka: {self.distance}")

class Bike(Vehicle):
    def __init__(self, name, gears):
        super().__init__(name)
        self.gears = gears
    def print_info(self):
        super().print_info()
        print(f"vaihteita: {self.gears}")

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.gas_tank = 30
    def accelerate(self):
        super().accelerate()
        self.speed += 5
        self.gas_tank -= 1
    def print_info(self):
        super().print_info()
        print(f"bensaa tankissa: {self.gas_tank}")

vehicle1 = Car("ralliauto")
vehicle1.accelerate()
vehicle1.print_info()
vehicle2 = Bike("jopo", 5)
vehicle2.accelerate()
vehicle2.print_info()'''