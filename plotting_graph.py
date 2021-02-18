import matplotlib.pyplot as plt
from collections import Counter


arr_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
               'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
               'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
               'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


arr_wikipedia_frequency = [8.01, 1.59, 4.54, 1.7, 2.98, 8.45, 0.04, 0.94, 1.65, 7.35,
                           1.21, 3.49, 4.4, 3.21, 6.7, 10.97, 2.81, 4.73, 5.47, 6.26,
                           2.62, 0.26, 0.97, 0.48, 1.44, 0.73, 0.36, 0.04, 1.9, 1.74,
                           0.32, 0.64, 2.01]

f = open('comments.txt')
counter = Counter(f.read().lower())


def count_letters():
    count = 0
    for i in range(len(arr_letters)):
        count += counter[arr_letters[i]]
    return count


def frequency(count):
    arr_my_frequency = []
    for i in range(len(arr_letters)):
        frequency = counter[arr_letters[i]] / count * 100
        arr_my_frequency.append(frequency)

    return arr_my_frequency



def plotting_diagram(arr_my_frequency):

    fig, ax = plt.subplots()

    xs = range(len(arr_letters))

    ax.bar([x + 0.05 for x in xs], arr_my_frequency,
           width=0.1, color='red', alpha=0.7, label='my',
           zorder=2)
    ax.bar([x + 0.15 for x in xs], arr_wikipedia_frequency,
           width=0.1, color='blue', alpha=0.7, label='wikipedia',
           zorder=2)

    plt.xticks(xs, arr_letters)
    ax.set_facecolor('seashell')
    fig.set_figwidth(21)
    fig.set_figheight(12)
    fig.set_facecolor('floralwhite')
    plt.legend()
    fig.savefig('frequency_0.png')


if __name__ == '__main__':
    count = count_letters()
    arr_my_frequency = frequency(count)
    plotting_diagram(arr_my_frequency)

