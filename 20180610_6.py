NUMBER_DICT = {"0":"zero",
                "1":"one",
               "2":"two",
               "3":"three",
               "4":"four",
               "5":"five",
               "6":"six",
               "7":"seven",
               "8":"eight",
               "9":"nine",
               ".":"point"}

def cyphers_to_words(number):
    numb_words=[]
    #
    # for i in str(number):
    #     numb_words.append(NUMBER_DICT[i])
    #
    numb_words = [NUMBER_DICT[x] for x in str(number)]
    #
    print(number)
    print(" ".join(numb_words))

#cyphers_to_words(23234384.23)







NUMBER_OF_TENS_DICT = {"1":"",
                       "2":"twenty",
                       "3":"thirty",
                       "4":"fourty",
                       "5":"fifty",
                       # "6":"sixty",
                       # "7":"seventy",
                       # "8":"eighty",
                       # "9":"ninety"
                       }

def number_to_words(number):
    number_str = str(number)[::-1]
    word_list = []
    i=0
    while i < len(number_str):
        if i % 3 == 0:
            try:
                tens = number_str[i+1]
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
            if (i+1) / 3 == 1:
                element += " hundred"
            elif (i+1) / 6 == 1:
                element += " thousand"
            elif (i+1) / 9 == 1:
                element += " million"
            else:
                element += " a fucking lot"
            word_list.append(element)
        i += 1
    return " ".join(word_list[::-1])

print(number_to_words(13654483311))