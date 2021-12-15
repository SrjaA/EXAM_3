class Tomat:
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
        self.tomatoes = list(range(self.amount))

    def grow_all(self):
        pass
    def all_are_ripe(self):
        pass
    def give_away_all(self):
        pass


class Gardener:
    def __init__(self):
        self.name = int(input('input Name: '))
        super().__init__(SmallHouse.default_area, price)

    def work(self):
        pass

    def harvest(self):
        pass
    @staticmethod
    def knowledge_base(self):
        print('Help')

Gardener.knowledge_base()
bush=TomatoBush()
gardener=Gardener()
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
