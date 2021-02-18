
def V(c):
    return c in u"АЕЁИОУЫЭЮЯаеёиоуыэюя"


def C(c):
    return c in u"БВГДЖЗКЛМНПРСТФХЦЧШЩбвгджзклмнпрстфхцчшщ"


def S(c):
    return c in u"Йй"


def M(c):
    return c in u"ЪЬъь"


def BEG(c):
    return c == u"["


def END(c):
    return c == u"]"


def split(s):
    cur_pos = 0
    items = list(u"[" + s + u"]")
    while cur_pos < len(items):
        input_context = items[cur_pos:]
        res = apply1(input_context)
        if res is None:
            cur_pos += 1
        else:
            items = items[:cur_pos] + res[0] + input_context[res[1]:]
            cur_pos += res[2]
    return items[1:-1]


def apply1(s):
        if C(s[0]):
            if V(s[1]):
                if C(s[2]):
                    if V(s[3]):
                        return ([s[0]+s[1], s[2], s[3]], 4, 1)  # SYLLABER_1

                    if C(s[3]):
                        if V(s[4]):
                            return ([s[0]+s[1]+s[2], s[3], s[4]], 5, 1)  # SYLLABER_5

                        if C(s[4]):
                            if C(s[5]):
                                if END(s[6]):
                                    return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5], s[6]], 7, 1)  # SYLLABER_11

                                if not END(s[6]):
                                    return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5], s[6]], 7, 1)  # SYLLABER_12


                            if V(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3], s[4], s[5]], 6, 1)  # SYLLABER_36

                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_120

                            if M(s[5]):
                                if END(s[6]):
                                    return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5], s[6]], 7, 1)  # SYLLABER_330



                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_52

                        if M(s[4]):
                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_76

                            if C(s[5]):
                                if V(s[6]):
                                    return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5], s[6]], 7, 1)  # SYLLABER_250


                            if V(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_260



                    if END(s[3]):
                        return ([s[0]+s[1]+s[2], s[3]], 4, 1)  # SYLLABER_6

                    if M(s[3]):
                        if C(s[4]):
                            if not END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3], s[4], s[5]], 6, 1)  # SYLLABER_13

                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_39

                            if C(s[5]):
                                if C(s[6]):
                                    if END(s[7]):
                                        return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6], s[7]], 8, 1)  # SYLLABER_350




                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_14

                        if V(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_20



                if END(s[2]):
                    return ([s[0]+s[1], s[2]], 3, 1)  # SYLLABER_7

                if S(s[2]):
                    if C(s[3]):
                        if V(s[4]):
                            return ([s[0]+s[1]+s[2], s[3], s[4]], 5, 1)  # SYLLABER_8

                        if C(s[4]):
                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_9


                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_280

                        if M(s[4]):
                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_400



                    if END(s[3]):
                        return ([s[0]+s[1]+s[2], s[3]], 4, 1)  # SYLLABER_10

                    return ([s[0]+s[1]+s[2]], 3, 1)  # SYLLABER_64

                if V(s[2]):
                    return ([s[0]+s[1], s[2]], 3, 1)  # SYLLABER_31


            if C(s[1]):
                if C(s[2]):
                    if V(s[3]):
                        if C(s[4]):
                            if C(s[5]):
                                if V(s[6]):
                                    return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5], s[6]], 7, 1)  # SYLLABER_2

                                if M(s[6]):
                                    if END(s[7]):
                                        return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6], s[7]], 8, 1)  # SYLLABER_310



                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_3

                            if V(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3], s[4], s[5]], 6, 1)  # SYLLABER_4

                            if M(s[5]):
                                if C(s[6]):
                                    if M(s[7]):
                                        if END(s[8]):
                                            return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7], s[8]], 9, 1)  # SYLLABER_300



                                return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5]], 6, 1)  # SYLLABER_200


                        if S(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3]+s[4]], 5, 1)  # SYLLABER_54

                        if V(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_68

                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_170

                        return ([s[0]+s[1]+s[2]+s[3]], 4, 1)  # SYLLABER_210

                    if C(s[3]):
                        if V(s[4]):
                            if S(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5]], 6, 1)  # SYLLABER_220

                            return ([s[0]+s[1]+s[2]+s[3]+s[4]], 5, 1)  # SYLLABER_98



                if V(s[2]):
                    if C(s[3]):
                        if C(s[4]):
                            if V(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3], s[4], s[5]], 6, 1)  # SYLLABER_15

                            if C(s[5]):
                                if C(s[6]):
                                    if END(s[7]):
                                        return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6], s[7]], 8, 1)  # SYLLABER_370


                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_80

                            if M(s[5]):
                                if V(s[6]):
                                    return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5], s[6]], 7, 1)  # SYLLABER_340

                                if C(s[6]):
                                    if V(s[7]):
                                        return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5], s[6], s[7]], 8, 1)  # SYLLABER_390



                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_470


                        if M(s[4]):
                            if not C(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_21

                            if C(s[5]):
                                if V(s[6]):
                                    return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5], s[6]], 7, 1)  # SYLLABER_48

                                if C(s[6]):
                                    if V(s[7]):
                                        return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5], s[6], s[7]], 8, 1)  # SYLLABER_240




                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_62

                        if V(s[4]):
                            return ([s[0]+s[1]+s[2], s[3], s[4]], 5, 1)  # SYLLABER_230


                    if V(s[3]):
                        if C(s[4]):
                            return ([s[0]+s[1]+s[2], s[3], s[4]], 5, 1)  # SYLLABER_17

                        return ([s[0]+s[1]+s[2], s[3]], 4, 1)  # SYLLABER_82

                    if S(s[3]):
                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_33

                        if C(s[4]):
                            if V(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3], s[4], s[5]], 6, 1)  # SYLLABER_92

                            if C(s[5]):
                                if C(s[6]):
                                    if END(s[7]):
                                        return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6], s[7]], 8, 1)  # SYLLABER_450




                        return ([s[0]+s[1]+s[2]+s[3]], 4, 1)  # SYLLABER_190

                    if END(s[3]):
                        return ([s[0]+s[1]+s[2], s[3]], 4, 1)  # SYLLABER_66


                if M(s[2]):
                    if V(s[3]):
                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_410

                        if C(s[4]):
                            if V(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3], s[4], s[5]], 6, 1)  # SYLLABER_480





            if M(s[1]):
                if V(s[2]):
                    if C(s[3]):
                        if V(s[4]):
                            return ([s[0]+s[1]+s[2], s[3], s[4]], 5, 1)  # SYLLABER_16

                        if C(s[4]):
                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_19

                            if V(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3], s[4], s[5]], 6, 1)  # SYLLABER_290

                            if C(s[5]):
                                if C(s[6]):
                                    if V(s[7]):
                                        return ([s[0]+s[1]+s[2]+s[3]+s[4]+s[5], s[6], s[7]], 8, 1)  # SYLLABER_430




                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_22


                    if END(s[3]):
                        return ([s[0]+s[1]+s[2], s[3]], 4, 1)  # SYLLABER_94


                if C(s[2]):
                    if V(s[3]):
                        if S(s[4]):
                            if END(s[5]):
                                return ([s[0]+s[1]+s[2]+s[3]+s[4], s[5]], 6, 1)  # SYLLABER_320


                        if V(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_360






        if V(s[0]):
            if C(s[1]):
                if C(s[2]):
                    if END(s[3]):
                        return ([s[0]+s[1]+s[2], s[3]], 4, 1)  # SYLLABER_18

                    if V(s[3]):
                        return ([s[0]+s[1], s[2], s[3]], 4, 1)  # SYLLABER_28

                    if C(s[3]):
                        if V(s[4]):
                            if C(s[5]):
                                return ([s[0]+s[1]+s[2], s[3], s[4], s[5]], 6, 1)  # SYLLABER_96

                            return ([s[0]+s[1], s[2], s[3], s[4]], 5, 1)  # SYLLABER_50

                        if C(s[4]):
                            if V(s[5]):
                                return ([s[0]+s[1]+s[2], s[3], s[4], s[5]], 6, 1)  # SYLLABER_460



                    if M(s[3]):
                        if END(s[4]):
                            return ([s[0]+s[1]+s[2]+s[3], s[4]], 5, 1)  # SYLLABER_72



                if V(s[2]):
                    return ([s[0], s[1], s[2]], 3, 1)  # SYLLABER_35

                if M(s[2]):
                    if END(s[3]):
                        return ([s[0]+s[1]+s[2], s[3]], 4, 1)  # SYLLABER_40

                    if C(s[3]):
                        if C(s[4]):
                            if V(s[5]):
                                return ([s[0]+s[1]+s[2], s[3], s[4], s[5]], 6, 1)  # SYLLABER_42


                        if V(s[4]):
                            return ([s[0]+s[1]+s[2], s[3], s[4]], 5, 1)  # SYLLABER_84


                    if V(s[3]):
                        return ([s[0]+s[1]+s[2], s[3]], 4, 1)  # SYLLABER_78


                if END(s[2]):
                    return ([s[0]+s[1], s[2]], 3, 1)  # SYLLABER_44

                return ([s[0]+s[1]], 2, 1)  # SYLLABER_56

            if END(s[1]):
                return ([s[0], s[1]], 2, 1)  # SYLLABER_30

            if V(s[1]):
                return ([s[0], s[1]], 2, 1)  # SYLLABER_34

            if S(s[1]):
                if END(s[2]):
                    return ([s[0]+s[1], s[2]], 3, 1)  # SYLLABER_46

                if C(s[2]):
                    if V(s[3]):
                        return ([s[0]+s[1], s[2], s[3]], 4, 1)  # SYLLABER_180





        if BEG(s[0]):
            if C(s[1]):
                if C(s[2]):
                    if V(s[3]):
                        if C(s[4]):
                            if END(s[5]):
                                return ([s[0], s[1]+s[2]+s[3]+s[4], s[5]], 6, 2)  # SYLLABER_23

                            if C(s[5]):
                                if END(s[6]):
                                    return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5], s[6]], 7, 2)  # SYLLABER_60

                                if M(s[6]):
                                    if END(s[7]):
                                        return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5]+s[6], s[7]], 8, 2)  # SYLLABER_74




                        if S(s[4]):
                            if END(s[5]):
                                return ([s[0], s[1]+s[2]+s[3]+s[4], s[5]], 6, 2)  # SYLLABER_24


                        if END(s[4]):
                            return ([s[0], s[1]+s[2]+s[3], s[4]], 5, 2)  # SYLLABER_27


                    if END(s[3]):
                        return ([s[0], s[1]+s[2], s[3]], 4, 2)  # SYLLABER_70

                    if C(s[3]):
                        if C(s[4]):
                            if V(s[5]):
                                if C(s[6]):
                                    if END(s[7]):
                                        return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5]+s[6], s[7]], 8, 2)  # SYLLABER_88




                        if V(s[4]):
                            if C(s[5]):
                                if M(s[6]):
                                    if END(s[7]):
                                        return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5]+s[6], s[7]], 8, 2)  # SYLLABER_90



                            if END(s[5]):
                                return ([s[0], s[1]+s[2]+s[3]+s[4], s[5]], 6, 2)  # SYLLABER_140




                if V(s[2]):
                    if C(s[3]):
                        if C(s[4]):
                            if M(s[5]):
                                if END(s[6]):
                                    return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5], s[6]], 7, 2)  # SYLLABER_26


                            if END(s[5]):
                                return ([s[0], s[1]+s[2]+s[3]+s[4], s[5]], 6, 2)  # SYLLABER_37


                        if M(s[4]):
                            if C(s[5]):
                                if C(s[6]):
                                    if END(s[7]):
                                        return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5]+s[6], s[7]], 8, 2)  # SYLLABER_440





                    if S(s[3]):
                        if C(s[4]):
                            if END(s[5]):
                                return ([s[0], s[1]+s[2]+s[3]+s[4], s[5]], 6, 2)  # SYLLABER_160




                if END(s[2]):
                    return ([s[0], s[1], s[2]], 3, 2)  # SYLLABER_32

                if M(s[2]):
                    if C(s[3]):
                        if V(s[4]):
                            if END(s[5]):
                                return ([s[0], s[1]+s[2]+s[3]+s[4], s[5]], 6, 2)  # SYLLABER_58

                            if C(s[5]):
                                if END(s[6]):
                                    return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5], s[6]], 7, 2)  # SYLLABER_100

                                if V(s[6]):
                                    return ([s[0], s[1]+s[2]+s[3]+s[4], s[5], s[6]], 7, 2)  # SYLLABER_420




                    if V(s[3]):
                        if END(s[4]):
                            return ([s[0], s[1]+s[2]+s[3], s[4]], 5, 2)  # SYLLABER_86

                        if S(s[4]):
                            if END(s[5]):
                                return ([s[0], s[1]+s[2]+s[3]+s[4], s[5]], 6, 2)  # SYLLABER_110


                        if C(s[4]):
                            if M(s[5]):
                                if END(s[6]):
                                    return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5], s[6]], 7, 2)  # SYLLABER_150






            if V(s[1]):
                if C(s[2]):
                    if M(s[3]):
                        if END(s[4]):
                            return ([s[0], s[1]+s[2]+s[3], s[4]], 5, 2)  # SYLLABER_25


                    if END(s[3]):
                        return ([s[0], s[1]+s[2], s[3]], 4, 2)  # SYLLABER_29

                    if C(s[3]):
                        if C(s[4]):
                            if C(s[5]):
                                if END(s[6]):
                                    return ([s[0], s[1]+s[2]+s[3]+s[4]+s[5], s[6]], 7, 2)  # SYLLABER_130






            if S(s[1]):
                if V(s[2]):
                    if C(s[3]):
                        if V(s[4]):
                            return ([s[0], s[1]+s[2], s[3], s[4]], 5, 2)  # SYLLABER_380






if __name__ == "__main__":
    sx = split(u"спросил")
    print(u"|".join(sx))

def split_word(word):
    """
    Split single word to syllables
    :param word: unicode string representing Russian word
    :return: list of unicode strings for syllables
    """
    return split(word)


def split_words(words):
    """
    Split the words in list to contiguous list of sillables and word separators (single space chars)
    :param words: list of words (unicode strings)
    :return: list of tokens - syllables and spaces
    """
    tokens = []
    for word in words:
        sx = split(word)
        if len(tokens) > 0:
            tokens.append(u' ')
        tokens.extend(sx)
    return tokens
