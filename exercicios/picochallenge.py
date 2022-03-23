
string = input("digite seu nome: ")
for i in range(100, 110):
    print(string)
    print(i)
print("\n")
for i in range(10):
    print(i)
    
# so far == ate o momento
print("\n")
for i in range(100):
    if(i < 10):
        print("The following number is less than 10")
    elif(i >= 10 and i <= 50):
        print("The following number is greater or equal than 10 and lesser or equal than to 50")
    else:
        print("The following number is greater than 50")
    print(i)