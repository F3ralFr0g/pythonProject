# tehtävät 10.1-3

class Lift:
    def __init__(self, bottom_floor, highest_floor):
        self.bottom_floor = bottom_floor
        self.highest_floor = highest_floor
        self.current_floor = self.bottom_floor

    def move_up(self):
        self.current_floor += 1
        print(f"Hissi on {self.current_floor}. kerroksessa")

    def move_down(self):
        self.current_floor -= 1
        print(f"Hissi on {self.current_floor}. kerroksessa")

    def to_floor(self, floor):
        if self.current_floor < floor:
            for i in range(floor - self.current_floor):
                Lift.move_up(self)
        if self.current_floor > floor:
            for i in range(floor - self.current_floor):
                Lift.move_down(self)


class Building:
    def __init__(self, bottom_floor, highest_floor, lifts):
        self.bottom_floor = bottom_floor
        self.highest_floor = highest_floor
        Lifts = []
        for i in range(lifts):
            Lifts.append(Lift(bottom_floor, highest_floor))

#    def lift_drive(self, lift_number, destination_floor):

#    def fire_alarm(self):

lift1 = Lift(1, 10)
lift1.to_floor(5)
lift1.to_floor(1)

