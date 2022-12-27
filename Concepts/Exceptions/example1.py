def exp(num1, num2):
    return f'{num1 / num2:.2f}'


try:
    number1 = float(input("Number 1: "))
    number2 = float(input("Number 2: "))
    result = exp(number1, number2) # a chamada da função deve ficar dentro do try

except NameError:
    print("Error: erro de nome não suportado")


except TypeError:
    print("Error: erro de tipo não suportado")


except ZeroDivisionError:
    print("ERROR: Divisão por 0 não suportada")


else:
    print(f'O resultado da divisão é: {result}')
    print("Tudo certo com a divisão")


finally:
    print("Finalizando...")