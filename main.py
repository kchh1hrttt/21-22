import random

quantity_persons = random.randint(5, 20)

greeting = f'''Добро пожаловать в "Героя меча и магии"!
————————————————————————————————————————
1. Создание нового персонажа
2. Создание {quantity_persons}-ти персонажей
3. Просмотр существующих персонажей\n
Ваш ответ: '''

artifacts = ['Sword', 'Stick', 'Magic Ball', 'Ring of Power', 'Amulet of Wisdom',
             'Cloak of Invisibility', 'Wand of Lightning', 'Scroll of Knowledge']

races = {
    'first_dict': {
        1: 'Elf',
        2: 'Human',
        3: 'Dwarf',
        4: 'Gnome',
        5: 'Orc'
    },
    'second_dict': {
        1: 'Elf',
        2: 'Human',
        3: 'Half-elf',
        4: 'Angel',
        5: 'Demon'
    },
    'third_dict': {
        1: 'Leonal',
        2: 'Centaur',
        3: 'Phoenix',
        4: 'Cyborg',
        5: 'Extraterrestrial'
    },
    'fourth_dict': {
        1: 'Orc',
        2: 'Vampire',
        3: 'Werewolf',
        4: 'Anthropomorphic animal',
        5: 'Mutant'
    },
    'fifth_dict': {
        1: 'Undead',
        2: 'Celestial',
        3: 'Angel',
        4: 'Forest spirit',
        5: 'Half-orc'
    }
}

names = {
    'first_dict': {
        1: 'Argo',
        2: 'Bronislav',
        3: 'Velena',
        4: 'Thunder',
        5: 'Darina'
    },
    'second_dict': {
        1: 'Astra',
        2: 'Golden Eagle',
        3: 'Vesta',
        4: 'Gavin',
        5: 'Daria'
    },
    'third_dict': {
        1: 'Alice',
        2: 'Boris',
        3: 'Victoria',
        4: 'Gregory',
        5: 'Dina'
    },
    'fourth_dict': {
        1: 'Ayla',
        2: 'Bogdan',
        3: 'Barbara',
        4: 'George',
        5: 'Elizabeth'
    },
    'fifth_dict': {
        1: 'Aurora',
        2: 'Vlad',
        3: 'Zlata',
        4: 'Daniel',
        5: 'Jeanne'
    }
}


def new_players():
    # переменным присвоены случайные словари с именами/расами из другого словаря
    race_dict = races[random.choice(list(races.keys()))]
    name_dict = names[random.choice(list(names.keys()))]

    # нумерация имён из словаря
    name_options = "\n".join(f"{index + 1}: {name}" for index, name in enumerate(name_dict.values()))
    race_options = "\n".join(f"{index + 1}: {race}" for index, race in enumerate(race_dict.values()))

    while True:
        artifact = random.choice(artifacts)
        spirit = random.randint(1, 10)
        exp = random.randint(1, 10)
        knowledge = random.randint(1, 10)

        try:
            name_key = int(input(f'''\nДайте имя вашему персонажу, из представленных ниже ↓\n{name_options}
Ваш ответ: '''))
            race_key = int(input(f'''\nВыберите расу вашему персонажу, из представленных ниже ↓\n{race_options}
Ваш ответ: '''))

            attack = int(input('\nАтака: '))
            defense = int(input('Защита: '))
            magic_power = int(input('Магическая сила: '))
            luck = int(input('Удача: '))
            sex = str(input('Пол (f/m): ').lower())
            name = name_dict[name_key]
            race = race_dict[race_key]

            character_parameters = [artifact, attack, defense, exp, knowledge,
                                    luck, magic_power, name, race, sex, spirit]

            print(format_data(character_parameters))

            for param in character_parameters:
                if isinstance(param, int) and param > 10 or isinstance(param, str) and sex not in ('f', 'm'):
                    print('\nОшибка: Какой-то из параметров указан неверно.')
                    new_players()
                    break

        except KeyError:
            print('\nОшибка: Имя или раса выбраны не верно')
            new_players()
            break
        except ValueError:
            print('\nОшибка: Неверное значение параметра')
            new_players()
            break

        answer = input('\nВсё верно? (+/-)')

        match answer:
            case '+':
                formatted_data = format_data(character_parameters, octal=True)
                write_to_data_f(formatted_data)
                break
            case '-':
                print('\nНачнём заново')
                new_players()
                break
            case _:
                print('\nНеверный ответ')


def format_data(c_parameters, octal=False):
    """
    :param c_parameters: параметры персонажа
    :param octal: в зависимости от состояния параметра, характеристики персонажа преобразовываются в восьмеричный формат
    :return: возвращает параметры персонажа, в том, или ином формате
    """

    # проверяется тип данных каждой хар-ки персонажа, int преобразовывается
    if octal:
        c_parameters = [oct(param) if isinstance(param, int) else param for param in c_parameters]

    # случайный номер персонажа
    random_num = random.randint(0, 99999999)

    formatted_data = f'''Person#{random_num}:
artifact: {c_parameters[0]}
attack: {c_parameters[1]}
defense: {c_parameters[2]}
exp: {c_parameters[3]}
knowledge: {c_parameters[4]}
luck: {c_parameters[5]}
magic_power: {c_parameters[6]}
name: {c_parameters[7]}
race: {c_parameters[8]}
sex: {c_parameters[9]}
spirit: {c_parameters[10]}'''

    return formatted_data


def write_to_data_f(data):
    with open('data.all', 'a', encoding='ASCII') as f:
        formatted_data = data.format('f')
        f.write(formatted_data + '\n\n')


def main():
    x = quantity_persons
    answer = int(input(greeting))
    match answer:
        case 1:
            new_players()
        case 2:
            while x != 0:
                new_players()
                x = x - 1
        case _:
            print('Ошибка: Такого пункта нету')


if __name__ == "__main__":
    main()
