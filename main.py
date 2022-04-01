
class Deck():
    def __init__(self):
        pass


    def shafl(self):
        pass


    def get_card(self):
        pass


class Card():
    def __init__(self):

        pass


class Table():
    def __init__(self):
        pass


    def compare_beat(self):
        """
        Проверяет правильность бито или нет
        если бито то позволяет подкинуть ещё карту или пас
        иначе возвращает карту в руку
        :return:
        """
        pass



class Player():
    def __init__(self):
        pass


    def check_hand(self):
        """
        :return:
        Возращает карты в руке в формате
        ---------------------------------
        id| names
        0 | card(Name)
        1 | card(Name)
        2 | card(Name)
        3 | card(Name)
        4 | card(Name)
        5 | card(Name)
        ...
        ---------------------------------
        """
        pass

    def motion_card(self,id):
        """
        Добавляет карту на стол
        :return:
        """
        pass


    def beat_card(self,id):
        """
        Бьет карту
        :return:
        """
        pass
