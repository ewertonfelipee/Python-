# Modelando um carro

class car:
	def __init__(self, preco, cor, marca):
		self.preco = preco
		self.cor = cor
		self.marca = marca
		
	def cor_padrao(self):
		print(self.cor)
	
	def preco_padrao(self):
		print(str(self.preco))
	
	def marca_padrao(self):
		print(self.marca)
		
carro = car('red', '10000', 'bmw')
carro.cor_padrao()
carro.preco_padrao()
carro.marca_padrao()
