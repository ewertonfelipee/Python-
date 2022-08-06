user = input('enter user name: ')
if user == 'root':
	print('logged in user with: %s' % user)
elif user == 'admin':
	print('logged in user with: %s' % user)
else: # O ":" determina o fim da linha no condicional
	print('No logged in with root')
