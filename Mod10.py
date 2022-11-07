# tehtävät 10.1-3

class Lift:
    def __init__(self, bottom_floor, highest_floor):
        self.bottom_floor = bottom_floor
        self.highest_floor = highest_floor
        self.current_floor = self.bottom_floor
#        print(f"Hissi numero {Building.lifts[]} on {self.current_floor}. kerroksessa")

    def move_up(self):
        self.current_floor += 1
        print(f"Hissi on {self.current_floor}. kerroksessa")

    def move_down(self):
        self.current_floor -= 1
        print(f"Hissi on {self.current_floor}. kerroksessa")

    def next_floor(self, floor):
        if self.current_floor < floor:
            for i in range(floor - self.current_floor):
                Lift.move_up(self)
            return
        if self.current_floor > floor:
            for i in range(self.current_floor - floor):
                Lift.move_down(self)
            return


class Building:
    def __init__(self, bottom_floor, highest_floor, lifts):
        self.bottom_floor = bottom_floor
        self.highest_floor = highest_floor
        self.lifts = []
        for i in range(lifts):
            self.lifts.append(Lift(bottom_floor, highest_floor))
#        print(f"Talossa on {len(self.lifts)} hissiä")

    def lift_drive(self, lift_number, destination_floor):
        self.lift_number = Building.lifts[lift_number]
        Lift.next_floor(destination_floor)

#    def fire_alarm(self):

'''lift1 = Lift(1, 10)
lift1.next_floor(10)
lift1.next_floor(1)'''
building1 = Building(1, 10, 3)
building1.lift_drive(3, 5)
