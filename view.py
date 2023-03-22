def get_op():
    print('Для работы с телефонным справочником введите цифру нужного действия и нажмите Enter')
    print("1 - импорт данных\n2 - экспорт данных\n3 - удалить данные\n4 - изменить данные\n5 - отсортировать список\n0 - завершить работу")
    return input()

def get_op_import():
    print('\nДля импорта данных выберите нужное действие: ')
    print("0 - отмена\n1 - найти абонента по имени или фамилии\n2 - вывести всех абонентов")
    return input()

def get_op_delete():
    print('\nВыберите нужное действие: ')
    print("0 - отмена\n1 - найити и удалить\n2 - удалить все записи")
    return input()

def get_num_str():
    return input('Введите номер нужной строки: ')

def get_export():
    print('Пожалуйста, введите ФИО и телефонный номер абонента: ')
    last_name = input('Введите фамилию: ')
    name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    return f"{last_name.strip()} {name.strip()} {surname.strip()} {phone.strip()}"

def get_op_sort():
    print('Выберите параметр сортировки: ')
    print("1 - по фамилии\n2 - по имени")
    return input()

def get_name():
    print('Введите имя, либо фамилию абонента: ')
    return input()

def get_next_action():
    return input('\nВведите любое значение, чтобы продолжить. Введтие 0, чтобы завершить: ')

def print_completed():
    print('Работа завершена')
    
def print_canceled():
    print('Отменено')

def print_not_found():
    print('По вашему запросу ничего не найдено')
    

def print_error():
    print('\nВведено неверное значение! Попробуйте еще раз.')