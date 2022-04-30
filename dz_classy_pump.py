

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

class Ingredient:
    def __init__(self, product, weight):
            self.product = product
            self.__weight = weight

    @property        
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self,value):
        if self.__weight <= 0:
            raise ValueError('Значение атрибута weight должно быть положительным')   
        else:
            self.__weight = value
    
    def get_calorific(self):
        calorific_ingredient = self.weight / 100 * self.product.calorific
        return calorific_ingredient
    
    
    def get_cost(self):
        cost_ingredient = self.weight / 100 * self.product.cost
        return cost_ingredient


