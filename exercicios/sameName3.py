def spam():
    global eggs
    eggs = 'spam' # global variable

def bacon():
    eggs = 'bacon' # local variable
    
def ham():
    print(eggs) # global variable
    
eggs = 42 # global variable
spam()
print(eggs)

"""

output: spam

"""