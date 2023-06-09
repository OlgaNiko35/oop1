class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_rating(self):
        if not self.grades:
            return 0
        grades_list = []
        for k in self.grades.values():
            grades_list.extend(k)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return  f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за ДЗ: {self.get_average_rating()}\n' \
              f'Курсы в процессе: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Некорректно'
        return self.get_average_rating() < other.get_average_rating()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Некорректно'
        return self.get_average_rating() > other.get_average_rating()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Некорректно'
        return self.get_average_rating() == other.get_average_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,  name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def get_average_rating(self):
        if not self.grades:
            return 0
        grades_list = []
        for k in self.grades.values():
            grades_list.extend(k)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_rating()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Некорректно'
        return self.get_average_rating() < other.get_average_rating()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Некорректно'
        return self.get_average_rating() > other.get_average_rating()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Некорректно'
        return self.get_average_rating() == other.get_average_rating()

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
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


best_student = Student('Эван', 'Луиза', 'your_gender')
bad_student = Student('Августин', 'Манила', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Java']
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']
bad_student.finished_courses += ['Java']

cool_reviewer = Reviewer('Аделаида', 'Августина')
bad_reviewer = Reviewer('Майкл', 'Даниэль')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)

cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'Git', 5)
cool_reviewer.rate_hw(best_student, 'Git', 6)

bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Git']

bad_reviewer.rate_hw(bad_student, 'Python', 3)
bad_reviewer.rate_hw(bad_student, 'Python', 2)
bad_reviewer.rate_hw(bad_student, 'Python', 2)

bad_reviewer.rate_hw(bad_student, 'Git', 3)
bad_reviewer.rate_hw(bad_student, 'Git', 2)
bad_reviewer.rate_hw(bad_student, 'Git', 6)

cool_lecturer = Lecturer('Ева', 'Эдди')
bad_lecturer = Lecturer('Лина', 'Лео')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer, 'Python', 6)
best_student.rate_lect(cool_lecturer, 'Python', 10)

best_student.rate_lect(cool_lecturer, 'Git', 9)
best_student.rate_lect(cool_lecturer, 'Git', 9)
best_student.rate_lect(cool_lecturer, 'Git', 9)

bad_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['Git']

bad_student.rate_lect(bad_lecturer, 'Python', 4)
bad_student.rate_lect(bad_lecturer, 'Python', 3)
bad_student.rate_lect(bad_lecturer, 'Python', 3)

bad_student.rate_lect(bad_lecturer, 'Git', 1)
bad_student.rate_lect(bad_lecturer, 'Git', 3)
bad_student.rate_lect(bad_lecturer, 'Git', 4)

print(best_student.grades)
print(bad_student.grades)
print()
print(cool_lecturer.grades)
print(bad_lecturer.grades)
print()
print(cool_reviewer)
print(bad_reviewer)
print(cool_lecturer)
print(bad_lecturer)
print(best_student)
print(bad_student)

print()
print(f'Средняя оценка студентов по ДЗ: '
      f'{best_student.name} {best_student.surname} {"<" if best_student < bad_student  else (">" if best_student > bad_student else "=")} {bad_student.name} {bad_student.surname}')
print()

print(f'Средняя оценка за лекции: '
      f'{cool_lecturer.name} {cool_lecturer.surname} {"<" if cool_lecturer < bad_lecturer  else (">" if cool_lecturer > bad_lecturer else "=")} {bad_lecturer.name} {bad_lecturer.surname}')
print()

list_student = [best_student, bad_student]
list_lecturer = [cool_lecturer, bad_lecturer]
course_name = input('Введите название курса: ')

def student_rating(list_student, course_name):
    grades_list = []
    for student in list_student:
        grades_list.extend(student.grades.get(course_name, []))
    if not grades_list:
        return "Такого курса нет"
    return round(sum(grades_list) / len(grades_list), 2)


def lecturer_rating(list_lecturer, course_name):
    return student_rating(list_lecturer, course_name)

print()
print(f"Средняя оценка студентов по курсу {course_name}: {student_rating(list_student, course_name)}")
print()

print(f"Средняя оценка лекторов по курсу {course_name}: {lecturer_rating(list_lecturer, course_name)}")
print()
