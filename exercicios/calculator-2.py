def calculator(num1, num2):
    return num1+num2, num1 - num2, num1 * num2, num1 / num2

number1 = int(input("Digite o primeiro numero: "))
number2 = int(input("Digite o segundo numero: "))
calc = calculator(number1, number2)
for result in calc:
    print(f'Os resultados são: {result:.1f}')