class Car():
	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def getdescriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		print("this car has " + str(self.odometer_reading) + " miles on it.")
		
#mynewcar = Car('audi', 'a4', 2016)
#print(mynewcar.getdescriptive_name())
#mynewcar.read_odometer()

# MODOFICANDO VALOR DE ATRIBUTOS
# MODOFICANDO O VALOR DE UM ATRIBUTO DIRETAMENTE

#mynewcar.odometer_reading = 23
#mynewcar.read_odometer()

# MODIFICANDO O VALOR DE UM ATRIBUTO COM UM METODO

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("you can't roll back an odometer!")
		
mynewcar = Car('audi', 'a4', 2016)
print(mynewcar.getdescriptive_name())
mynewcar.update_odometer(23)
mynewcar.read_odometer()
