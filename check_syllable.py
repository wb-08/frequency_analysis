from difflib import SequenceMatcher
import collections
import rusyllab
import sqlite3


def split_word(text):
    syllables_lst = rusyllab.split_words(text.strip().lower().split())
    return syllables_lst


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


# читаем данные из базы и для каждого слога создаём словарь
# создаём словарь вида : 'слог':(схожесть, частота встречания) и сортируем его
def find_similar_syllable(syllable):
    similarity_syllables = {}
    con = sqlite3.connect('bd/syllable.db')
    cursor_object = con.cursor()
    cursor_object.execute('SELECT * FROM syllables')
    rows = cursor_object.fetchall()
    for row in rows:
        ratio = similarity(row[0], syllable)
        similarity_syllables[row[0]] = (ratio, row[1])
    order_dict = collections.OrderedDict(
        sorted(similarity_syllables.items(), key=lambda item: (item[1], item[0]), reverse=True))
    print(syllable + ': ' + str(list(order_dict)[0:30]))


if __name__ == '__main__':
    word = 'двужа'
    syllables = split_word(word)
    for element in syllables:
        find_similar_syllable(element)
