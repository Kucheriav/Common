from random import  shuffle
grades = ['7а', '8а', '8б', '8в', '8г', '9а', '10а', '11а', '11б']
shuffle(grades)
grades.sort(key=lambda x: [len(x), x])
print(grades)