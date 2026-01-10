student_records = []

num_records = int(input("Enter No of records- "))

for i in range(num_records):
    print(f"Enter Details of student-{i+1}")
    name = input("Enter Student name- ")
    higher_education = input("Enter Higher Education- ")
    primary_skill = input("Enter Primary Skill- ")
    graduation_year = input("Enter Year of Graduation- ")
    student_records.append((name, higher_education, primary_skill, graduation_year))

print("\nEnter Job Role Requirement")
required_skill = input("Enter Skill- ")
required_education = input("Enter Higher Education- ")
required_year = input("Enter Year of Graduation- ")

found_candidate = False
for student in student_records:
    if (student[2].lower() == required_skill.lower() and
        student[1].lower() == required_education.lower() and
        student[3] == required_year):
        print(student)
        found_candidate = True

if not found_candidate:
    print("No such candidate")