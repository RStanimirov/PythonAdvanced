number_of_students = int(input())

students_dict = {}

for i in range(number_of_students):
    command = input().split()
    name = command[0]
    grade = float(command[1])
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

for student in students_dict.items():
    student_name = student[0]
    student_grades = student[1]
    average_grade = sum(student[1]) / len(student[1])
    grades_as_str = []
    for x in student_grades:
        grades_as_str.append(str(f'{x:.2f}'))
    # grades_as_str = ' '.join([f"{x:.2f}" for x in student_grades])
    print(f"{student_name} -> {' '.join(grades_as_str)} (avg: {average_grade:.2f})")
