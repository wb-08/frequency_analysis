import re


def delete_emojis(text):
    pattern = re.compile(pattern="["
                                 u"\U0001F600-\U0001F64F"
                                 u"\U0001F300-\U0001F5FF"
                                 u"\U0001F680-\U0001F6FF"
                                 u"\U0001F1E0-\U0001F1FF"
                                 "]+", flags=re.UNICODE)
    return pattern.sub(r'', text)


# delete references like '[id529195942|Расул], good РФ -> , good РФ
def delete_references(text):
    pattern = r'\[\w+\|\w+\]'
    return re.sub(pattern, '', text)


def delete_symbols(text):
    for letter in text:
        if letter.isalpha() or letter.isspace():
            pass
        else:
            text = text.replace(letter, '')
    return text


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def clean_text():
    arr_clean_comments = []
    file = open("comments/all_comments.txt", "r")
    for line in file:
        comment = delete_emojis(line.strip())
        comment = delete_references(comment)
        clean_comment = delete_symbols(comment)
        if has_cyrillic(clean_comment):
            arr_clean_comments.append(clean_comment)

    return list(set(arr_clean_comments))


def add_clean_text_in_file(clean_comments):
    file = open("comments/clean_comments.txt", 'a')
    file.writelines("%s\n" % comment for comment in clean_comments)


if __name__ == '__main__':
    lst_clean_comments = clean_text()
    add_clean_text_in_file(lst_clean_comments)
