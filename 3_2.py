class Tomat:
    pomidor = {1:'cvetenie', 2:'plod',3:'red',4:'salad'}


    def __init__(self):
        self._index = 0
        self._state = Tomat.pomidor[1]

    def grow(self):
        pass
    def earn_money(self, amount):

        print('Tomat is done')
class TomatoBush:
    def __init__(self, amount):
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


    def work(self):
        pass

    def harvest(self):
        pass
    @staticmethod
    def knowledge_base():
        print('Help')

Gardener.knowledge_base()
bush=TomatoBush()
gardener=Gardener()
