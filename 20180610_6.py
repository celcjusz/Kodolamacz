NUMBER_DICT = {"0": "zero",
               "1": "one",
               "2": "two",
               "3": "three",
               "4": "four",
               "5": "five",
               "6": "six",
               "7": "seven",
               "8": "eight",
               "9": "nine",
               ".": "point"}


def cyphers_to_words(number):
    numb_words = []
    #
    # for i in str(number):
    #     numb_words.append(NUMBER_DICT[i])
    #
    numb_words = [NUMBER_DICT[x] for x in str(number)]
    #
    print(number)
    print(" ".join(numb_words))


# cyphers_to_words(23234384.23)





NUMBER_DICT = {"0": "",
               "1": "one",
               "2": "two",
               "3": "three",
               "4": "four",
               "5": "five",
               "6": "six",
               "7": "seven",
               "8": "eight",
               "9": "nine",
               ".": "point"}

NUMBER_OF_TENS_DICT = {"0": "",
                        "1": "ten",
                        "2": "twenty",
                       "3": "thirty",
                       "4": "fourty",
                       "5": "fifty",
                       "6": "sixty",
                       "7": "seventy",
                       "8": "eighty",
                       "9": "ninety"
                       }

NUMBER_OF_TEENS_DICT = {"10": "ten",
                        "11": "eleven",
                        "12": "twelve",
                        "13": "thirteen",
                        "14": "fourteen",
                        "15": "fifteen",
                        "16": "sixteen",
                        "17": "seventeen",
                        "18": "eighteen",
                        "19": "nineteen"}


def number_to_words(number):
    # Let's divide the number into hundreds - each 3-cypher group can be treated the same way :)
    # string must be reversed, so that we start from the lowest number (10 ** 0 + 10 ** 1 + etc.)
    number_str = str(number)[::-1]
    number_threes = []
    i = 0
    while i < len(number_str):
        number_threes.append(number_str[i:i + 3])
        i += 3

    #empty list of words
    word_list = []

    # only a 3-cypher group is really interesting for us
    i = 0
    while i < len(number_threes):
        three_words_list = []
        #print(number_threes[i])

        #each hundred is already reversed, so that we start from units,thru tens until hundreds
        hundred_reversed = number_threes[i]

        if i == 0:
            pass
        elif i == 1:
            three_words_list.append("thousand")
        elif i == 2:
            three_words_list.append("million")
        elif i == 3:
            three_words_list.append("billion")
        else:
            three_words_list.append("fucking lot")

        #units
        if len(hundred_reversed) > 1 and int(hundred_reversed[1]) == 1:
            pass
            # three_words_list.append(NUMBER_OF_TEENS_DICT[hundred_reversed[1] + hundred_reversed[0]])
        elif int(hundred_reversed[0]) > 0:
            three_words_list.append(NUMBER_DICT[hundred_reversed[0]])
        elif hundred_reversed[0] == 0 and len(hundred_reversed) == 1:
            three_words_list.append("zero")

        # tens
        if len(hundred_reversed) > 1 and int(hundred_reversed[1]) > 1:
            three_words_list.append(NUMBER_OF_TENS_DICT[hundred_reversed[1]])
        elif len(hundred_reversed) > 1 and int(hundred_reversed[1]) == 1:
            three_words_list.append(NUMBER_OF_TEENS_DICT[hundred_reversed[1] + hundred_reversed[0]])

        #hundreds
        if len(hundred_reversed) > 2 and int(hundred_reversed[2]) > 0:
            three_words_list.append(NUMBER_DICT[hundred_reversed[2]] + " hundred")

        # hundreds
        #print(number_threes[i][0])

        word_list.append(" ".join(three_words_list[::-1]))
        i += 1

    return " ".join(word_list[::-1])

"""
def number_to_words1(number):
    number_str = str(number)[::-1]
    word_list = []
    i = 0
    while i < len(number_str):
        if i % 3 == 0:
            try:
                tens = number_str[i + 1]
            except IndexError:
                pass
            if tens == '1':
                word_list.append(NUMBER_DICT[number_str[i]] + "teen")
            else:
                word_list.append(NUMBER_DICT[number_str[i]])
        if i % 3 == 1:
            try:
                word = NUMBER_OF_TENS_DICT[number_str[i]]
            except KeyError:
                word = NUMBER_DICT[number_str[i]] + "ty"
            word_list.append(word)
        if i % 3 == 2:
            # print(number_str[i])
            # print(i)
            element = NUMBER_DICT[number_str[i]]
            # print(i+1)
            if (i + 1) / 3 == 1:
                element += " hundred"
            elif (i + 1) / 6 == 1:
                element += " thousand"
            elif (i + 1) / 9 == 1:
                element += " million"
            else:
                element += " a fucking lot"
            word_list.append(element)
        i += 1
    return " ".join(word_list[::-1])
"""

num_input = 74635241#input("Enter a number: ")

print(num_input, "\n", number_to_words(num_input))
