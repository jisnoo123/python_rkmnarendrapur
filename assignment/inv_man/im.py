class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Overload:
    def input(self):
        n = int(input('No. of items:'))
        self.items = list()
        for i in range(n):
            name = input('Enter name: ')
            quantity = int(input('Enter quantity: '))
            ob = Item(name, quantity)
            self.items.append(ob)
        
    def add_same(self):
        self.items_dict = dict()
        for i in self.items:
            self.items_dict[i.name] = self.items_dict.get(i.name, 0) + i.quantity
        print(f'Final inventory items\n{self.items_dict}')

ob = Overload()
ob.input()
ob.add_same()