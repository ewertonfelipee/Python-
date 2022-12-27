# paramentros nomeados

def monta_pc(cpu, memory, ssd, *args, monitor=27, **kwargs): # **kwargs serve para colocar parametros nomeados variáveis
    print('O computador montado foi: ')
    print(f'\tCPU: {cpu}')
    print(f'\tMemória: {memory}')
    print(f'\tSSD: {ssd}')
    print(f'\tAcessórios: {args}')
    print(f'\tMonitor: {monitor} polegadas')
    print(f'\tPeriféricos: {kwargs}')

    chaves = kwargs.keys()
    for chave in chaves:
        print(f'\tChave: {chave}')

    valores = kwargs.values()
    for valor in valores:
        print(f'\tValor: {valor}')

    for item in args:
        print(f'Iterando sobre Acessórios: {item}')


monta_pc('i7', 16, 2, 'gabinete', 'fonte', monitor=25, webcam='Logitech', teclado='Razer')
# monta_pc(memory='16 GB', ssd='1 GB', cpu='i7') # nao importa a ordem