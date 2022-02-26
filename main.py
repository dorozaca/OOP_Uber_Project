from car import Car
from account import Account

if __name__== '__main__':
    #print('Hello World!')
    car1=Car('GJIT24',Account('Juan Perez', '40702088'))
    car1.passenger='Diego Oroza'
    print(vars(car1))
    print(vars(car1.driver))
   
