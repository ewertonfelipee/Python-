import random

def hit_the_number():
    
    answer = random.randint(1, 10)
    
    attempt = 0
    
    print("generate choice:")
    
    shoot = 0
    
    while shoot != answer:
        
        attempt = attempt + 1
        
        shoot = int(input())
        
        if(shoot > answer):
            print("you loose. your shoot was", shoot)
        elif(shoot < answer):
            print("you loose. your shoot was", shoot)
        else:
            print("you wins. your shoot was", answer)

while True:
    hit_the_number()
    break