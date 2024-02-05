import csv


###########################
## Functions declarations##
###########################
# Load student data from CSV
def load_students(filename):
    students_data = {}
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_data[row['ID']] = row
    except FileNotFoundError:
        print(f"CSV file {filename} not found. Creating a new empty student list.")
    return students_data

# Save Students to CSV
def save_students(students, filename):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['ID', 'Surname', 'Forename', 'DOB', 'Address', 'Phone', 'Gender', 'Tutor Group']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for student in students.values():
            writer.writerow(student)

# add a student function
def add_student(students):
    student = {}
    student['ID'] = input("Enter student ID number: ")
    student['Surname'] = input("Enter student surname: ")
    student['Forename'] = input("Enter student forename: ")
    student['DOB'] = input("Enter date of birth: ")
    student['Address'] = input("Enter home address: ")
    student['Phone'] = input("Enter home phone number: ")
    student['Gender'] = input("Enter gender: ")
    student['Tutor Group'] = input("Enter tutor group: ")

    students[student['ID']] = student
    print("Student added successfully.")

# Retrieve a student function
def retrieve_student(students, student_id):
    student = students.get(student_id)
    if student:
        print(', '.join([f"{key}: {value}" for key, value in student.items()]))
    else:
        print("Student not found.")

# Generate a report
def generate_report(students):
    print("Student Report:")
    for student in students.values():
        print(', '.join([f"{key}: {value}" for key, value in student.items()]))

# log in function
def login(username, password):
    return username == "admin" and password == "admin123"

def main_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Retrieve Student")
    print("3. Generate Report")
    print("4. Logout")
 
def main():
    students = load_students('students.csv')
 
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
 
        if login(username, password):
            print("Login successful.")
            break
        else:
            print("Login failed. Please try again.")
 
    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")
 
        if choice == "1":
            add_student(students)
            save_students(students, 'students.csv')
            print("Student added successfully.")
        elif choice == "2":
            student_id = input("Enter student ID: ")
            retrieve_student(students, student_id)
        elif choice == "3":
            generate_report(students)
        elif choice == "4":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
 
if __name__ == "__main__":
    main()