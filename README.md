# Student Grades Calculator

## Overview
This project is a simple command-line Grade Management System built with Python.
It lets you:

- Add students by name
- Add grades for a specific student
- View a student's grades, average, highest grade, and lowest grade
- List all students currently stored in the program

The goal is to practice Python fundamentals using a real, interactive mini-project.

## How It Works
The program is defined in `grades.py` and uses:

- A `Student` class to represent each student
- A list of `Student` objects to store data in memory while the program runs
- A menu loop in `main()` to repeatedly accept user input and perform actions

### Student Class
Each `Student` object has:

- `name`: the student's name
- `grades`: a list of numeric grades

Methods:

- `add_grade(grade)`: adds a grade to the student's list
- `get_average()`: returns average grade (or `None` if no grades)
- `display_grades()`: prints all grades plus average, highest, and lowest

### Menu Options
When you run the script, you can choose from:

1. Add a student by name
2. Add a grade for a student
3. Display grades for a student
4. Display a specific student's grades
5. Display all students
6. Exit

Note: Options 3 and 4 currently perform very similar behavior (both display a selected student's grades).

## How To Run
### Requirements
- Python 3.x installed

### Run Command
From the project folder, run:

```bash
python grades.py
```

If your system uses `python3`, run:

```bash
python3 grades.py
```

## Example Flow
1. Start the app
2. Add a student (for example: Alex)
3. Add grades (for example: 88, 92, 79)
4. Display Alex's grades to see:
	- Full grade list
	- Average
	- Highest grade
	- Lowest grade

## Skills Used
This project demonstrates:

- Python classes and object-oriented programming basics
- Defining and using instance methods
- Lists and list operations (`append`, `sum`, `max`, `min`)
- Conditional logic (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- User input handling with `input()`
- Basic CLI (command-line interface) design
- Function organization (`main()`)

## Possible Improvements
- Add input validation (for non-numeric grades and grade ranges)
- Prevent duplicate student names or support unique student IDs
- Save/load students and grades from a file (JSON/CSV)
- Add edit/delete features for students and grades
- Split logic into multiple files for scalability