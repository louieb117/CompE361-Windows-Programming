import pandas as pd

df_students = pd.read_excel('Assignment3.xlsx')
df_grades = pd.read_excel('Assignment3.xlsx', sheet_name=1)
df = pd.merge(df_students, df_grades, on='student_id', how='right')

df_computer = df_grades[df_grades.course_name == 'Computer']
df_math = df_grades[df_grades.course_name == 'Math']
df_physics = df_grades[df_grades.course_name == 'Physics']

#print('Hello World')
#print(df_students)
#print(df_grades)
# course_name
# Computer    50.504950
# Math        52.108911
# Physics     51.009901
def print_average_grades():


    avg_computer = df_computer.grade.sum()/len(df_computer)
    avg_math = df_math.grade.sum()/len(df_math)
    avg_physics = df_physics.grade.sum()/len(df_physics)

    print('\ncourse_name')
    print(f'Computer\t{avg_computer}')
    print(f'Math\t\t{avg_math}')
    print(f'Physics\t\t{avg_physics}\n')


#               grade
#               max min
# course_name
# Computer       96   0
# Math          100   1
# Physics       100   1
def print_max_and_min_grades():

    print('\t\tgrade')
    print('\t\tmax\tmin')
    print('course_name')
    print(f'Computer\t{df_computer.grade.max()}\t{df_computer.grade.min()}')
    print(f'Math\t\t{df_math.grade.max()}\t{df_math.grade.min()}')
    print(f'Physics\t\t{df_physics.grade.max()}\t{df_physics.grade.min()}\n')


# the shown results are for Math
#
#
#    first_name   last_name  grade
# 0         Sau        Pfau     97
# 1         Sau        Pfau     96
# 2        Etta        Hurn     83
# 3      Teresa      Strawn     58
# 4    Lauralee     Perrine     87
# 5    Rasheeda      Alkire     77
# 6      Dorcas      Darity     53
# 7        Mara   Hashimoto     62
# 8    Franklyn      Unknow     95
# 9       Holly        Eudy     57
# 10     Dorcas      Darity     59
# 11     Tommie   Underdahl     54
# 12   Franklyn      Unknow     90
# 13   Vincenza     Weiland     89
# 14     Kelsie     Wachtel     59
# 15       Veta       Muntz     80
# 16      Chase      Karner     97
# 17       Veta       Muntz     54
# 18     Fallon     Winward     86
# 19       Jona     Grindle     63
# 20     Gaston       Brumm     77
# 21     Kelsie     Wachtel     87
# 22     Marvel        Hail     98
# 23   Demetria       Abbey     62
# 24    Arcelia      Bouska     85
# 25     Shavon      Benito     57
# 26      Holly        Eudy     55
# 27     Weston     Martina    100
# 28  Willodean        Harn     91
# 29     Philip        Gent     67
# 30     Lester     Prothro     78
# 31     Felisa        Cail     93
# 32     Stasia      Becker     65
# 33     Loreta      Curren     77
# 34     Marcel   Zabriskie     91
# 35       Kina    Hazelton     82
# 36   Lauralee     Perrine     83
# 37      Dulce       Abril     78
# 38       Roma  Lafollette     91
# 39     Lester     Prothro     67
# 40      Angel       Sanor     98
# 41    Earlean      Melgar     86
# 42    Shanice   Mccrystal     76
# 43   Kathleen      Hanner     61
# 44       Nena      Hacker     60
# 45     Felisa        Cail     87
# 46       Jona     Grindle     63
# 47    Angelyn        Vong     77
def print_students_greater_than_average(course_name):
    df_course = df[df.course_name == course_name]
    avg_course = df_course.grade.sum()/len(df_course)

    df_gta = df_course[df_course.grade > avg_course]
    df_gta = df_gta.reset_index()

    print(df_gta[['first_name', 'last_name','grade']])




#     course_name  gender first_name   last_name  grade
# 135    Computer  Female       Roma  Lafollette     96
# 76         Math  Female     Marvel        Hail     98
# 100     Physics  Female      Judie    Claywell    100
# 278    Computer    Male      Angel       Sanor     95
# 133        Math    Male     Weston     Martina    100
# 167     Physics    Male     Gaston       Brumm     88
def print_male_and_female_students_with_max_grade():
    #df_female = df[df.gender == 'Female']
    df_female = df.loc[df['gender'] == 'Female']

    df_female_comp = df_female[df_female.course_name == 'Computer']
    df_fc_max = df_female_comp.loc[df_female_comp.grade == df_female_comp.grade.max()]

    df_female_math = df_female[df_female.course_name == 'Math']
    df_fm_max = df_female_math.loc[df_female_math.grade == df_female_math.grade.max()]

    df_female_phys = df_female[df_female.course_name == 'Physics']
    

    female_comp = pd.DataFrame()
    female_math = pd.DataFrame()
    df_f_print = pd.DataFrame()
    female_comp = df_female_comp.sort_values(by='grade',ascending=False).iloc[0][['course_name','gender','first_name', 'last_name','grade']]
    female_math = df_female_math.sort_values(by='grade',ascending=False).iloc[0][['course_name','gender','first_name', 'last_name','grade']]
    df_f_print = pd.concat([female_comp,female_math])

    print(df_female)
    print(max)
    print(df_fc_max)
    df_female_math.grade.sort_values()
    df_female_phys.grade.sort_values()


if (__name__ == '__main__'):
    #print_average_grades()
    #print_max_and_min_grades()
    #print_students_greater_than_average('Math')
    #print_students_greater_than_average('Physics')
    print_male_and_female_students_with_max_grade()
