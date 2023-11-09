import re
text = input()
# with open('row.txt', 'r') as file:
#      text = file.read()
tx = re.sub(r"(\w)([A-Z])", r"\1 \2",text)
print(tx)
