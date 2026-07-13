students = []

with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name": name, "city": city}
        students.append(student)


def get_city(student):
    return student["city"]


for student in sorted(students, key=get_city):
    print(f"{student['name']} is in {student['city']}")
