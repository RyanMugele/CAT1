class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to store assignments and grades

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        print(f"\nGrades for {self.name}:")
        if not self.assignments:
            print("No assignments available.")
        else:
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # List to store students

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) has been added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                return
        print(f"Student with ID {student_id} not found in this course.")

    def display_all_students_grades(self):
        print(f"\nAll Students and Grades in {self.course_name}:")
        if not self.students:
            print("No students in the course.")
        else:
            for student in self.students:
                print(f"\n{student.name} (ID: {student.student_id}):")
                student.display_grades()


# Create an interactive function for the instructor
def course_management():
    instructor_name = input("Enter instructor's name: ")
    course_name = input("Enter course name: ")
    instructor = Instructor(instructor_name, course_name)

    while True:
        print("\nCourse Management System")
        print("1. Add a student")
        print("2. Assign a grade to a student")
        print("3. Display all students and their grades")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            student_name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(student_name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            student_id = input("Enter the student ID to assign a grade: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == "3":
            instructor.display_all_students_grades()

        elif choice == "4":
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")


# Run the interactive course management system
course_management()
