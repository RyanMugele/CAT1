class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary has been updated to {self.salary}.")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} (ID: {employee.employee_id}) has been added to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for the {self.department_name} department: {total_salary}")

    def display_all_employees(self):
        print(f"\nEmployees in the {self.department_name} department:")
        if not self.employees:
            print("No employees in this department.")
        else:
            for employee in self.employees:
                employee.display_details()


# Interactive function to manage departments and employees
def department_management():
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\nDepartment Management System")
        print("1. Add an employee")
        print("2. Update an employee's salary")
        print("3. Display all employees")
        print("4. Display total salary expenditure")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee's ID: ")
            salary = float(input("Enter employee's salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            employee_id = input("Enter the employee ID to update salary: ")
            for employee in department.employees:
                if employee.employee_id == employee_id:
                    new_salary = float(input("Enter new salary: "))
                    employee.update_salary(new_salary)
                    break
            else:
                print("Employee not found.")

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.calculate_total_salary_expenditure()

        elif choice == "5":
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")


# Run the interactive department management system
department_management()
