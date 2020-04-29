class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0
        


    def can_add(self, v):
        if self.coins + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.coins = self.coins + v
            print('{} coin(s) added successfully.'.format(v))
        else:
            print('{} coin(s) cannot be added to MoneyBox \n It exceeds the capacity of {}'.format(v,self.capacity))


moneybox1 = MoneyBox(5)

moneybox1.add(3)
moneybox1.add(17)
print(moneybox1.coins)
    
