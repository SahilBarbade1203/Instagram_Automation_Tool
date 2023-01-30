class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Car(Vehicle):
    def __init__(self,ID):
        super().__init__(ID, 234, 234)
        self.seat = 5

    def reduce_seat(self):
        self.seat = self.seat - 1

    def check(self):
        if self.seat == 0:
            return False
        else:
            return True

    def vacancy(self):
        self.seat = self.seat + 1


class Bus(Vehicle):
    def __init__(self):
        super().__init__("BUS", 34 , 200)
        self.seatb = 25
        self.standb = 15

    def reduce_seatbus(self):
        self.seatb = self.seatb -1

    def reduce_standbus(self):
        self.standb = self.standb -1

    def check(self):
        if self.standb == 0:
            return "S"
        elif self.standb != 0 and self.seatb == 0:
            return "A"
        else:
            return "H"

    def filling_stand(self):
        self.standb = self.standb + 1

    def filling_seat(self):
        self.seatb = self.seatb + 1
