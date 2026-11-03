
students = [
    {"roll_no": 101, "name": "Jahnavi", "marks": 90},
    {"roll_no": 102, "name": "Kiran", "marks": 78},

    # Two newly added student records
    {"roll_no": 103, "name": "Rahul", "marks": 85},
    {"roll_no": 104, "name": "Priya", "marks": 92}
]


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


def display_students():
    print("\n----- STUDENT RESULT MANAGEMENT SYSTEM -----")
    print("{:<10} {:<15} {:<10} {:<10}".format(
        "Roll No", "Name", "Marks", "Grade"
    ))

    for student in students:
        grade = calculate_grade(student["marks"])

        print("{:<10} {:<15} {:<10} {:<10}".format(
            student["roll_no"],
            student["name"],
            student["marks"],
            grade
        ))


display_students()
