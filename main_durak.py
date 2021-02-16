import Game_Durak as Game_Durak
Durak = Game_Durak.Durak


# Игра___________________________________________________________________________________________________
print('Игра началась!)')
print('Вводите в игру карты как удобно - пример " 9 пики, пики 9, 9пики " ')

# переменные
card_in_game_coloda_list = []  # какие карты уже были задействованы в игре
my_card_list = []  # мои карты
oponent_card_list = []  # карты опонента
ho_move = 1  # чей ход, (1) первый ход наш, (2) второй опонента
tramp = []  # козырь
tramp_name = [] # Наименование козыря
tramp_mast_rang = 0  # Ранг козырной масти

attack_card = ""
defend_card = ""
card_in_game_now = []
end_game = False



my_card_return_dict = Durak.vydat_carty_iz_colody(6, card_in_game_coloda_list)

# Раздача карт нам
my_card_return_dict = Durak.vydat_carty_iz_colody(6, card_in_game_coloda_list)
card_in_game_coloda_list = my_card_return_dict.setdefault('card_in_game_coloda_list')
my_card_list = Durak.converter_rang_in_name(my_card_return_dict.setdefault('card_list'))

print(f'Ваши карты: {my_card_list}')
# Раздача карт опоненту
oponent_card_return_dict = Durak.vydat_carty_iz_colody(6, card_in_game_coloda_list)
card_in_game_coloda_list = oponent_card_return_dict.setdefault('card_in_game_coloda_list')
oponent_card_list = Durak.converter_rang_in_name(oponent_card_return_dict.setdefault('card_list'))


# Определяем козырь
tramp_return_dict = Durak.what_trump(card_in_game_coloda_list)
tramp = tramp_return_dict.setdefault('tramp')
tramp_mast_rang = tramp_return_dict.setdefault('tramp_mast_rang')
tramp_name = tramp_return_dict.setdefault('tramp_name')


# Цикл игры
# ------------------------------------------------------------------------------
while not end_game:
    # цикл атаки
    # Наша атаки
    # ------------------------------------------------------------------------------
    while ho_move == 1:
        if len(my_card_list) == 0 or len(oponent_card_list) == 0:
            ho_move = 2
            break

        attack_card_dict = Durak.player_attack(my_card_list, card_in_game_now)

        if attack_card_dict == 'Пас':
            ho_move = 2
            break

        attack_card = attack_card_dict.setdefault('card_attack')
        # убираем из своей колоды карту которой атаковали,
        remove_list = []
        for elem in attack_card.setdefault("card_name"):
            remove_list = elem

        remove_dict = Durak.remove_card_in_list(remove_list, my_card_list)
        my_card_list = remove_dict.setdefault('card_list')
    #
        card_in_game_now = attack_card_dict.setdefault('card_in_game_now')

    # защиты опонента
        defend_card_dict = Durak.oponent_defend(attack_card, oponent_card_list, card_in_game_now, tramp_mast_rang)

        card_in_game_now = defend_card_dict.setdefault("card_in_game_now")
        oponent_card_list = defend_card_dict.setdefault("oponent_card_list")

        # Если опонент взял карты, выдаем из колоды в наш лист недостающие
        if not defend_card_dict.setdefault("defend"):
            ho_many_i_need_card = 6 - len(my_card_list)
            if ho_many_i_need_card > 0:
                my_dobor_dict = Durak.vydat_carty_iz_colody(ho_many_i_need_card, card_in_game_coloda_list)
                if my_dobor_dict != []:
                    card_in_game_coloda_list = my_dobor_dict.setdefault('card_in_game_coloda_list')
                    my_dobor_list = Durak.converter_rang_in_name(my_dobor_dict.setdefault('card_list'))
                    for elem in my_dobor_list:
                        my_card_list.append(elem)
            print(f'Ваши карты: {my_card_list}     (Козырь {tramp_name})')




    # print('мои карты',my_card_list)# мои карты
    # print('карты опонента',oponent_card_list) # карты опонента)
    # print('карты карты в игре', card_in_game_now)  # карты опонента)

# -------------------------------------------------------------------------------


# добор карт после раунда
# мои
    ho_many_i_need_card = 6 - len(my_card_list)
    ho_many_oponent_need_card = 6 - len(oponent_card_list)
    if ho_many_i_need_card > 0:
        my_dobor_dict = Durak.vydat_carty_iz_colody(ho_many_i_need_card, card_in_game_coloda_list)
        if my_dobor_dict != []:
            card_in_game_coloda_list = my_dobor_dict.setdefault('card_in_game_coloda_list')
            my_dobor_list = Durak.converter_rang_in_name(my_dobor_dict.setdefault('card_list'))
            for elem in my_dobor_list:
                my_card_list.append(elem)
    print(f'Ваши карты: {my_card_list}     (Козырь {tramp_name})')

