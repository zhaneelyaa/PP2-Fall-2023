import re
pattern = r'ab*'
# with open('row.txt', 'r') as file:
#      text = file.read()
text=input()
matches = re.findall(pattern, text)
for match in matches:
    print("Match:", match)
# a=re.findall(pat