# def evenorodd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# #drive code to call the function
# x = int(input())
# evenorodd(x)
#################################################

#DEFAULT ARGUMENTS

# def myfunc(x, y = 50):
#     print("x: ", x)
#     print("y: ", y)
    
# myfunc(10)
##################################################

# KEYWORD ARGUMENTS

# def student(firstname, lastname):
#     print(firstname, lastname)
    
# student(firstname='ewerton', lastname='felipe')
##################################################

# DOCSTRING

# def evenodd(x):
#     """Docstring will show the that is here"""
#     if(x % 2 == 0):
#         print("even")
#     else:
#         print("odd")

# x = int(input())
# evenodd(x)
# print(evenodd.__doc__)