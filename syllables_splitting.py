from collections import Counter
import sqlite3
import rusyllab


def count_of_syllables():
    arr_syllables = []
    file = open("comments/clean_comments.txt", "r")
    for line in file:
        syllables = rusyllab.split_words(line.strip().lower().split())
        for syllable in syllables:
            arr_syllables.append(syllable)
    return dict(Counter(arr_syllables))


def add_syllables_in_bd(syllables_frequency):
    con = sqlite3.connect('bd/syllable.db')
    cursor_object = con.cursor()
    for key, value in syllables_frequency.items():
        if value > 50:
            cursor_object.execute("INSERT INTO syllables (word,count) VALUES('{}','{}')".format(str(key), value))
            con.commit()


if __name__ == '__main__':
    frequency_syllables = count_of_syllables()
    add_syllables_in_bd(frequency_syllables)
