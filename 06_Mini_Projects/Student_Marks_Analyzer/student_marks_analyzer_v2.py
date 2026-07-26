import numpy as np
n = int(input('Enter number of Students '))
marks = []
for i in range(1,n+1):
    while True:
        a = int(input('Enter marks of Student ' + str(i) + ': '))
        if 0 <= a <= 100:
            marks.append(a)
            break
        else:
            print('Invalid Input! Please enter marks between 0 and 100.')
print(marks)

marks = np.array(marks)
Pass = int(input('Enter Passing marks '))

print('\n','#'*22,'\n','Student Marks Analyzer\n', '#'*22,'\n')

print('Student :', n)
print('Highest :', np.max(marks))
print('Lowest :', np.min(marks))
print('Average :', np.mean(marks))
print('Standard Deviation:', np.std(marks))
print('Passed Students :', marks[marks >= Pass])
print('Failed Students :', marks[marks < Pass])
print(f'Pass Percentage :, {((np.size(marks[marks >= Pass])/np.size(marks)) * 100):.2f}%')
print('Top Scorers :', marks[marks > 80])
print('Sorted Marks :', np.sort(marks))

print('\n','#'*22,'\n',' '*8,'Grades\n', '#'*22,'\n')

conditions = [
    marks >= 90,
    marks >= 80,
    marks >= 70,
    marks >= 60,
    marks >= Pass
]
grades = ['A+', 'A', 'B', 'C', 'D']
student_grades = np.select(conditions, grades, default='F')
print('Individual Grades:')
for i in range(n):
    print(f'Student {i + 1}: {marks[i]} marks -> Grade {student_grades[i]}')
