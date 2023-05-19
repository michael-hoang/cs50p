camel_case = input('camelCase: ')
snake_case = ''
for letter in camel_case:
    if letter.isupper():
        snake_case += f'_{letter.lower()}'
    else:
        snake_case += letter

print(snake_case)
