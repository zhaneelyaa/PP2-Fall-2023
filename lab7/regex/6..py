import re
text=input()
with open('row.txt', 'r') as file:
    text = file.read()
tx=re.sub("[ ,.]","|",text)
print(tx)