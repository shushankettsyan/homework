class Fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price_kg = price
        self.kg = 0

    def presentation(self):
        text = "this is {} it's color is {} and price for kg is {}".format(self.name ,self.color, self.price_kg )
        print(text)

    def set_kg(self,kg):
        if kg > 0:
            self.kg = kg
        else:
            print(F"wrong kg{self.kg}")

Orange = Fruit("Orange", "orange", "500")
pomegranate = Fruit("Nur", "red", 1000)
print(Orange.price_kg)
print(pomegranate.price_kg)


Orange.presentation()
pomegranate.presentation()

#change kg
print(pomegranate.kg)
pomegranate.kg = 5000
print(pomegranate.kg)
print(Orange.kg)


class Car:
    def __init__(self, name, brand, color, year):
        self.name = name
        self.brand = brand
        self.color = color
        self.year = year

    def presentation(self):
        text = "this is {} it's brand is {} it's color is {} and year is {}".format(self.name ,self.brand, self.color, self.year )
        print(text)

audi = Car("Audi Etrone", "Audi", "Grey", "2019")
tesla = Car("Tesla road Star", "Tesla", "red", "2021")
mercedes = Car("Mercedes SL 55 AMG", "Mercedes", "Grey", "2002")

audi.presentation()
tesla.presentation()
mercedes.presentation()
