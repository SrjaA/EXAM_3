class Tomat:
    # Статические поля
    pomidor = {1:'cvetenie', 2:'plod',3:'red',4:'salad'}


    def __init__(self):
        self._index = 0
        self._state = Tomat.pomidor[1]

    def grow(self):
        self.sost += 1
    def earn_money(self, amount):

        print('Tomat is done')
class TomatoBush:
    def __init__(self):
        self.amount = int(input('input tomato amount: '))
        self.list = list(TomatoBush.amount)
    # Статический метод
    @staticmethod
    def default_info():
        print('Default Name:', Human.default_name)
        print('Default Age: ', Human.default_age)



    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
        else:
            print('Not enough money!')

    # Приватный метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print('Final price: ', final_price)
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':
    Human.default_info()

    alexander = Human('Sasha', 27)
    alexander.info()

    small_house = SmallHouse(8500)

    alexander.buy_house(small_house, 5)

    alexander.earn_money(5000)
    alexander.buy_house(small_house, 5)

    alexander.earn_money(20000)
    alexander.buy_house(small_house, 5)
    alexander.info()
