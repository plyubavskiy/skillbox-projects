text = input('Введите строку с 2 (h): ')
first_isymb = text.index('h')
last_isymb = text.rindex('h')

print(text[:first_isymb + 1] +
      text[last_isymb - 1:first_isymb - 1:-1] +
      text[last_isymb + 1:])

# другой способ

text = input('Введите строку с 2 (h): ')
first_part = text[:text.find('h')]
central_part = text[text.find('h'):text.rfind('h') + 1]
last_part = text[text.rfind('h') + 1:]

new_text = first_part + central_part[::-1] + last_part
print(new_text)