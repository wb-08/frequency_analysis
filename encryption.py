from collections import Counter


def caesar_cipher():
    file = open("text.txt")
    text_for_encrypt = file.read().lower().replace(',', '')
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    arr = []
    step = 3
    for i in text_for_encrypt:
        if i == ' ':
            arr.append(' ')
        else:
            arr.append(letters[(letters.find(i) + step) % 33])
    text_for_decrypt = ''.join(arr)
    return text_for_decrypt


def number_of_letters(text_for_decrypt):
    counter = Counter(text_for_decrypt)
    arr_decrypt_letters = []
    for i in range(len(counter)):
        arr_decrypt_letters.append(counter.most_common(len(counter))[i][0])

    return arr_decrypt_letters


def decrypt_text(text_for_decrypt, arr_decrypt_letters):
    arr_encrypt_text = []
    arr_encrypt_letters = [' ', 'о', 'а', 'е', 'и', 'т', 'н', 'л',
                           'р', 'с', 'в', 'к', 'м', 'д', 'у', 'п',
                           'б', 'г', 'ы', 'ч', 'ь', 'з', 'я', 'й',
                           'х', 'ж', 'ш', 'ю', 'ф', 'э', 'щ',
                           'ё', 'ц', 'ъ']
    dictionary = dict(zip(arr_decrypt_letters, arr_encrypt_letters))
    for i in text_for_decrypt:
        arr_encrypt_text.append(dictionary.get(i))
    text_for_decrypt = ''.join(arr_encrypt_text)
    print(text_for_decrypt)


if __name__ == '__main__':
    text_for_decrypt = caesar_cipher()
    arr_decrypt_letters = number_of_letters(text_for_decrypt)
    decrypt_text(text_for_decrypt, arr_decrypt_letters)



