# def args_function(arg1, arg2, *args):
#     print(arg1)
#     print(arg2)
#     print(args)

# args_function(5, 6, 6.5, 'hi')

def soma(maximum: int, *numbers: float) -> float:
    result = 0

    numbers_sum = []

    for number in numbers:

        if(result + number) > maximum:
            break

        result += number
        numbers_sum.append(number)

    # print(numbers_sum)
    return result

summ = soma(100,2,3,4.9,5,20.5,50,16.3,33.7)
print(f'O resultado é: {summ}')