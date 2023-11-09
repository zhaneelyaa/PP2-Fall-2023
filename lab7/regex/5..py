import re
# with open('row.txt', 'r') as file:
#      text = file.read()
text=input()
tx = re.findall(r"a.*b$", text)
print(tx)
