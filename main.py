class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 > grade > 10:
                return 'Неверный балл'
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_students_grade(self):
        sum_grade = 0
        count = 0
        for grade in self.grades.values():
            sum_grade += sum(grade)
            count += len(grade)
        return sum_grade / count

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n' \
            f'Средняя оценка за домашнее задание: {self.__average_students_grade()}\n' \
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n' \
                    f'Завершённые курсы: {', '.join(self.finished_courses)}'

    def __eq__ (self, other):
        return self.__average_students_grade() == other.__average_students_grade()
    
    def __ne__ (self, other):
        return self.__average_students_grade() != other.__average_students_grade()
    
    def __gt__ (self, other):
        return self.__average_students_grade() > other.__average_students_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_lecture_grade(self):
        sum_grade = 0
        count = 0
        for grade in self.grades.values():
            sum_grade += sum(grade)
            count += len(grade)
        return sum_grade / count
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.__average_lecture_grade()}'
    
    def __eq__ (self, other):
        return self.__average_lecture_grade() == other.__average_lecture_grade()
    
    def __ne__ (self, other):
        return self.__average_lecture_grade() != other.__average_lecture_grade()
    
    def __gt__ (self, other):
        return self.__average_lecture_grade() > other.__average_lecture_grade()
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        print(f'Имя: {self.name} \n Фамилия: {self.surname}')


def student_course_grade_point_average(students:list, course_name:str):
    avg_grade = []
    for student in students:
        if course_name in student.grades:
            avg_grade.extend(student.grades[course_name])

    return sum(avg_grade) / len(avg_grade)

def mentor_course_grade_point_average(mentors:list, course_name:str):
    avg_grade = []
    for mentor in mentors:
        if course_name in mentor.grades:
            avg_grade.extend(mentor.grades[course_name])

    return sum(avg_grade) / len(avg_grade)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'java']
second_student = Student('Leman', 'Russ', 'primarch')
second_student.courses_in_progress += ['Python', 'java', 'Space Wolves']
 
cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
second_cool_mentor = Lecturer('Once', 'Told me')
second_cool_mentor.courses_attached += ['Python', 'java']

one_reviewer = Reviewer('The world', 'Is gonna')
one_reviewer.courses_attached += ['Python', 'java']
second_reviewer = Reviewer('Roll', 'Me')
second_reviewer.courses_attached += ['Python', 'java', 'Space Wolves']

#Выставление оценок лекторам от студентов 
best_student.rate_hw(cool_mentor, 'Python', 10)
best_student.rate_hw(cool_mentor, 'Python', 8)
best_student.rate_hw(cool_mentor, 'Python', 3)
best_student.rate_hw(second_cool_mentor, 'Python', 5)

second_student.rate_hw(second_cool_mentor, 'Python', 10)
second_student.rate_hw(second_cool_mentor, 'java', 10)
second_student.rate_hw(cool_mentor, 'Python', 9)
second_student.rate_hw(second_cool_mentor, 'java', 10)

#Выставление оценок студентам от проверяющих
one_reviewer.rate_hw(best_student, 'Python', 10)
one_reviewer.rate_hw(best_student, 'Python', 7)
one_reviewer.rate_hw(second_student, 'java', 7)

second_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Space Wolves', 8)
second_reviewer.rate_hw(second_student, 'Space Wolves', 7)
second_reviewer.rate_hw(best_student, 'java', 10)

 
print(cool_mentor)
print(second_cool_mentor)
print(best_student)
print(second_student)
print(best_student > second_student)
print(best_student == second_student)
print(best_student != second_student)
print(cool_mentor < second_cool_mentor)
print(cool_mentor == second_cool_mentor)
print(cool_mentor != second_cool_mentor)
print(student_course_grade_point_average([second_student, best_student], 'Python'))
print(mentor_course_grade_point_average([second_cool_mentor, cool_mentor], 'Python'))

