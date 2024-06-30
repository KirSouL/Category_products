from builtins import object
from abc import ABC, abstractmethod
"""КЛАССЫ"""


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def __add__(self, other):
        pass


class MixinInit:
    """Класс примесь описания"""

    def __repr__(self):
        print(f"{self.__class__.__name__}('{self.name}', '{self.description}', {self._Product__price}, {self.quantity})")


class Product(BaseProduct, MixinInit):
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__repr__()


    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError

    @classmethod
    def new_product(cls, product: dict):
        name, description, price, quantity = product.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print(f"Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


class Category:
    """
    Класс для категорий товара
    """
    # list_name = []
    # list_products = []

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        sum_ = 0
        for i in self.__products:
            sum_ += i.quantity

        return f"{self.name}, количество продуктов: {sum_} шт."


    # def add_new_products(self):
    #     return self.__products


    # def add_new_products(self, product):
    #     if isinstance(product, LawnGrass) or isinstance(product, Smartphone) or isinstance(product, Product):
    #         self.__products.append(product)
    #         Category.category_count += 1



    @property
    def products(self):
        str_prod = ''
        for i in self.__products:
            str_prod += f"{i.name}, {i._Product__price} руб. Остаток: {i.quantity} шт.\n"
        return str_prod

    @products.setter
    def products(self, product):
        if isinstance(product, Product) or isinstance(product, Smartphone) or isinstance(product, LawnGrass):
            self.__products.append(product)
            Category.category_count += 1
        else:
            raise TypeError


class Smartphone(Product, MixinInit):
    """Класс описывающий смартфоны"""

    def __init__(self, name: str, description: str, price: int, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity * self._Product__price + other.quantity * other._Product__price
        else:
            raise TypeError

class LawnGrass(Product, MixinInit):
    """Класс описывающий траву"""

    def __init__(self, name: str, description: str, price: int, quantity: int, country: str, germination_period: str,
                     color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity * self._Product__price + other.quantity * other._Product__price
        else:
            raise TypeError
    # @property
    # def products(self):
    #     return self.__repr__()
    #
    # def __repr__(self) -> object:
    #     return Product.__str__
    # @property
    # def products(self):
    #     for i in self.__products:
    #         print(i)

    # @products.setter
    # def products(self, product: Product):
    #     self.__products.append(product)

    # @products.setter
    # def products(self, product):
    #     self.__products.append(product.new_product())
    #     self.__products.append(Product.new_product(product))
    #     Category.category_count += 1


    # @property
    # def category_count(self):
    #   return len(list_name)

    # property
    # def product_count(self):
    #   return len(list_products)

"""БАЗА ДАННЫХ"""
data = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            }
        ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55 QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }
]

"""БАЗА ЭКЗЕМПЛЯРОВ КЛАССОВ"""
categories = []
for category in data:
    products = []
    for product in category['products']:
        products.append(Product.new_product(product))
    category['products'] = products
    categories.append(Category(**category))





"""ТЕСТЫ"""

product_item = Product('Test', 'Test', 1000, 10)
product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5,  'Xiaomi', 10000, 'red')
product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')

categories[0].products = product_item
print(product_item.name in categories[0].products)

# print(product_item_3)
# # try:
# #     print(product_item + product_item_2)
# # except TypeError:
# #     print('Ошибка сложения. Нельзя складывать не экземпляры одного класса')
#
# print(product_item + product_item == 20000)
# assert categories[0].products == '''Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.
# Iphone 15, 210000.0 руб. Остаток: 8 шт.
# Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
# '''

# smart1 = Smartphone("Xiaomi Redmi Note 11", "256GB, Серый цвет, 200MP камера", 31000.0, 8, "100", "AA", "256 Гб", "Grey")
# smart2 = Smartphone("Xiaomi Redmi Note 12", "256GB, Серый цвет, 200MP камера", 52000.0, 10, "100", "AA", "256 Гб", "Grey")
# print(smart1 + smart2)
# # print(smart1 + 1)
# grass1 = LawnGrass("Зеленая трава", "Обычная трава", 100, 10, "Россия", "месяц", "Зеленая")
# grass2 = LawnGrass("Красная трава", "Редкая трава", 500, 20, "Россия", "два месяца", "Красная")
# print(grass1 + grass2)
# grass2 + 1
# product_item = Product('Test', 'Test', 1000, 10)
# product_item2 = Product('Test', 'Test', 850, 2)
# print(product_item + product_item2)
# # print(product_item.price)
# #
# # #
# # prod_ome = Product("132", "sf", 12345.0, 456)
# for product in categories:
#     cat_prod = Category("Смартфоны", "5", products)
#     print(cat_prod)
# # # print(categories)
# cat_prod.add_new_products = prod_ome
# for i in categories:
#     # print(i)
#     # print(i._Category__products, "\n")
#     oft = len(i._Category__products)
#     for j in range(oft):
#         print(i._Category__products[j].name)
# # print(categories)

# # cat_prod.products = prod_ome
# #
# # # print(cat_prod.products)
# print(cat_prod.add_new_products)


# product_item.price = 800
# print(product_item.price)

# product_item = Product('Test', 'Test', 1000, 10)
# print(product_item.price)
#
#
# product_item.price = -100
# print(product_item.price)
