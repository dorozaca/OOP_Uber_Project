class Encapsulation:
    def __init__(self, name, age, gender):
        self.__name=name
        self.__age=age
        self.__gender=gender

        @property
        def Name(self):
            return self.__name
        
        @Name.setter
        def Name(self,value):
            self.__name=value

    @staticmethod
    def mymethod():
        print ('Hello Diego')

diego=Encapsulation('Diego',41,'m')
print(vars(diego))

diego.mymethod()

        
