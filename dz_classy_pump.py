class Product:
    def __init__(self, title, calorific, cost):
        self.__title = title
        self.calorific = calorific
        self.cost = cost

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError('Название обязательно для заполнения')
        else:
            self.__title = value

    @property
    def calorific(self):
        return self.__calorific

    @calorific.setter
    def calorific(self, value):
        if value <= 0:
            raise ValueError('Калорийность должна быть положительной')
        else:
            self.__calorific = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value <= 0:
            raise ValueError('Себестоимость должна быть положительной')
        else:
            self.__cost = value


class Ingredient():
    def __init__(self, product, weight):
            self.product = product
            self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError('Вес должен быть положительным')
        else:
            self.__weight = value

    def get_calorific(self):
        return self.weight / 100 * self.product.calorific

    def get_cost(self):
        return self.weight / 100 * self.product.cost


class Pizza (Product):
    def __init__(self, title, ingredients):
        super().__init__(title, 1, 1)
        self.ingredients = ingredients

    def get_calorific(self):
        total_calorific = 0
        for ingredient in self.ingredients:
            total_calorific += ingredient.get_calorific()
        return total_calorific

    def get_cost(self):
        total_cost = 0
        for ingredient in self.ingredients:
            total_cost += ingredient.get_cost()
        return total_cost

    def __str__(self):
        return f'{self.title} ({self.get_calorific()} kkal) - {self.get_cost()} руб'


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты.
# Для каждого ингредиента указываем продукт, из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
pizza_margarita_light = Pizza('Маргарита', [dough_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(pizza_margarita)
print(pizza_margarita_light)

