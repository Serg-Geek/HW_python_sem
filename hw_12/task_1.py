# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.



import csv
import os


class NameDescriptor:
    def get(self, instance, owner):
        return instance._name

    def set(self, instance, value):
        if not value.isalpha():
            raise ValueError("Имя должно содержать только буквы")

        if not value[0].isupper():
            raise ValueError("Имя должно начинаться с заглавной буквы")

        instance._name = value


class Student:
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects_file = subjects_file
        self.subjects = self.load_subjects()
        self.marks = {subj: [] for subj in self.subjects}
        self.test_results = {subj: [] for subj in self.subjects}

    def load_subjects(self):
        if not os.path.isfile(self.subjects_file):
            # Если файл отсутствует, создаем его
            with open(self.subjects_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Math", "Science", "History"])

        with open(self.subjects_file, 'r') as file:
            reader = csv.reader(file)
            subjects = next(reader)

        return subjects

    def add_mark(self, subject, mark):
        if subject not in self.subjects:
            raise ValueError(f"{subject} не является действительным предметом для этого студента")

        if mark < 2 or mark > 5:
            raise ValueError("Оценка должна быть между 2 и 5")

        self.marks[subject].append(mark)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError(f"{subject} не является действительным предметом для этого студента")

        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")

        self.test_results[subject].append(result)

    def avg_test_score_by_subject(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"{subject} не является действительным предметом для этого студента")

        test_results = self.test_results[subject]
        if not test_results:
            return 0

        return sum(test_results) / len(test_results)

    def avg_test_score_overall(self):
        total_scores = []
        total_marks = []

        for subject in self.subjects:
            test_results = self.test_results[subject]
            total_scores.extend(test_results)
            marks = self.marks[subject]
            total_marks.extend(marks)

        if not total_marks:
            return 0

        return sum(total_marks) / len(total_marks)


subjects_file = 'subjects.csv'
student = Student("John Doe", subjects_file)
student.add_mark("Math", 4)
student.add_test_result("Math", 80)
student.add_mark("Science", 5)
student.add_test_result("Science", 90)

print(student.avg_test_score_by_subject("Science"))  # Выводит средний балл по тестам для предмета "Science"
print(student.avg_test_score_overall())  # Выводит средний балл по оценкам всех предметов (без учета тестов)