letter = input('Input alphabet letter : ')
vowels = {'a', 'e', 'i', 'o', 'u','e'}  # set
#vowels[1] = 'z' # immutable
#vowels = "aeiuo"  # str
print(type(vowels))
if letter in vowels:  # *in*
    print(f'{letter} is a vowel~')
else:
    print(f'{letter} is a consonant!')