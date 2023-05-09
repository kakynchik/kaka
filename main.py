class school:
    def __init__(self, name, students):
        self.name = name
        self.students = students
    def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} byv dodani do shkoli {self.name}')
    def expel_student(self, student):
        expelled_student = next(filter(lambda s: s.name == student.name and
                                                 s.grade == student.grade, self.students), None)
        if expelled_student is not None:
            self.students.remove(expelled_student)
            print(f'{expelled_student.name} byv vydalenniy z {self.name}')
        else:
            print(f'{student.name} nema takogo {self.name}')
        #1
        def add_teacher(self, teacher):
            self.teacher.append(teacher)
        def add_class(self, class_obj):
            self.classes.append(class_obj)


class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade += 1
        print(f'{self.name} byv pidvisheniy {self.grade}')
    def promote(self):
        self.grade -= 1
        print(f'{self.name} byl ponizheniy {self.grade}')
    def __str__(self):
        return f'{self.name} - Rang {self.grade}'



multiply = lambda x, y: x * y
print(multiply(2, 5))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filter_numbers)

lisa = student("Alisa", 6)
masha = student("Maria", 2)
andriyko = student("Andriy", 50)
dima = student("Dmytro", 23)
hleb = student("Glib", 100)
my_school = school("ItStep", [lisa, masha, andriyko, dima, hleb])
print("pochatkovi studenty")
for students in my_school.students:
    print(student)


my_school.admit_student(Student("bodya", 3))
my_school.admit_student(Student("Alisa", 6))
print("obnova")
for student in my_school.students:
    print(student)
    #pershe
class Teacher:
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes
#2
class Class:
    def __init__(self, number):
        self.number = number
        self.students = []
    def add_student(self, student):
        self.students.appent(student)
