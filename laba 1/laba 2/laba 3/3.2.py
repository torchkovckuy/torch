class Worker:
    def __init__(self, name, surname, rate, days):
        self._name = name
        self._surname = surname
        self._rate = rate
        self._days = days

    def GetSalary(self):
        return self._rate * self._days

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def rate(self):
        return self._rate

    @property
    def days(self):
        return self._days

workers = []

while True:
    choice = int(input("1 - Добавить сотрудника\n2 - Показать зарплату\n3 - Вывести список сотрудников\n4 - Выход\nВыберите действие: "))
    if choice == 1:
        name = input("Имя: ")
        surname = input("Фамилия: ")
        rate = int(input("Ставка за день: "))
        days = int(input("Отработанные дни: "))
        workers.append(Worker(name, surname, rate, days))
    elif choice == 2:
        print("Список сотрудников:")
        for i in range(len(workers)):
            print(f"{i + 1}. {workers[i].name} {workers[i].surname}")
            number = int(input("Номер сотрудника: ")) - 1
            print(f"Зарплата: {workers[number].GetSalary()}")
    elif choice == 3:
        print("Список сотрудников:")
        for i in range(len(workers)):
            print(f"{i + 1}. {workers[i].name} {workers[i].surname} {workers[i].rate} {workers[i].days}")
    elif choice == 4:
        break