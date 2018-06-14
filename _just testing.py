a = "12312312312"
number_str = a[::-1]

print(number_str)

number_threes = []
i = 3

while i -3 < len(number_str):
    number_threes.append(number_str[i - 3:i])
    i += 3

print (number_threes)