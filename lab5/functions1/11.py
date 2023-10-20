def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

word = "madam"
result = is_palindrome(word)
if result:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")



       

