from car import Car

class Uber_Van(Car):
    type_car_accepted=[]
    seat_material=[]

    def __init__(self, license,driver,type_car_accepted,seat_material):
        super().__init__(license,driver)
        self.type_car_accepted=type_car_accepted
        self.seat_material=seat_material
