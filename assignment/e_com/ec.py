class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:

    def input_products(self):
        n = int(input('No. of products:'))
        self.prod = list()
        for i in range(n):
            name = input('Enter name: ')
            price = float(input('Enter price: '))
            quantity = int(input('Enter quantity: '))
            ob = Product(name, price, quantity)
            self.prod.append(ob)

    def cal_cost(self):
        self.total_cost = 0
        for i in self.prod:
            self.total_cost += i.price * i.quantity
        
        print(f'Total price: Rs.{self.total_cost}')

ob = Cart()
ob.input_products()
ob.cal_cost()
