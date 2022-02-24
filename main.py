from car import Car

if __name__== '__main__':
    #print('Hello World!')
    car1=Car()
    car1.id=4512
    car1.license='AMS234'
    car1.driver='Juan Perez'
    car1.passenger='Manuel Ramos'
    print(vars(car1))

    car2=Car()
    car2.id=4513
    car2.license='AMS237'
    car2driver='Juana Laoz'
    car2.passenger='Manny Jones'
    print(vars(car2))
