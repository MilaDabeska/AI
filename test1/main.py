
def gradePoints(points):
    if points > 50:
        return ((points - 1) // 10) + 1


if __name__ == '__main__':
    students = {}

line = input()

while line != "end":
    parts = line.split(",")

    name = parts[0] + " " + parts[1]
    last_name = parts[1]
    index = parts[2]
    subject = parts[3]
    grade = gradePoints(int(parts[4]) + int(parts[5]) + int(parts[6]))

    if (name, index) in students:
        grades = students[(name, index)]
        grades.append((subject, grade))
        students[(name, index)] = grades
    else:
        students[(name, index)] = [(subject, grade)]

    line = input()

for name in students:
    print(f"Student: {name[0]}")
    for subject in students[name]:
        print(f"----{subject[0]}: {subject[1]}")
    print()

