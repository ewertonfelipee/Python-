#CALCULO SIMPLES

def calc_simple():
        
        
    enter = input()
    
    numberasstring = enter.split()
    
    numbers = [float(number) for number in numberasstring]
    
    code, numberofpieces, value = numbers
    
    res = numberofpieces * value
        
    enter2 = input()
    
    numberasstring2 = enter2.split()
    
    numbers2 = [float(number2) for number2 in numberasstring2]
    
    code2, numberofpieces2, value2 = numbers2
    
    res2 = numberofpieces2 * value2
    
    result = res + res2
    
    print("VALOR A PAGAR: R$ {0:2.2f}".format(result))
    
calc_simple()