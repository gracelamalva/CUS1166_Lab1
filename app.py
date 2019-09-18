from mymodules.models import Student
from mymodules.math_utils import average_grade


roster = [
    Student("Kevin",100),
    Student("Kelly",93),
    Student("Toby",88),
    Student("Michael",62),
    Student("Creed",91),
    Student("Phyllis",71),
    Student("Stanley",88),
    Student("Dwight",80),
    Student("Pam",80),
    Student("Jim",92)
    ]

for i in roster:
    i.print_student_info()

print(f"The Roster's Average is {str(average_grade(roster))}")