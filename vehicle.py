class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f'Nissan {self.name}')

    def about(self):
        print(f'{self.name}, цена {self.price}')


class Car:
    def __init__(self, power):
        self.power = power

    def horse_powers(self):
        return self.power


class Nissan(Vehicle, Car):
    def __init__(self, name, price, power):
        Vehicle.__init__(self, name, price)
        Car.__init__(self, power)

    def about(self):
        super().about()
        print(f'л.с. {self.horse_powers()}')


nissan = Nissan('Silvia', 3500000, 200)
nissan.info()
nissan.about()



