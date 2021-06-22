name = input()

age = int(input())

if name == 'Alice' and age > 2000:
    print('hi, Alice')
    print('unlike you, alice is not undead, immortal vampire')
    
elif age < 12 and name == 'kiddo':
    print('you are not alice, kiddo')
    
elif age > 100 and name == 'grannie':
    print('you are not alice, grannie')
    
else:
    print('alice is human')