class Product:
    def __init__(self,title,calorific,cost):
        self.title = title # Название продукта
        self.calorific = calorific # Калорийность продукта только положительно число
        self.cost = cost # Себестоимость только положительное число


class Ingredient(Product):
    def __init__(self,weight):
        self.weight = weight    # Вес только положительное число
        self.product = Product()  
    
    def get_calorific(self):
        calorific_ingredient = self.weight / 100 * self.product.calorific
        return calorific_ingredient
    
    def get_cost(self):
        cost_ingredient = self.weight / 100 * self.product.cost
        return cost_ingredient

class Pizza:
    def __init__(self,title):
        self.title = title
        ingredients = Ingredient()

    def get_calorific():
        pass

    def get_cost():
        pass


