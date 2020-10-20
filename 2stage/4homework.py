class Country:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent

    def country_presentation(self):
        return_country = (F"{self.name}\n {self.continent}")
        return return_country


class Brand:
    def __init__(self, brand_name, buisness_start_date):
        self.brand_name = brand_name
        self.buisness_start_date = buisness_start_date

    def brand_presentation(self):
        return_brand = (F"{self.brand_name}\n {self.buisness_start_date}")
        return return_brand


class Season:
    def __init__(self, season_name, avarage_tempriture):
        self.season_name = season_name
        self.avarage_tempriture = avarage_tempriture

    def season_presentation(self):
        return_season = (F"{self.season_name}\n {self.avarage_tempriture}")
        return return_season


class Product:
    def __init__(
    product_name, product_type, product_price, product_quantity, self,name, continent, brand_name, buisness_start_date, season_name, avarage_tempriture,):
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
        self.product_quantity = product_quantity
        Country.__init__(self, name, continent)
        Brand.__init__(self, brand_name, buisness_start_date)
        Season.__init__(self, season_name, avarage_tempriture)

    def product_presentation(self):
        print(F"{product_name}\n {product_type}\n {product_price}\n {product_quantity}")
        print(self.country_presentation())
        print(self.brand_presentation())
        print(self.season_presentation())

    def discount(self):
        return self.product_price * x / 100

    def discount(self):
        return self.product_quantity * y

apple = Product("Iphone 12 pro", "phone", "999" , "1", "USA", "North America", "Apple", "April 1, 1976", "x", "y")
apple.product_presentation()


# x_ = input("discount percent")
# x = Product(float(x_))
# print(x.discount())
