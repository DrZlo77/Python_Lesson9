import random

class Durak:

    # def __init__(self,n,card_in_game_coloda_list,my_card_list,oponent_card_list,ho_move,tramp,tramp_name,tramp_mast_rang,attack_card,defend_card,card_in_game_now,end_game):
        # self.card_in_game_coloda_list=card_in_game_coloda_list
        # self.my_card_list = my_card_list
        # self.oponent_card_list = oponent_card_list
        # self.ho_move = ho_move
        # self.tramp = tramp
        # self.tramp_name = tramp_name
        # self.tramp_mast_rang = tramp_mast_rang
        # self.attack_card = attack_card
        # self.defend_card = defend_card
        # self.card_in_game_now = card_in_game_now
        # self.end_game = end_game

    # Выдаем карты которые еще остаются в колоде, n - количество необходимых для выдачи карт
    # Карты обозначаются рангами и номерами мастей
    def vydat_carty_iz_colody(n, card_in_game_coloda_list):
        card_list = []

        rezerv_card = 36 - len(card_in_game_coloda_list)
        if rezerv_card < n:
            n = rezerv_card

        rezerv_card -= n
        # print(rezerv_card)

        if n <= 0:
            return []

        for i in range(n):
            karta = random.randint(1, 9)
            mast = random.randint(1, 4)
            while card_in_game_coloda_list.count([karta, mast]) == 1:
                karta = random.randint(1, 9)
                mast = random.randint(1, 4)
            card_list.append([karta, mast])
            card_in_game_coloda_list.append([karta, mast])

        return_dict = {'card_list': card_list, 'card_in_game_coloda_list': card_in_game_coloda_list}

        # print(card_list)
        return return_dict

    # возвращает наименование карты в зависимости от ранга
    # 6, 7, 8, 9, 10, Валет, Дама, Король, Туз
    def what_card(rang_numer_card):
        if rang_numer_card == 1:
            return 6
        elif rang_numer_card == 2:
            return 7
        elif rang_numer_card == 3:
            return 8
        elif rang_numer_card == 4:
            return 9
        elif rang_numer_card == 5:
            return 10
        elif rang_numer_card == 6:
            return "Валет"
        elif rang_numer_card == 7:
            return "Дама"
        elif rang_numer_card == 8:
            return "Король"
        elif rang_numer_card == 9:
            return "Туз"

    # возвращает ранг карты в зависимости от наименование
    # Валет, Дама, Король, Туз => 6,7,8,9
    def what_rang(name_card):
        if name_card == "6":
            return 1
        elif name_card == "7":
            return 2
        elif name_card == "8":
            return 3
        elif name_card == "9":
            return 4
        elif name_card == "10":
            return 5
        elif name_card == "Валет" or name_card == "валет":
            return 6
        elif name_card == "Дама" or name_card == "дама":
            return 7
        elif name_card == "Король" or name_card == "король":
            return 8
        elif name_card == "Туз" or name_card == "туз":
            return 9

    # возвращает наименование масти в зависимости от номера
    # Пики, Крести, Бубны,Червы
    def what_mast(mast_numer):
        if mast_numer == 1:
            return "Пики"
        elif mast_numer == 2:
            return "Крести"
        elif mast_numer == 3:
            return "Бубны"
        elif mast_numer == 4:
            return "Червы"
        else:
            return False

    # возвращает номер масти в зависимости от наименования
    # Пики, Крести, Бубны,Червы
    def what_mast_number(mast_name):
        if mast_name == "пики" or mast_name == "Пики":
            return 1
        elif mast_name == "крести" or mast_name == "Крести":
            return 2
        elif mast_name == "бубны" or mast_name == "Бубны":
            return 3
        elif mast_name == "червы" or mast_name == "Червы":
            return 4
        else:
            return False

    # Преобразователь: Из рангов и номеров мастей в читабельный вид
    # (6,1) => Валет Пик
    def converter_rang_in_name(rang_card_list):
        card_name_list = []
        for elem in rang_card_list:
            card_name_list.append([Durak.what_card(elem[0]), Durak.what_mast(elem[1])])
        return card_name_list

    # Преобразователь: Из наименования карты в ранги
    # Валет Пик => (6,1)
    def converter_name_in_rang(name_card_list):
        card_name_list = []
        # for elem in rang_card_list:
        for elem in name_card_list:
            card_name_list.append([Durak.what_card(elem[0]), Durak.what_mast(elem[1])])
        return card_name_list

    # определяем козырь
    # выбираем первую карту из оставшейся колоды как козырь
    # заполняем глобальные переменные
    def what_trump(card_in_game_coloda_list):
        tramp=[]
        card_in_coloda = []
        tramp_list = []
        for i in range(24):
            karta = random.randint(1, 9)
            mast = random.randint(1, 4)
            while card_in_game_coloda_list.count([karta, mast]) == 1:
                karta = random.randint(1, 9)
                mast = random.randint(1, 4)
            card_in_coloda.append([karta, mast])  # колода оставшихся после раздачи игрокам карт
        tramp.append(card_in_coloda[0])  # первая карта из оставшихся

        tramp_name = str(Durak.converter_rang_in_name(tramp))
        print(f"Козырь: {tramp_name}")
        tramp_dict = Durak.razbor_str_card(tramp_name)

        tramp_mast_rang = tramp_dict.setdefault('mast_rang')

        tramp_return_dict = {'tramp': tramp, 'tramp_mast_rang': tramp_mast_rang, 'tramp_name': tramp_name}
        return tramp_return_dict

    # Определим какая карта в строке
    # запишем "красиво" в список для дальнейшей обработки
    def razbor_str_card(card):
        # масть
        mast_name = ""

        if card.find("червы") != -1 or card.find("Червы") != -1:
            mast_name = "Червы"
        elif card.find("пики") != -1 or card.find("Пики") != -1:
            mast_name = "Пики"
        elif card.find("крести") != -1 or card.find("Крести") != -1:
            mast_name = "Крести"
        elif card.find("бубны") != -1 or card.find("Бубны") != -1:
            mast_name = "Бубны"

        if mast_name == "":
            print(f'Не найдено наименование МАСТИ в карте {card}')
            return False

        # карта
        card_name = ""

        if card.find("6") != -1:
            card_name = "6"
        elif card.find("7") != -1:
            card_name = "7"
        elif card.find("8") != -1:
            card_name = "8"
        elif card.find("9") != -1:
            card_name = "9"
        elif card.find("10") != -1:
            card_name = "10"
        elif card.find("валет") != -1 or card.find("Валет") != -1:
            card_name = "Валет"
        elif card.find("дама") != -1 or card.find("Дама") != -1:
            card_name = "Дама"
        elif card.find("король") != -1 or card.find("Король") != -1:
            card_name = "Король"
        elif card.find("туз") != -1 or card.find("Туз") != -1:
            card_name = "Туз"

        if card_name == "":
            print(f'Не найдено эталонное наименование Карты {card}')
            return False

        mast_rang = Durak.what_mast_number(mast_name)
        card_rang = Durak.what_rang(card_name)

        if mast_rang == False:
            print(f'Не найден РАНГ масти в Карте {card}')
            return False
        if card_rang == False:
            print(f'Не найден РАНГ карты {card}')
            return False

        card_list = []
        card_list.append([card_name, mast_name])
        # print(card_list)

        card_dict = {'card_name': card_list, 'card_rang': card_rang, 'mast_rang': mast_rang}

        return card_dict

    # определим какая карта сильнее
    # параметры - карта атаки, карта защиты, возвращаем True - побился, False - не побился или непонятные карты
    def ho_iz_stronger(attack_card, defender_card, tramp_mast_rang):
        attack_card_dict = Durak.razbor_str_card(attack_card)
        # print(attack_card_dict)

        defender_card_dict = Durak.razbor_str_card(defender_card)
        # print(defender_card_dict)

        if attack_card_dict == False:
            print("Напишите Атакующую карту")
            return False
        if defender_card_dict == False:
            print("Напишите Защитную карту")
            return False

        # получаем раги для сравнения
        # карта атаки
        attack_card_rang = attack_card_dict.setdefault('card_rang')
        attack_card_mast_rang = attack_card_dict.setdefault('mast_rang')

        # print(attack_card_rang)
        # print(attack_card_mast_rang)
        # карта защиты
        defender_card_rang = defender_card_dict.setdefault('card_rang')
        defender_card_mast_rang = defender_card_dict.setdefault('mast_rang')

        # print(defender_card_rang)
        # print(defender_card_mast_rang)

        # козырь масть
        if tramp_mast_rang == 0:
            print("Назначте козырную карту")
            return False
        trump_card_mast_rang = tramp_mast_rang

        # Если масти совпадают
        if attack_card_mast_rang == defender_card_mast_rang:
            # print("Совпадение мастей")
            if attack_card_rang < defender_card_rang:
                # print('Побился')
                return True
            else:
                # print('Не побился')
                return False

        # Если масти НЕ совпадают
        if attack_card_mast_rang != defender_card_mast_rang:
            # print("НЕт Совпадение мастей")
            if attack_card_mast_rang == trump_card_mast_rang:
                # print('Не побился')
                return False
            elif defender_card_mast_rang == trump_card_mast_rang:
                # print('Побился')
                return True
            else:
                # print('Не побился')
                return False

    # Проверка -  Может ли игрок походить этой картой, есть ли она у него
    def can_player_go_card(card, my_card_list):
        card_dict = Durak.razbor_str_card(card)

        if card_dict != False:
            card_rang = card_dict.setdefault('card_rang')
            card_mast = card_dict.setdefault('mast_rang')

            for card_in in my_card_list:
                card_in_dict = Durak.razbor_str_card(str(card_in))
                card_in_rang = card_in_dict.setdefault('card_rang')
                card_in_mast = card_in_dict.setdefault('mast_rang')
                if card_rang == card_in_rang and card_mast == card_in_mast:
                    return True
        return False

    # Наш ход, проверка вводит ли игрок карту которая есть в его колоде
    def player_go(card, my_card_list, comand):
        # card = input('Ваш ход! Введите карту:')
        ok = Durak.can_player_go_card(card, my_card_list)
        while not ok:
            card = input(f'Введите карту снова или команду {comand}:')

            if card.find(comand) != -1 or card.find(comand) != -1:
                return comand

            ok = can_player_go_card(card, my_card_list)
        return card

    # Опонент отбивает атаку
    def oponent_defend(attack_card, oponent_card_list, card_in_game_now, tramp_mast_rang):
        defend = False
        defend_card_list = []

        for card in oponent_card_list:
            # print(attack_card,card,oponent_card_list)
            if Durak.ho_iz_stronger(str(attack_card.setdefault('card_name')), str(card), tramp_mast_rang):
                defend_card_list.append(card)

        # print(attack_card)
        # print(oponent_card_list)
        # print(card_in_game_now)

        if len(defend_card_list) == 0:
            print('Взял!')

            for elem in attack_card.setdefault('card_name'):
                oponent_card_list.append(elem)

            # oponent_card_list.append(attack_card.setdefault('card_name'))
            attack_card.clear()

            for elem in card_in_game_now:
                oponent_card_list.append(elem)
            card_in_game_now.clear()
            return {"defend": False, "oponent_card_list": oponent_card_list, "card_in_game_now": card_in_game_now}

        defend_card_dict = Durak.get_min_card(defend_card_list, tramp_mast_rang, 0)

        for elem in defend_card_dict.setdefault('card_name'):
            defend_card_list = elem

        print('Побил!', defend_card_list)

        card_in_game_now.append(defend_card_list)

        for elem in attack_card.setdefault('card_name'):
            card_in_game_now.append(elem)

        remove_dict = Durak.remove_card_in_list(defend_card_list, oponent_card_list)
        oponent_card_list = remove_dict.setdefault('card_list')

        return {"defend": True, "oponent_card_list": oponent_card_list, "card_in_game_now": card_in_game_now}

    # Атакуем опонента
    def player_attack(my_card_list, card_in_game_now):
        card = input('Ваш ход! Введите карту или команду Пас:')

        if card.find('пас') != -1 or card.find('Пас') != -1:
            return "Пас"
        command = "Пас"
        card = Durak.player_go(card, my_card_list, command)
        atack_card = Durak.razbor_str_card(card);

        # Если уже есть карты в игре, проверяем может ли игрок атаковать именно этой картой
        if len(card_in_game_now) > 0:
            can_attack_this_card = False
            while not can_attack_this_card:
                for card_in_game in card_in_game_now:
                    if atack_card.setdefault('card_rang') == Durak.razbor_str_card(str(card_in_game)).setdefault('card_rang'):
                        can_attack_this_card = True
                    # card_in_game_now.append(atack_card)
                if not can_attack_this_card:
                    card = input(f'Введите карту снова или команду {command}:')
                    card = Durak.player_go(card, my_card_list, command)
                    atack_card = Durak.razbor_str_card(card);

        return {'card_attack': atack_card, 'card_in_game_now': card_in_game_now}

    def player_defend(atack_card, my_card_list, card_in_game_now, tramp_mast_rang):
        card = input('Защищайтесь! Введите карту или команду Взял:')
        if card.find('Взял') != -1 or card.find('взял') != -1:
            return "Взял"
        command = "Взял"
        defend_card = Durak.player_go(card, my_card_list, command)
        defend = Durak.ho_iz_stronger(str(atack_card), defend_card, tramp_mast_rang)
        if defend:
            print("Побил!")

        if not defend:
            card = input('Защищайтесь! Введите карту или команду Взял:')
            if card.find('Взял') != -1 or card.find('взял') != -1:
                return "Взял"
            command = "Взял"
            defend_card = Durak.player_go(card, my_card_list, command)
            defend = Durak.ho_iz_stronger(str(atack_card), defend_card, tramp_mast_rang)

        # добавляем карту защиты в список карт в игре
        defend_card_dict = Durak.razbor_str_card(defend_card)
        for elem in defend_card_dict.setdefault('card_name'):
            defend_card_list = elem
        card_in_game_now.append(defend_card_list)

        # удаляем карту защиты из карт игрока

        remove_dict = Durak.remove_card_in_list(defend_card_list, my_card_list)
        my_card_list = remove_dict.setdefault('card_list')

        return {'defend': defend, 'my_card_list': my_card_list, 'card_in_game_now': card_in_game_now}

    # Функция выбора минимальной карты
    def get_min_card(card_list, tramp_mast_rang, mast_rang):
        # mast_rang - если нужно выбрать минимальную карьу определенной масти
        # print(card_list)
        card_rang_list = []  # получаем список со всеми возможными данными о картах
        for card in card_list:
            card_rang_list.append(Durak.razbor_str_card(str(card)))

        # Узнаем не все ли карты козырные
        all_tramp = True
        for card_dict in card_rang_list:
            if tramp_mast_rang != card_dict.setdefault('mast_rang'):
                all_tramp = False

        # Если не все карты козырные исключаем козыри из обхода
        min_card_dict = {}
        # Если не нужна определенная масть и не козырные карты
        if mast_rang == 0 and not all_tramp:
            for card_dict in card_rang_list:
                # заполним первую карту
                if min_card_dict == {} and card_dict.setdefault('mast_rang') != tramp_mast_rang:
                    min_card_dict = card_dict
                # после заполнения первой карты продолжаем обход
                if min_card_dict != {}:
                    if min_card_dict.setdefault('card_rang') > card_dict.setdefault(
                            'card_rang') and card_dict.setdefault(
                            'mast_rang') != tramp_mast_rang:
                        min_card_dict = card_dict

        # Если не нужна определенная масть и все козырные карты
        if all_tramp:
            # for card_dict in card_rang_list:
            #     min_card_dict = card_dict

            for card_dict in card_rang_list:
                # # заполним первую карту
                if min_card_dict == {} and card_dict.setdefault('mast_rang') == tramp_mast_rang:
                    min_card_dict = card_dict
                # после заполнения первой карты продолжаем обход
                if min_card_dict.setdefault('card_rang') > card_dict.setdefault('card_rang'):
                    min_card_dict = card_dict

        # Если нужна определенная масть и не козырные карты
        if not all_tramp and mast_rang > 0:
            for card_dict in card_rang_list:
                # заполним первую карту
                if min_card_dict == {} and card_dict.setdefault(
                        'mast_rang') != tramp_mast_rang and mast_rang == card_dict.setdefault('mast_rang'):
                    min_card_dict = card_dict
                # после заполнения первой карты продолжаем обход
                if min_card_dict != {}:
                    if min_card_dict.setdefault('card_rang') > card_dict.setdefault(
                            'card_rang') and mast_rang == card_dict.setdefault('mast_rang'):
                        min_card_dict = card_dict

        # Если нужна определенная масть и она совпадает с козырем
        if tramp_mast_rang == mast_rang:
            for card_dict in card_rang_list:
                # заполним первую карту
                if min_card_dict == {} and mast_rang == card_dict.setdefault('mast_rang'):
                    min_card_dict = card_dict
                    # после заполнения первой карты продолжаем обход
                    if min_card_dict != {}:
                        if min_card_dict.setdefault('card_rang') > card_dict.setdefault(
                                'card_rang') and mast_rang == card_dict.setdefault('mast_rang'):
                            min_card_dict = card_dict

        # print(min_card_dict)
        return min_card_dict

    # Убираем карту из списка
    def remove_card_in_list(card, card_list):
        remove_list = []
        for elem in card_list:
            if str(elem[0]) == str(card[0]):
                if str(elem[1]) == str(card[1]):
                    remove_list = elem
        card_list.remove(remove_list)
        return {'card_list': card_list}

    def end_game_sign(my_card_list, oponent_card_list):
        # Проверка на концовку
        if len(oponent_card_list) == 0 and len(my_card_list) > 0:
            print("ВАШ ОПОНЕНТ ВЫИГРАЛ ПАРТИЮ!")
            return True

        if len(my_card_list) == 0 and len(oponent_card_list) > 0:
            print("!!!ВЫ ВЫИГРАЛИ ПАРТИЮ!!!!")
            return True

        if len(my_card_list) == 0 and len(oponent_card_list) == 0:
            print("!!!ПАРТИЯ СЫГРАНА В НИЧЬЮ!!!!")
            return True

        return False

