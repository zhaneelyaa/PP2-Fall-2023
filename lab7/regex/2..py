import re
my_string = input('enter a string ')
p = re.compile('ab{2,3}?')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')
