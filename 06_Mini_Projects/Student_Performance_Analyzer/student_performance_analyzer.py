import numpy as np
k = int(input('Enter number of students: '))
marks = []
for i in range(1, k+1):
    print(f'Marks for student {i}:')

    math = int(input('Enter math score: '))
    science = int(input('Enter science score: '))
    english = int(input('Enter english score: '))
    marks.append([math, science, english])

marks = np.array(marks)
print(marks)
print('\n','='*10,'\n','STATISTICS','\n','='*10,'\n')
print('\n','='*11,'\n','PER SUBJECT','\n','='*11,'\n')
print('Average Maths Score :', np.mean(marks[:,0]))
print('Average Science Score :', np.mean(marks[:,1]))
print('Average English Score :', np.mean(marks[:,2]))
print('\n','='*11,'\n','PER STUDENT','\n','='*11,'\n')
means = np.mean(marks, axis=1)
for i in range(len(means)):
    print(f'Average Score for Student {i+1}:')
    print(f'{means[i]:.2f}')
print('\n','='*11,'\n','CLASS TOPPER','\n','='*11,'\n')
print(f'The class topper is Student {np.argmax(means)+1}')
print(np.max(means))
print('\n','='*23,'\n','BEST PERFORMING SUBJECT','\n','='*23,'\n')
subs = np.mean(marks, axis=0)
subject = ['Maths', 'Science', 'English']
print('The best performing subject is', subject[np.argmax(subs)])
print(np.max(subs))

print('\n','#'*22,'\n',' '*8,'Grades\n', '#'*22,'\n')
Passing = int(input('Enter Passing Average: '))
conditions = [
    means >= 90,
    means >= 80,
    means >= 70,
    means >= 60,
    means >= Passing
]
grades = ['A+', 'A', 'B', 'C', 'D']
student_grades = np.select(conditions, grades, default='F')
print('Individual Grades:')
for i in range(k):
    print(f'Student {i + 1}:')
    print(f'Marks: {marks[i]}')
    print(f'Average: {means[i]}')
    print(f'Grade: {student_grades[i]}')
