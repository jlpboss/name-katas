import re

kata = input("Enter Kata Name: ")
kata = kata.lower()
kata = re.sub(r'[^a-zA-Z0-9\s]+', '', kata)
kata = kata.replace(" ", "-", -1)
print(kata + ".js")