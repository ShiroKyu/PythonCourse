Str = 'shOrtCAKE'
newStr = ''

for letter in Str:
    if letter.isupper():
        newStr += letter

for letter in Str:
    if not letter.isupper():
        newStr += letter

print(newStr)
