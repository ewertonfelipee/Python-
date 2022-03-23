def evenorodd(x):
    if(x % 2 == 0):
        return True
    else:
        return False
if(evenorodd(int(input()))):
    print("even")
else:
    print("odd")