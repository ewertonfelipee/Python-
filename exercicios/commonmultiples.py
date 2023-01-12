# common multiples of 4 and 5 in list of 0 until 500

result = [number for number in range(0,501) if number % 4 == 0 and number % 5 == 0]

print(result)
