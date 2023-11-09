import re
text = input()
# with open('row.txt', 'r') as file:
#      text = file.read()
tx = re.sub(r"(\w)(\s)+([A-Z])", r"\1 \3",text)
print(tx)

