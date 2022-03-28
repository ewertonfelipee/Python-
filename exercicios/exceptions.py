num1 = 8
print("Input the that will divide: ")
num2 = int(input())
try:
    result = num1/num2
    print(result)
except ZeroDivisionError:
    #been more specific
    print("Don't divide by zero, that is forbidden.")
except TypeError:
    print("Your input value must be an integer.")
print("The program keeps executing to do other stuff...")