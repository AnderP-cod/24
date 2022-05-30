
"""from sys import stdin"""


# класс пользовательский акаунт
class Bankacaynt:
    def __init__(self, room, pincot, pye):
        self.__room = room
        self.__pincot = pincot
        self.__pye = pye

    def __add__(self):  # ввод данных и проверка их
        nu1 = 10000000000000000
        nu2 = 999999999999999
        self.__room = int(input("Напишите номер карты: "))
        if self.__room >= nu2 and self.__room <= nu1:
            self.__pincot = int(int(input("Напишите пин код: ")))
            if self.__pincot >= 1000 and self.__pincot < 10000:
                self.__pye = int(input("Напишите сколько денег "
                                       "у вас на карте: "))
                return "Вы вошли в акаунт банка"
            else:
                return "Ошибка 02: Ваш пин код не соответствует требованием"
        else:
            return "Ошибка 01: Ваш номер карты не соответствует требованием"

    def All_information(self):  # вся информация про акаунт пользователя
        pincot = input("Pin: ")
        if self.__pincot == int(pincot):
            return f"Карта {self.__room}, пинкот" \
                   f" {self.__pincot},  баланс {self.__pye}"
        return "Неправельный pin"

    def Top_up_card(self):  # функция которая позволяет ложить деньги на карту
        pincot = input("Pin: ")
        if self.__pincot == int(pincot):
            pye = input("На какую сумму хотите пополнить карточку: ")
            self.__pye += int(pye)
            return f"{self.__pye}"
        return "Неправельный pin"

    def Xiang_money(self):  # съем денег с карты
        pincot = input("Pin: ")
        if self.__pincot == int(pincot):
            pye2 = int(input("Сколько денег вы хотите снять денег с карты: "))
            if pye2 <= self.__pye:
                self.__pye -= int(pye2)
                return f'Вы сняли  {pye2} грн \n' \
                       f'у вас осталося на карте {self.__pye} '
            else:
                return "Вы хотите снять больше чем у вас на карте"
        else:
            return "Неправельный pin"


# бонкомат наследуеться от банкакаунт
class Bankomat(Bankacaynt):
    """Спомощью этого класса вызываються все функции с банкакаунта"""
    def __init__(self):
        super().__init__()

    @staticmethod
    def Bankomat_Balance_check():
        return emp_1.All_information()

    @staticmethod
    def Bankomat_Top_up_card():
        return emp_1.Top_up_card()

    @staticmethod
    def Bankomat_Xiang_money():
        return emp_1.Xiang_money()


emp_1 = Bankacaynt('', '', '')
print(emp_1.__add__())
print()
print("1) Посмотреть баланс")
print("2) Пополнить карту")
print("3) Снять деньги с карты")

item1 = input("Выберите что вы хотите сделать: 1,2,3: ")

if item1 == "1":
    print(Bankomat.Bankomat_Balance_check())
elif item1 == "2":
    print(Bankomat.Bankomat_Top_up_card())
elif item1 == "3":
    print(Bankomat.Bankomat_Xiang_money())
else:
    print("Ошибка")