#
# # опонент
    if ho_many_oponent_need_card > 0:
        oponent_dobor_dict = Durak.vydat_carty_iz_colody(ho_many_oponent_need_card, card_in_game_coloda_list)
        if oponent_dobor_dict != []:
            card_in_game_coloda_list = oponent_dobor_dict.setdefault('card_in_game_coloda_list')
            oponent_dobor_list = Durak.converter_rang_in_name(oponent_dobor_dict.setdefault('card_list'))
            for elem in oponent_dobor_list:
                oponent_card_list.append(elem)

    # print(f'карты опонента: {oponent_card_list}')
    card_in_game_now.clear()

# Проверка на концовку
    end_game = Durak.end_game_sign(my_card_list,oponent_card_list)
    if end_game:
        break


# цикл атаки опонента
# Атака опонента
# ------------------------------------------------------------------------------
    while ho_move == 2:

    # Если в игре уже есть карты сделаем список, чем может атаковать опонент
        chose_list = oponent_card_list
        if len(card_in_game_now) > 0:
            chose_list = []
            permited_rang_list = []
            for card_in_game in card_in_game_now:
                permited_rang_list.append(Durak.razbor_str_card(str(card_in_game)).setdefault('card_rang'))
        # print(permited_rang_list)
            for card_oponent in oponent_card_list:
                if permited_rang_list.count(Durak.razbor_str_card(str(card_oponent)).setdefault('card_rang')):
                    chose_list.append(card_oponent)
        # print('Разрешенные карты опонента',chose_list)

        if len(chose_list) == 0:
            print('Пас!')
            # Раздадим недостающие карты мне
            ho_many_i_need_card = 6 - len(my_card_list)
            ho_many_oponent_need_card = 6 - len(oponent_card_list)
            if ho_many_i_need_card > 0:
                my_dobor_dict = Durak.vydat_carty_iz_colody(ho_many_i_need_card, card_in_game_coloda_list)
                if my_dobor_dict != []:
                    card_in_game_coloda_list = my_dobor_dict.setdefault('card_in_game_coloda_list')
                    my_dobor_list = Durak.converter_rang_in_name(my_dobor_dict.setdefault('card_list'))
                    for elem in my_dobor_list:
                        my_card_list.append(elem)
            print(f'Ваши карты: {my_card_list}     (Козырь {tramp_name})')


            # Раздадим недостающие карты Опоненту

            if ho_many_oponent_need_card > 0:
                oponent_dobor_dict = Durak.vydat_carty_iz_colody(ho_many_oponent_need_card, card_in_game_coloda_list)
                if oponent_dobor_dict != []:
                    card_in_game_coloda_list = oponent_dobor_dict.setdefault('card_in_game_coloda_list')
                    oponent_dobor_list = Durak.converter_rang_in_name(oponent_dobor_dict.setdefault('card_list'))
                    for elem in oponent_dobor_list:
                        oponent_card_list.append(elem)

            # print(f'карты опонента: {oponent_card_list}')
            card_in_game_now.clear()

            ho_move = 1
            break

        min_card_dict = Durak.get_min_card(chose_list, tramp_mast_rang, 0)
        min_card_list = min_card_dict.setdefault('card_name')
        print(f'Опонент атакует: {min_card_list[0]}')

    # Удаляем катру атаки из списка карт опонента и пееводим ее в списко карт в игре
        remove_list = []
        for elem in min_card_list:
            remove_list = elem

        remove_dict = Durak.remove_card_in_list(remove_list, oponent_card_list)
        oponent_card_list = remove_dict.setdefault('card_list')
    #
        card_in_game_now.append(remove_list)
        defend_card_dict = Durak.player_defend(min_card_list, my_card_list, card_in_game_now, tramp_mast_rang)

    # Если берем карты, добавляем в наш списко карт карты в игре, раздаем опоненту недостающие карты и переходим в начало цикла
        if defend_card_dict == 'Взял':

        # my_card_list.append(min_card_list[0])
            for card in card_in_game_now:
                my_card_list.append(card)
            card_in_game_now.clear()
            ho_many_oponent_need_card = 6 - len(oponent_card_list)
            if ho_many_oponent_need_card > 0:
                oponent_dobor_dict = Durak.vydat_carty_iz_colody(ho_many_oponent_need_card, card_in_game_coloda_list)
                if oponent_dobor_dict == []:
                    print("Колода пуста!")
                if oponent_dobor_dict != []:
                    card_in_game_coloda_list = oponent_dobor_dict.setdefault('card_in_game_coloda_list')
                    oponent_dobor_list = Durak.converter_rang_in_name(oponent_dobor_dict.setdefault('card_list'))
                    for elem in oponent_dobor_list:
                        oponent_card_list.append(elem)
            print(f'Ваши карты: {my_card_list}     (Козырь {tramp_name})')
            # print(f'Карты опонента: {oponent_card_list}')
            continue

        end_game = Durak.end_game_sign(my_card_list, oponent_card_list)
        if end_game:
            break


# -------------------------------------------------------------------------------


