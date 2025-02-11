class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                                        lecturer.grades[course].append(grade)
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка: Лектор не ведет этот курс у этого студента'

    def __str__(self):
        avg_grade = round(self.get_average_grade(), 1)  
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def get_average_grade(self):
        total_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() > other.get_average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
        self.grades = {}

    def __str__(self):
        avg_grade = round(self.get_average_grade(), 1)  
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")

    def get_average_grade(self):
        total_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() > other.get_average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_student = Student("Ruoy", "Eman", "your_gender")
some_student.courses_in_progress = ["Python", "Git"]
some_student.finished_courses = ["Введение в программирование"]
some_student.grades = {"Python": [10, 10, 9], "Git": [10, 8, 9]}

some_student2 = Student("Ivan", "Dude", "your_gender")
some_student2.courses_in_progress = ["Python", "Git"]
some_student2.finished_courses = ["Введение в программирование"]
some_student2.grades = {"Python": [8, 7, 8], "Git": [7, 6, 8]}

some_lecturer = Lecturer("Some", "Buddy", ["Python"])
some_lecturer.grades = {"Python": [9, 9, 10]}

some_lecturer2 = Lecturer("Brad", "Pitt", ["Git"])
some_lecturer2.grades = {"Git": [8, 9, 8]}

some_reviewer = Reviewer("Some", "Buddy", ["Python"])

print(some_reviewer)
print(some_lecturer)
print(some_student)

print(f"Student1 > Student2: {some_student > some_student2}")
print(f"Lecturer1 > Lecturer2: {some_lecturer > some_lecturer2}")

def average_grade_for_course_students(student_list, course):
    total_grades = []
    for student in student_list:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return round(sum(total_grades) / len(total_grades), 1)
    return 0


def average_grade_for_course_lecturers(lecturer_list, course):
    total_grades = []
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return round(sum(total_grades) / len(total_grades), 1)
    return 0

student_list = [some_student, some_student2]
lecturer_list = [some_lecturer, some_lecturer2]

python_average = average_grade_for_course_students(student_list, "Python")
git_average = average_grade_for_course_lecturers(lecturer_list, "Git")

print(f"Средняя оценка за Git среди лекторов: {git_average}")
print(f"Средняя оценка за Python среди студентов: {python_average}")