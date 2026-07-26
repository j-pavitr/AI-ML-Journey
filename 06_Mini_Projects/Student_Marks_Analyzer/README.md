# 📊 Student Marks Analyzer

A Python and NumPy project that analyzes student marks and generates a detailed performance report.

## Version

Current Version: **v2**

---

## Features

### Version 1
- Analyze student marks using NumPy
- Highest marks
- Lowest marks
- Average marks
- Standard deviation
- Passed students
- Failed students
- Pass percentage
- Top scorers
- Sorted marks

### Version 2
- User enters the number of students
- User enters marks for each student
- Input validation (only accepts marks between 0 and 100)
- User-defined passing marks
- Automatic grade generation (A+, A, B, C, D, F)
- Individual grade report for every student

---

## Technologies Used

- Python 3
- NumPy

---

## Project Structure

```
Student_Marks_Analyzer/
│── student_marks_analyzer_v1.py
│── student_marks_analyzer_v2.py
│── README.md
```

---

## How to Run

1. Clone the repository.
2. Open the project in PyCharm or VS Code.
3. Install NumPy:

```bash
pip install numpy
```

4. Run:

```bash
python student_marks_analyzer_v2.py
```

---

## Sample Output

```
######################
Student Marks Analyzer
######################

Students : 5

Highest : 98

Lowest : 43

Average : 74.60

Passed Students : 5

Failed Students : 0

Pass Percentage : 100.00%

Top Scorers : [98 91]

Sorted Marks : [43 65 76 91 98]
```

---

## Future Improvements

- [ ] Read marks from a CSV file (Pandas)
- [ ] Display charts (Matplotlib)
- [ ] Export report to PDF
- [ ] GUI version using Tkinter
- [ ] Web version using Streamlit

---

## Author

**Pavitr Jain**

Learning AI, Machine Learning, Data Science and Python by building projects.