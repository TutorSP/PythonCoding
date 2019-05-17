# WAP in Python to input name, roll number and marks of a student in 3 subjects. Display student details alongwith his average
# marks, highest mark, lowest mark

name = input("Enter name of student: ")
roll = input("Enter roll number of student: ")
sub_first = int(input("Enter marks in first subject: "))
sub_second = int(input("Enter marks in second subject: "))
sub_third = int(input("Enter marks in third subject: "))
avg_marks = round(((sub_first + sub_second + sub_third) / 3), 3)
highest_mark = max(sub_first, sub_second, sub_third)
lowest_mark = min(sub_first, sub_second, sub_third)
print("Name: {} \nRoll Number: {} \nAverage Marks: {} \nHighest Mark: {} \nLowest Mark: {}".format(name, roll, avg_marks,\
highest_mark, lowest_mark))