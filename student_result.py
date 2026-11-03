students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return

    for roll, details in students.items():
        print("\nRoll Number:", roll)
        print("Name:", details["name"])
        print("Marks:", details["marks"])

def main():
    while True:
        print("\n===== STUDENT RESULT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

main()