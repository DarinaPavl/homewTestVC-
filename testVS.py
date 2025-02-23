def calculate_average(grades):
    all_grades = []
    for grades_list in grades.values():
        all_grades.extend(grades_list)
    return sum(all_grades) / len(all_grades) if all_grades else 0



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_average_grade(self):
        return calculate_average(self.grades)

    def __str__(self):
        average_grade = self.calculate_average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {average_grade:.1f}\n'
            f'Курсы в процессе изучения: {courses_in_progress_str}\n'
            f'Завершенные курсы: {finished_courses_str}\n'
        )

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() == other.calculate_average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() != other.calculate_average_grade()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() <= other.calculate_average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() > other.calculate_average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() >= other.calculate_average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculate_average_grade(self):
        return calculate_average(self.grades)

    def __str__(self):
        average_grade = self.calculate_average_grade()
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {average_grade:.1f}\n'
        )

    # Магические методы сравнения
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() == other.calculate_average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() != other.calculate_average_grade()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() <= other.calculate_average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() > other.calculate_average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() >= other.calculate_average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
        )

def calculate_average_hw_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0

def calculate_average_lecture_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0

# Создание объектов
student1 = Student('Ruoy', 'Eman', 'female')
student1.courses_in_progress += ['Python', 'Git']
student1.grades = {'Python': [10, 9, 8], 'Git': [7, 8]}
student2 = Student('Merry', 'Bro', 'female')
student2.courses_in_progress += ['Python', 'Git']
student2.grades = {'Python': [9, 8, 7], 'Git': [6, 7]}

lecturer1 = Lecturer('John', 'Doe')
lecturer1.courses_attached += ['Python', 'Git']
lecturer1.grades = {'Python': [10, 10, 9], 'Git': [8, 9]}
lecturer2 = Lecturer('Tigr', 'Li')
lecturer2.courses_attached += ['Python', 'Git']
lecturer2.grades = {'Python': [9, 8, 8], 'Git': [7, 8]}

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'Git']
reviewer2 = Reviewer('Len', 'Shushpp')
reviewer2.courses_attached += ['Python', 'Git']

# Выставление оценок студенту
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Git', 7)

student1.rate_lec(lecturer1, 'Python', 10)
student1.rate_lec(lecturer1, 'Git', 8)
student2.rate_lec(lecturer2, 'Python', 9)
student2.rate_lec(lecturer2, 'Git', 7)

# Печать информации об объектах
print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)

# Подсчёт средних оценок
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

average_hw_grade_python = calculate_average_hw_grade(students, 'Python')
average_lecture_grade_python = calculate_average_lecture_grade(lecturers, 'Python')

print(f"\nСредняя оценка за домашние задания по курсу Python: {average_hw_grade_python:.1f}")
print(f"Средняя оценка за лекции по курсу Python: {average_lecture_grade_python:.1f}")


# Сравнение студентов
print("\nСравнение студентов:")
print(f"Студент 1 > Студент 2: {student1 > student2}")  # True
print(f"Студент 1 == Студент 2: {student1 == student2}")  # False
print(f"Студент 1 < Студент 2: {student1 < student2}")  # False

# Сравнение лекторов
print("\nСравнение лекторов:")
print(f"Лектор 1 > Лектор 2: {lecturer1 > lecturer2}")  # True
print(f"Лектор 1 == Лектор 2: {lecturer1 == lecturer2}")  # False
print(f"Лектор 1 < Лектор 2: {lecturer1 < lecturer2}")  # False
