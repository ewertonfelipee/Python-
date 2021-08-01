# greater number

def greater():
    # Below line read inputs from user using map() function
    g = list(map(int, input().split()))
    # max() function take the greater number in a sequence
    greaternumber = max(g)
    
    print(greaternumber, 'eh o maior')
    
greater()
