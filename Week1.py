from vechicles import Car
from vechicles import Bus
import random

list = [Car(1), Car(2)]
bus = Bus()
while (True):
    s = input("YOUR COMMAND?")

    if s == "A":

        for item in list:
            if item.check():
                item.reduce_seat()
                print(f"Seat alloted in car{item.name}")
                break
            elif item.name == 2:
                print("No seat available.\nVisit next time")
            else:
                continue

    if s == "B":

        if bus.check() == "H":
            bus.reduce_seatbus()
            print("Passenger is alloted a seating seat in bus")

        elif bus.check() == "A":
            bus.reduce_standbus()
            print("Passenger is alloted a standing seat in bus")

        else:
            print("No seat is alloted to passenger\nVisit next time.")




    if s == "C":
        a = random.random()*10
        if a<=6:
            if bus.seatb == 25:
                print("No passenger removed")
            elif bus.check() == "H":
                bus.filling_seat()
                print("Passenger removed from seating ones of bus")
            elif bus.check() == "A" or bus.check() == "S":
                bus.filling_stand()
                print("Passenger removed from standing ones of bus")

        elif a<=8:
            if list[0].check():
                list[0].vacancy()
                print(f"Passenger removed from car{list[0].name}")
            else:
                print("No passenger removed")

        else:
            if list[1].check():
                list[1].vacancy()
                print(f"Passenger removed from car{list[1].name}")
            else:
                print("No passenger removed")

