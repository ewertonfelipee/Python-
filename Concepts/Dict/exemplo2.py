notebook = {
    'cpu' : 'i5 11300h',
    'gpu' : 'gtx 1650',
    'ram' : 'ddr4 8gb',
    'ssd' : '512gb pcie'
}

print(f"A configuração do notebook é {notebook}")

notebook['ssd'] = '1tb nvme'

print(f"A configuração do notebook após a melhoria é {notebook}")

notebook['tela'] = '15.6 inches'

print(f"A configuração do notebook após a segunda melhoria é {notebook}")

notebook.update({'gpu' : '1660 super', 'cpu' : 'i9 12900k'})

print(f"Novas configs do notebook {notebook}")