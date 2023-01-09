import time
import random

VALUE_TOLL_CAR = 3.75
VALUE_TOLL_MOTO = 1.50

VALUE_KM_TRAVELED_CAR = 3.00
VALUE_KM_TRAVELED_MOTO = 2.25

class Auto:
    total_locations = 0 # class atribute

    def __init__(self, manufacturer, model, rented):
        self.manufacturer = manufacturer
        self.model = model
        self.rented = rented
        self.bill_value = 0
        self.client_name = ""
        print(f'Automobile {self.manufacturer} {self.model} acquired by rental company')

    def rent(self, client_name):
        Auto.total_locations += 1 # method atribute
        self.rented = True
        self.client_name = client_name
        print(f'the {self.manufacturer} {self.model} was rented by {self.client_name}')

    def return_auto(self):
        self.rented = False
        print(f'the {self.manufacturer} {self.model} was returned by {self.client_name}')
        #self.client_name = ""

    def generate_bill(self, number_toll, km_traveled): # método abstrato
        raise NotImplementedError # quem herdar esse método tem obrigação de implementá-lo

    @classmethod
    def show_total_locations(cls):
        print(f'The total number of locations is {cls.total_locations} locations')
# c = Auto('honda', 'civic', True)
# c.rent('John Doe')
# c.return_car()

class Car(Auto): # Inhiritence
    total_locations_car = 0
    total_value_locations = 0.0

    def __init__(self, manufacturer, model, rented):
        super(Car, self).__init__(manufacturer, model, rented)
        print('The auto acquired was car')

    def rent(self, client_name):
        super(Car, self).rent(client_name)
        Car.total_locations_car += 1

    def generate_bill(self, number_toll, km_traveled):
        self.bill_value = number_toll * VALUE_TOLL_CAR + km_traveled * VALUE_KM_TRAVELED_CAR
        print(f'Bill\'s car {self.manufacturer} {self.model} generate with success. Value R${self.bill_value}')
        Car.total_value_locations += self.bill_value

    @classmethod
    def calculate_location_mean(cls):
        if cls.total_locations_car != 0:
            locations_mean = cls.total_value_locations / cls.total_locations_car
            print(f'The average value of location car\'s is R${locations_mean}')
        else:
            print(f'The total number of locations is equal zero')

class Motocycle(Auto):
    total_locations_moto = 0
    total_value_locations = 0.0

    def __init__(self, manufacturer, model, rented):
        super(Motocycle, self).__init__(manufacturer, model, rented)
        print('The auto acquired was moto')

    def rent(self, client_name):
        super(Motocycle, self).rent(client_name)
        Motocycle.total_locations_moto += 1

    def generate_bill(self, number_toll, km_traveled):
        self.bill_value = number_toll * VALUE_TOLL_MOTO + km_traveled * VALUE_KM_TRAVELED_MOTO
        print(f'Bill\'s moto {self.manufacturer} {self.model} generate with success. Value R${self.bill_value}')
        Motocycle.total_value_locations += self.bill_value

    @classmethod
    def calculate_location_mean(cls):
        if cls.total_locations_moto != 0:
            locations_mean = cls.total_value_locations / cls.total_locations_moto
            print(f'The average value of location moto\'s is R${locations_mean}')
        else:
            print(f'The total number of locations is equal zero')

def show_bill(Auto):
    print(f'The bill value of {Auto.manufacturer} {Auto.model} rented by {Auto.client_name} is R${Auto.bill_value}')


civic = Car('Honda', 'Civic', False)
civic.rent('John Doe')

# Simulation rent time
time.sleep(random.randint(3,7))

civic.return_auto()

civic.generate_bill(number_toll = 5, km_traveled = 900)

show_bill(civic)

print('\n')
print('===============================================================')
print('\n')
fiesta = Car('Ford', 'Fiesta', False)
fiesta.rent('Ewerton')

# Simulation rent time
time.sleep(random.randint(3,7))

fiesta.return_auto()

fiesta.generate_bill(number_toll = 15, km_traveled = 650)

show_bill(fiesta)

print('===============================================================')
Car.calculate_location_mean()

print('\n')
print('===============================================================')
print('\n')

cb = Motocycle('Honda', 'CB 500', False)
cb.rent('Felipe')
cb.return_auto()
cb.generate_bill(number_toll = 10, km_traveled = 860)
show_bill(cb)

print('\n')
print('===============================================================')
print('\n')

ninja = Motocycle('Kawasali', 'Ninja 600', False)
ninja.rent('Joe')
ninja.return_auto()
ninja.generate_bill(number_toll = 8, km_traveled = 420)
show_bill(ninja)

print('===============================================================')
Motocycle.calculate_location_mean()