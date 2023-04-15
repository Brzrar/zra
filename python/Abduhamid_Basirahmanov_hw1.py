class Person:
    def __init__(self, fullname, age, is_married):

        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, full_name, age, is_married,):
            print(f"fullname: {full_name} \n age: {age} \n is_married: {is_married}")

class Student(Person):
    def __init__(self, fullname, age,  is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
        print(sum(self.marks) / i.marks)

class Teacher(Person):
    def __init__(self, fullname, age,  is_married, experience=3):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 15000

    def Teacher_cash(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary / 100 * 5) * (self.experience - 3))
            return new_salary


uchitel = Teacher("Harry", 30, "No", 5)
print(f'Fullname: {uchitel.fullname} Age: {uchitel.age} Married: {uchitel.is_married} experience'
      f': {uchitel.experience}')
print(uchitel.Teacher_cash())
print()
def create_students():
    student1 = Student(fullname="Maxim", age=22, is_married="No", marks={
        "biology": 5,
        "smm": 4,
        "mathematics": 3,
        "physicd": 2,
        "english": 5,
    })
    student2 = Student(fullname="Kevin", age=15, is_married="No", marks={
        "biology": 3,
        "smm": 3,
        "mathematics": 2,
        "physics": 5,
        "english": 4,
    })
    student3 = Student(fullname="Daniel", age=19, is_married="No", marks={
        "biology": 5,
        "smm": 5,
        "mathematics": 4,
        "physics": 3,
        "english": 4,
    })
    results = [student1, student2, student3]
    return results
students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Fullname: {i.fullname}\n"
          f"Age: {i.age}\n"
          f"Married: {i.is_married}\n"
          f"Average marks: {sum(list) / len(list)}\n")

