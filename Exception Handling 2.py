class NegativeAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Invalid age: {self.age} (Negative age is not allowed)"


def create_student_dictionary():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    if age < 0:
        raise NegativeAgeError(age)

    marks = []
    for i in range(1, 7):
        mark = float(input(f"Enter mark for subject {i}: "))
        marks.append(mark)

    student_details = {
        "Name": name,
        "Age": age,
        "Marks": marks
    }

    return student_details


# Main program
try:
    student_dict = create_student_dictionary()
    print("Student Details:", student_dict)
except NegativeAgeError as e:
    print("Error:", str(e))

