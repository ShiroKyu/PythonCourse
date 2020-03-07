def count_vowels(txt):
    cont = 0
    for letter in txt:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            cont += 1
    return cont


print(count_vowels('Paulo'))

# Soluções alternativas

'''
def count_vowels(txt):
  return sum([1 for x in txt.lower() if x in 'aeiou'])
'''

'''
def countVowels(string):
       vowels = ['a','e','i','o','u']
   total = 0
   for s in string:
      if s in vowels:
         total += 1
   return total
'''
