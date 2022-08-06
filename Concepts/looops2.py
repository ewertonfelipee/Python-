'''
while True:
	user = input('digite um usuario: ')
	print('O usuario digitado foi: %s' % user)
	if user == 'root':
		print('voce foi logado')
		break
'''
'''
contador = 0
while (contador < 1024):
	if contador == 256:
		continue
	print (contador)
	contador = contador + 1
'''
for i in range(0, 256, 2):
	print(i)
