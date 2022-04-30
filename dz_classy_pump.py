class Title:
    def __init__(self,title):
       if len(title) == 0:
            raise NameError('Поле title должно быть обьязательно заполнено')
       else:
           self.title = title
       return self.title



class Product(Title):
    def __init__(self,title,calorific, cost):
        if calorific < 0:
            raise ValueError('Значение атрибута calorific только положительное число')
        elif cost < 0:
            raise ValueError('Значение cost только положительное число')    
        else:    
            self.title = super().__init__(title) # Название продукта
            self.calorific = calorific # Калорийность продукта только положительно число
            self.cost = cost # Себестоимость только положительное число

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
            raise ValueError('Значение атрибута calorific только положительное число')
        else:
            self.__calorific = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value <= 0:
            raise ValueError('Значение cost только положительное число')
        else:
            self.__cost = value                

class Ingredient():
    def __init__(self,Product,weight):
        self.__weight = weight    # Вес только положительное число
        self.product = Product

    @property        
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self):
        if self.__weight <= 0:
            raise ValueError('Значение атрибута weight должно быть положительным')   
    
    @property
    def get_calorific(self):
        calorific_ingredient = self.weight / 100 * self.product.calorific
        return calorific_ingredient
    
    @property
    def get_cost(self):
        cost_ingredient = self.weight / 100 * self.product.cost
        return cost_ingredient


class Pizza(Product):
    def __init__(self,title,ingredients:list):
        self.title = super().__init__(title,1,1)
        self.ingredients = ingredients

    @property
    def get_calorific(self):
        sum_calorific = 0
        for ingred_calorific in self.ingredients:
            sum_calorific += ingred_calorific.get_calorific
        return sum_calorific
   
    @property
    def get_cost(self):
        sum_cost = 0
        for ingred_cost in self.ingredients:
            sum_cost += ingred_cost.get_cost      
        return sum_cost

    def __str__(self):
        return f'{self.title} ({self.get_calorific} kkal) - {self.get_cost} руб'  

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
pizza_margarita_light = Pizza('Маргарита лайт', [dough_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(pizza_margarita)
print(pizza_margarita_light)
