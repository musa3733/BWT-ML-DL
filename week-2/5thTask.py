def get_student_details():
    students = []
    for i in range(3):
        name = input(f"Enter the name of student {i + 1}: ")
        age = int(input(f"Enter the age of student {i + 1}: "))
        grade = input(f"Enter the grade of student {i + 1}: ")
        students.append((name, age, grade))
    return students

def convert_to_dict(students):
    student_dict = {}
    for student in students:
        name, age, grade = student
        student_dict[name] = (age, grade)
    return student_dict

def display_students(student_dict):
    for name, details in student_dict.items():
        age, grade = details
        print(f"Name: {name}, Age: {age}, Grade: {grade}")

def main():
    students = get_student_details()
    student_dict = convert_to_dict(students)
    display_students(student_dict)

# Run the main function
if __name__ == "__main__":
    main()
