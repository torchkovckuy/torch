class MyClass:
    def __init__(self, name="NoName"):
        self._name = name
        print(f"Обьект {self._name} создан")

    def __del__(self):
        print(f"Обьект {self._name} удален")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

while True:
    choice = input("Создать обьект? (Да/Нет): ").strip().capitalize()
    if choice == 'Да':
        name = input("Введите имя обьекта: ")
        obj = MyClass(name)
        break
    elif choice == 'Нет':
        print("OK")
        break
    else:
        print("Неверно введено")

while True:
    try:
        choice = int(input("1 - Редактировать обьект\n2 - Удалить обьект\nДействие: "))
        if choice == 1:
            new_name = input("Создайте новое имя обьекта: ")
            obj.name = new_name
            print(f"Изменение имени обьекта {obj.name}")
        elif choice == 2:
            del obj
            break
        else:
            print("Неверный выбор")
    except ValueError:
        print("Пожалуйста выберите число")