#симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #список студентів
        self.teachers = [] #1 завдання
        self.classes = [] #2 завдання
    def admit_student(self, student): #зарахування студентів
        self.students.append(student)
        print(f'{student.name} був доданий до школи {self.name}') #дописати, коли створимо клас студентів
    def expel_student(self, student):
        expelled_student =  next(filter(lambda s: s.name == student.name
                                                  and s.grade == student.grade, self.students), None)
        if expelled_student is not None:
            self.students.remove(expelled_student)
            print(f'{expelled_student.name} був видалений з {self.name}')
        else:
            print(f'{student.name} не був знайдений {self.name}')
    #1 завдання
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    def add_class(self, class_obj):
        self.classes.append(class_obj)
    def get_school_statistics(self):
        num_students = len(self.students)
        if num_students == 0:
            avg_grade = 0
        else:
            avg_grade = sum(student.grade for student in self.students) / num_students
        return f"на {num_students} студентів середня оцінка по школі {avg_grade}"

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade +=  1
        print(f'{self.name} був підвищений {self.grade}')
    def demote(self):
        self.grade -=  1
        print(f'{self.name} був понижений {self.grade}')
    def __str__(self):
        return f'{self.name} - Ранг {self.grade}'

lisa = Student("Alisa", 6)
masha = Student("Maria", 2)
andriiko = Student("Andriy", 50)
dima = Student("Dmytro", 23)
gleb = Student("Gleb", 100)
my_school = School("ItStep", [lisa, masha, andriiko, dima, gleb])
print("Початкові студенти")
for student in my_school.students:
    print(student)

my_school.admit_student(Student("Bogdan", 3))
my_school.expel_student(Student("Alisa", 6))
print("Оновлення")
for student in my_school.students:
    print(student)
#Практична робота
#перше завдання
class Teacher:
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes
#друге завдання
class Class:
    def __init__(self, number):
        self.number = number
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    #3
    def get_avarage_grade(self):
        total_grades = 0
        for student in self.students:
            total_grades += student.grade
        return total_grades / len(self.students)
