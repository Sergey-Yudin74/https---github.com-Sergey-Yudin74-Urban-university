grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny',
            'Bilbo',
            'Steve',
            'Khendrik',
            'Aaron'}
students = list(students)
students_= students.sort()
dict_ = zip(students, grades)
students_grades = dict(dict_)
print(students_grades)
from statistics import mean
students_grades1 = {k:mean(v) for k,v in students_grades.items()}
print(students_grades1)