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
# range parameters
# 1-inicio da sequencia
# 2-ultimo da sequencia
#	ultimo numero - 1
# 3-de quanto em quanto a sequencia sera incrementada
for i in range(0, 256, 2):
	print(i)
