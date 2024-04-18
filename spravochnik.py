def view():
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
            
            
def add_contact():
    count = 0
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        for line in file:
            count += 1
    s_name = input('Введите фамилию: ')
    f_name = input('Введите имя: ')
    m_name = input('Введите отчество: ')
    phone_num = input('Введите телефонный номер: ')
    contact = {
        'number_of_place': count,
        'sur_name': s_name,
        'first_name': f_name,
        'middle_name': m_name,
        'phone_number': phone_num
    }
    with open('contacts.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n')
        for key in contact:
            file.write(f'{contact[key]} ')
            
            
def search_contact():
    s_name = input('Введите фамилию человека, контакты которого хотите найти: ')
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if s_name in line:
                print(line)
                
                
def save_contact_in_own_file():
    view()
    m = int(input('Выберите номер контакта, который хотите сохранить: '))
    not_origin_file_name = input('Введите имя файла в который хотите сохранить выбранный контакт: ')
    origin_file_name = not_origin_file_name + '.txt'
    count = 0
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        for line in file:
            count += 1
            if count == m:
                saved_string = line
    with open(origin_file_name, 'a', encoding='utf-8') as file:
        file.write(f'{saved_string}\n')


def main():
    print(f'Это телефонный справочник\nЧтобы посмотреть контакты нажмите цифру 1\nЧтобы сохранить контакты нажмите цифру 2\nЧтобы найти контакты по фамилии нажмите цифру 3\nЧтобы сохранить контакты из справочника в ваши избранные нажмите цифру 4\n')
    n = int(input())
    if n == 1:
        view()
    elif n == 2:
        add_contact()
    elif n == 3:
        search_contact()
    elif n == 4:
        save_contact_in_own_file()
    input('Нажмите энтер чтобы продолжить:')
    main()
main()