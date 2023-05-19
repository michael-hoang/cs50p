vowels = 'aeiouAEIOU'
text = input('Input: ')
output = ''
for char in text:
    if char not in vowels:
        output += char

print(f'Output: {output}')
