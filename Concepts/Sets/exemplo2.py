man = {'ewerton', 'felipe', 'john', 'victor', 'tom', 'leo', 'silva', 'augusto'}
high_income = {'ana', 'julia', 'ewerton', 'felipe', 'phillip', 'leandro'}

# print(f'Homens - conjunto 1: {man}\n')
# print(f'Alta renda - conjunto 2: {high_income}\n')

# man_high_income = man.intersection(high_income)
# print(f'Homens com alta renda: {man_high_income}\n')

# all_people = man.union(high_income)
# print(f'Todas as pessoas: {all_people}\n')

# diff = man.difference(high_income)
# print(f'A diferença dos conjuntos 1 - 2: {diff}\n')

# diff2 = high_income.difference(man)
# print(f'A diferença dos conjuntos 2 - 1: {diff2}\n')

# no_high_income_men_and_women = man.symmetric_difference(high_income) # exluci a interseção
# print(f'Homens que não são alta renda e mulheres: {no_high_income_men_and_women}\n')

# print(f'Os conjuntos de homens e alta renda são disjuntos? {man.isdisjoint(high_income)}')
# print(f'O conjunto de homens é subconjunto de alta renda? {man.issubset(high_income)}')
# print(f'O conjunto de homens é superconjunto de alta renda? {man.issuperset(high_income)}')

#intersection
print(man & high_income)

#union
print(man | high_income)

#difference
print(man - high_income)

#symmetric difference
print(man ^ high_income)