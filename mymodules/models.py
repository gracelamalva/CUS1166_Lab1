class Student:

    def __init__(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade
    
    def set_grade(self,grade):
        self.student_grade = grade
    
    def get_grade(self):
        return self.student_grade
    
    def print_student_info(self):
        print (f'Student name {self.student_name}')
        print (f'Student grade {self.student_grade}')
