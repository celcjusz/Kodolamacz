a = "12345678"
number_str = a #[::-1]

print(number_str)

number_threes = []
HUND_LEN = 3
end_point = len(number_str)

while end_point > 0:
    start_point = end_point - 3 if end_point - 3 >= 0 else 0
    number_threes.append(number_str[start_point : end_point])
    end_point -= 3
    # print(start_point)

print (number_threes)

number_str = a[::-1]
number_threes = []
i = 0
while i < len(number_str):
    number_threes.append(number_str[i:i + 3])
    i += 3

print (number_threes)
