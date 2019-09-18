#from mymodules.models import Student


def average_grade(roster):
    sum = 0
    for i in roster:
        sum += i.get_grade()
    return sum/ len(roster)

    