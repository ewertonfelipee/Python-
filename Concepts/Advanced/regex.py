import re

string = 'hello, i\'m Joe'
regex = re.search('^w.*joe$', string)

if regex: 
    print('matching')
else:
    print('Don\'t matching')