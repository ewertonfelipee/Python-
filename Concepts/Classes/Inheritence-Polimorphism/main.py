import time
import random

VALUE_TOLL_CAR = 3.75
VALUE_TOLL_MOTO = 1.50

VALUE_KM_TRAVELED_CAR = 3.00
VALUE_KM_TRAVELED_MOTO = 2.25

class Auto:
    def __init__(self, manufacturer, model, rented):
        self.manufacturer = manufacturer
        self.model = model
        self.rented = rented
        self.bill_value = 0
        self.client_name = ""
        print(f'Automobile {self.manufacturer} {self.model} acquired by rental company')

    def rent(self, client_name):
        self.rented = True
        self.client_name = client_name
        print(f'the car {self.manufacturer} {self.model} was rented by {self.client_name}')

    def return_car(self):
        self.rented = False
        print(f'the car {self.manufacturer} {self.model} was returned by {self.client_name}')
        #self.client_name = ""

    def generate_bill(self, number_toll, km_traveled): # método abstrato
        raise NotImplementedError # quem herdar esse método tem obrigação de implementá-lo

# c = Auto('honda', 'civic', True)
# c.rent('John Doe')
# c.return_car()

class Car(Auto): # Inhiritence

    def __init__(self, manufacturer, model, rented):
        super(Car, self).__init__(manufacturer, model, rented)
        print('The auto acquired was car')

    def generate_bill(self, number_toll, km_traveled):
        self.bill_value = number_toll * VALUE_TOLL_CAR + km_traveled * VALUE_KM_TRAVELED_CAR
        print(f'Bill\'s car {self.manufacturer} {self.model} generate with success. Value R${self.bill_value}')

class Motocycle(Auto):

    def __init__(self, manufacturer, model, rented):
        super(Motocycle, self).__init__(manufacturer, model, rented)
        print('The auto acquired was moto')

    def generate_bill(self, number_toll, km_traveled):
        self.bill_value = number_toll * VALUE_TOLL_MOTO + km_traveled * VALUE_KM_TRAVELED_MOTO
        print(f'Bill\'s moto {self.manufacturer} {self.model} generate with success. Value R${self.bill_value}')

def show_bill(Auto):
    print(f'The bill value of {Auto.manufacturer} {Auto.model} rented by {Auto.client_name} is R${Auto.bill_value}')


fiesta = Car('Honda', 'Civic', False)
fiesta.rent('John Doe')

# Simulation rent time
time.sleep(random.randint(7,10))

fiesta.return_car()

fiesta.generate_bill(number_toll = 5, km_traveled = 900)

show_bill(fiesta)