def separate_student_details(students):
    roll_nos = [student[0] for student in students]
    names = [student[1] for student in students]
    ages = [student[2] for student in students]

    return roll_nos, names, ages

students_list = [(151, "ved", 19), (153, "prem", 20), (154, "jinit", 18), (156, "rohit", 19)]

roll_numbers, names, ages = separate_student_details(students_list)

print("Roll Numbers:", roll_numbers)
print("Names:", names)
print("Ages:", ages)
