def salaryy_bonuses():
    
    noame = input()
    fixed_salary = float(input())
    total_sales = float(input())
    
    total = fixed_salary + (total_sales*(15/100))
    
    print("TOTAL = R$ {0:2.2f}".format(total))

salaryy_bonuses()