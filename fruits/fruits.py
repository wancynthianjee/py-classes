class Fruits:
    taste="sour"
    def __init__(self,name,price,size):
        self.name=name
        self.price=price
        self.size=size
     def fruit_name(self):
        return f'{self.name}'
    def fruit_price(self):
        return f'{self.price}'
    def fruit_size(self):
        return f'{self.size}'