# Assignment 1 / COMPE 361 / Luis Bello

student_grades = [{'name': 'Kathlyn Wakefield', 'gender': 'female', 'grade': 75},
                  {'name': 'Gerry Kinsey', 'gender': 'male', 'grade': 90},
                  {'name': 'Isaac Fortune', 'gender': 'male', 'grade': 8},
                  {'name': 'Elisa Christian', 'gender': 'female', 'grade': 35},
                  {'name': 'Christy Derrickson', 'gender': 'female', 'grade': 82}]
grade_table = {'A+': (90, 100),
               'A': (80, 89),
               'B+': (75, 79),
               'B': (70, 74),
               'C+': (65, 69),
               'C': (60, 64),
               'C-': (0, 59)}


def average_grade(student_grades):
    sum = 0
    for student in student_grades:
        sum += student['grade']
    avg = sum/len(student_grades)
    print(f'\t\tGrade Average: {avg}\n')
    return avg


def average_grade_of_male_students(student_grades):
    temp = []
    for student in student_grades:
        if student['gender'] == 'male':
            temp.append(student)
    print('\tMale Students')
    average_grade(temp)


def maximum_grade_of_female_students(student_grades):
    max_grade = 0
    for student in student_grades:
        if student['gender'] == 'female':
            if max_grade < student['grade']:
                max_grade = student['grade']
    print(f'\tMaximum grade of female students: {max_grade}\n')
    return max_grade


def calculate_and_add_letter_grades(student_grades, grade_table):
    print('\tStudent_grades with letter grade update:\n')
    for student in student_grades:
        for grade in grade_table:
            temp_low = grade_table[grade][0]
            temp_high = grade_table[grade][1]
            if student['grade'] <= temp_high and student['grade'] >= temp_low:
                student.update({'letter_grade':str(grade)})
                print(f'\t\t{student}')
    print()
    return student_grades


def sort_descending_order_by_grades(student_grades):
    print('\tStudent_grades sorted in descending order:\n')
    temp = student_grades
    new_student_grades = []
    x = 0
    while x < len(temp):
        max_grade = 0
        for student_index in temp:
            if max_grade < student_index['grade']:
                max_grade = student_index['grade']
        for student in student_grades:
            if student['grade'] == max_grade:
                new_student_grades.append(student)
                temp.remove(student)
                print(f'\t\t{student}')
    return new_student_grades


if __name__ == '__main__':
    print('\nAssignment 1 output\n')
    print('\tAll Students')
    average_grade(student_grades)
    average_grade_of_male_students(student_grades)
    maximum_grade_of_female_students(student_grades)
    calculate_and_add_letter_grades(student_grades, grade_table)
    sort_descending_order_by_grades(student_grades)