import statistics as stat

ALLOWED_GRADES = {2, 3, 3.5, 4, 4.5, 5}
grade_lst = []

while True:
    grade = input("Enter grade (press return to finish): ")
    if not grade:
        break;
    try:
        grade = float(grade)
        if grade in ALLOWED_GRADES:
            grade_lst.append(grade)
        else:
            print("Grade must be one of the following: ",ALLOWED_GRADES)
    except ValueError:
        print("Entered value is not a number. Following grades are allowed: ", ALLOWED_GRADES)

mean_normal = sum(grade_lst) / len(grade_lst)
mean_stat = stat.mean(grade_lst)

print(f"Normally calculated mean: {mean_normal}\nMean using 'statistics' package: {mean_stat}")