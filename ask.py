def ask():
    ask = int(input("Выберете действие 1 - изменение дынных, 2 - удаление данных, 3 - выход из программы добавления/изменения данных: "))
    return ask

def get_data():
    print("Введите новые данные ")
    name = input("Имя ")
    surname = input("Фамилия ")
    tel_number = input("Номер телефона ")
    data = name + " " + surname + " " + tel_number + "\n"
    return data

def find_str():
    data = input("Введите запрос на поиск")
    return data

def choose_str():
    line = input("Введите строку, которую нужно удалить")
    return line

def delete_data():
    data = input("Введите запрос на поиск строки для удаления")
    return data