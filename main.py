from car import Car
from account import Account
from card import Card

if __name__== '__main__':
    #print('Hello World!')
    car1=Car('GJIT24',Account('Juan Perez', '40702088'))
    car1.passenger='Diego Oroza'
    mypay = Card(4512, 123, 22, 'June')
    print(vars(car1))
    print(vars(car1.driver))
    print(vars(mypay))
   
