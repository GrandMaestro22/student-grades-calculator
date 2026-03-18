class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []    # each student starts with no grades

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Added grade {grade} for {self.name}")

    def get_average(self):
        if not self.grades:
            print("No grades yet.")
            return None
        return sum(self.grades) / len(self.grades)

    def display_grades(self):
        if not self.grades:
            print(f"{self.name} has no grades yet.")
            return
        print(f"\n{self.name}'s grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Highest: {max(self.grades)}")
        print(f"Lowest: {min(self.grades)}")

def main():
    students = []
    active = True
    while active:
        print("\nGrade Management System")
        print("1. Add a Student by name")
        print("2. Add a grade for a student")
        print("3. Display grades for a student")
        print("4. Display a specific student's grades")
        print("5. Display all students")
        print("6. Delete a student")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter the student's name: ")
            student = Student(name)
            students.append(student)
            print(f"Student {name} added.")
        elif choice == '2':
            name = input("Enter the student's name: ")
            grade = float(input("Enter the grade to add: "))
            for student in students:
                if student.name == name:
                    student.add_grade(grade)
                    break
            else:
                print(f"No student found with the name {name}.")
        elif choice == '3':
            name = input("Enter the student's name: ")
            for student in students:
                if student.name == name:
                    student.display_grades()
                    break
            else:
                print(f"No student found with the name {name}.")
        elif choice == '4':
            name = input("Enter the student's name: ")
            if not students:
                print("No students available.")
                continue
            for student in students:
                if student.name == name:
                    student.display_grades()
                    break
            else:
                print(f"No student found with the name {name}.")
        elif choice == '5':
            if not students:
                print("No students added yet.")
            else:
                print("\nAll students:")
                for i, student in enumerate(students):
                    print(f"  {i + 1}. {student.name}")
        elif choice == '6':
            name = input("Enter the student's name to delete: ")
            for i, student in enumerate(students):
                if student.name == name:
                    del students[i]
                    print(f"Student {name} deleted.")
                    break
            else:
                print(f"No student found with the name {name}.")
        elif choice == '7':
            print("Exiting the Grade Management System.")
            active = False
main()