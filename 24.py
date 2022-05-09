
class Bankacaynt():

    def __init__(self,room,pincot,pye):
        self.__room = room
        self.__pincot = pincot
        self.__pye = pye

    def All_information(self):
        pincot = input("Pin: ")
        if self.__pincot == int(pincot):
            return f"{self.__room} {self.__pincot} {self.__pye}"
        return "Неправельный pin"

    def Top_up_card(self):
        pye = input("На какую сумму хотите пополнить карточку: ")
        self.__pye += int(pye)
        return f"{self.__pye}"

    def Xiang_money(self):
        pye2 = input("Сколько денег вы хотите снять денег с карты: ")
        self.__pye -= int(pye2)
        return f'Вы сняли денег {pye2} \nувас осталося на карте {self.__pye} '



class Bankomat(Bankacaynt):
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

emp_1 = Bankacaynt(input("Напишите номер карты: "),int(input("Напишите пинкот: ")),int(input("Напишите сколько денег у вас на карте: ")))
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
