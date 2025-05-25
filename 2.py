# Дано множину предметів: {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

# Список викладачів:
# 1. Олександр Іваненко, 45 років, o.ivanenko@example.com, предмети: {'Математика', 'Фізика'}
# 2. Марія Петренко, 38 років, m.petrenko@example.com, предмети: {'Хімія'}
# 3. Сергій Коваленко, 50 років, s.kovalenko@example.com, предмети: {'Інформатика', 'Математика'}
# 4. Наталія Шевченко, 29 років, n.shevchenko@example.com, предмети: {'Біологія', 'Хімія'}
# 5. Дмитро Бондаренко, 35 років, d.bondarenko@example.com, предмети: {'Фізика', 'Інформатика'}
# 6. Олена Гриценко, 42 роки, o.grytsenko@example.com, предмети: {'Біологія'}

# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects  = set()
        self.assigned_subjects = set()  # Що фактично викладач буде викладати

    def add_subject(self, subject):
        if subject not in self.can_teach_subjects:
            self.can_teach_subjects.add(subject)

    def add_subjects(self, subjects):
        for subject in subjects:
            self.add_subject(subject)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.email}, може викладати: {', '.join(self.can_teach_subjects)}"


def create_schedule(subjects, teachers):
    chosen_teachers = []
    uncovered_subjects = subjects.copy()

    while uncovered_subjects:
        # Відбираємо викладачів, які можуть викладати хоча б один з потрібних предметів
        candidates = [t for t in teachers if t.can_teach_subjects & uncovered_subjects]

        if not candidates:
            print("  ❌  Жоден викладач не може викладати:", *uncovered_subjects)
            return []

        # Вибрати кращого: найбільше покриття -> найменший вік
        best_teacher = max(
            candidates,
            key=lambda t: (len(t.can_teach_subjects & uncovered_subjects), -t.age)
        )

        # Предмети, які цей викладач покриває
        assigned = best_teacher.can_teach_subjects & uncovered_subjects
        best_teacher.assigned_subjects = assigned

        chosen_teachers.append(best_teacher)
        uncovered_subjects -= assigned

    return chosen_teachers

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # print("\n  Предмети: ")
    # print(subjects)

    # Створення списку викладачів
    teachers = []
    t1 = Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com")
    t1.add_subjects(["Математика", "Фізика"])
    teachers.append(t1)

    t2 = Teacher("Марія", "Петренко", 38, "m.petrenko@example.com")
    t2.add_subjects(["Хімія"])
    teachers.append(t2)

    t3 = Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com")
    t3.add_subjects(["Інформатика", "Математика"])
    teachers.append(t3)

    t4 = Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com")
    t4.add_subjects(["Біологія", "Хімія"])
    teachers.append(t4)

    t5 = Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com")
    t5.add_subjects(["Фізика", "Інформатика"])
    teachers.append(t5)

    t6 = Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com")
    t6.add_subjects(["Біологія"])
    teachers.append(t6)

    # Вивід усіх викладачів
    # print("\n  Викладачі: ")
    # for teacher in teachers:
    #     print(teacher)

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("\n  Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")