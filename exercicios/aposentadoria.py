age = int(input("Digite sua idade: "))
gender = input("Digite seu gênero: ")

if gender.upper() == "M":
    if age >= 65:
        print("Aposentadoria concedida")
    else:
        print(f'Sua aposentadoria ficará disponível em {65 - age} anos')

elif gender.upper() == "F":
    if age >= 60:
         print("Aposentadoria concedida")
    else:
        print(f'Sua aposentadoria ficará disponível em {60 - age} anos')

else:
    print("Opção inválida")