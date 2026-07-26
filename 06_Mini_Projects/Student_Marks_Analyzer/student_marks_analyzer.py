import numpy as np
marks = np.array([55,72,91,34,87,65,49,100,78,69])
PASS_MARKS = 40
print('='*6,'STUDENT MARKS ANALYZER','='*6)
print('No. of Student :', np.size(marks))
print('Highest Marks :', np.max(marks))
print('Lowest Marks :', np.min(marks))
print('Average Marks :', np.mean(marks))
print('Standard Deviation :', np.std(marks))
print('Passed Students :', marks[marks >= PASS_MARKS])
print('Failed Students :', marks[marks < PASS_MARKS])
print(f'Pass Percentage :, {((np.size(marks[marks >= PASS_MARKS])/np.size(marks)) * 100):.2f}%')
print('Top Scorers :', marks[marks > 80])
print('Sorted Marks :', np.sort(marks))
