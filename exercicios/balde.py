import random

CAPACIDADE_MAX_BALDE = 1000

balde = 0

while balde <= CAPACIDADE_MAX_BALDE:
    volume_copo = random.randint(95, 100)

    print(f'O copo foi enchido com {volume_copo}mls')

    balde += volume_copo

    print(f'\nO volume do balde é de {balde}mls')

print(f'\nO volume do balde passou a capacidade max de {CAPACIDADE_MAX_BALDE}mls e esta com {balde}mls')