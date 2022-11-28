# Modelando um computador

class computador:
	def __init__(self, marca, memoria, placa):
		self.marca = marca
		self.memoria = memoria
		self.placa = placa
		
	def ligar(self):
		print('estou ligando')
		
	def desligar(self):
		print('estou desligando')
		
	def informacoesdocomputador(self):
		print(self.marca, self.memoria, self.placa)
		
comp = computador('asus', '16gb', 'nvidia')
comp.ligar()
comp.desligar()
comp.informacoesdocomputador()
