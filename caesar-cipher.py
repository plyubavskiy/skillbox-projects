def get_index(sym, i_shift, letters):
    index = alphabet.index(sym)
    new_index = index + i_shift
    if new_index > len(letters) - 1:
        new_index = new_index % len(letters)
    return new_index


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
list_alphabet = list(alphabet)

mess = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
new_mess = ''

for symbol in mess:
    if symbol in list_alphabet:
        new_mess += list_alphabet[get_index(symbol, shift, list_alphabet)]
    else:
        new_mess += symbol

print('Зашифрованное сообщение:', new_mess)