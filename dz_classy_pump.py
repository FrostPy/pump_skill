class Title:
    def __init__(self,title = ''):
       if title == '':
            raise NameError('Поле title должно быть обьязательно заполнено')
       else:
           self.title = title
       



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


      

class Ingredient:
    def __init__(self,product = Product,weight = 0):
           if weight <= 0:
             raise ValueError('Значение weigh только положительно число')
           else:
              self.weight = weight
              self.product = product
       

            
    @property
    def get_calorific(self):
        calorific_ingredient = self.weight / 100 * self.product.calorific
        return calorific_ingredient
    
    @property
    def get_cost(self):
        cost_ingredient = self.weight / 100 * self.product.cost
        return cost_ingredient


class Pizza(Title):
    def __init__(self,title,ingredients:list):
        self.title = super().__init__(title)
        self.ingredients = ingredients

    @property
    def get_calorific(self):
        sum_calorific = ''
        for ingred_calorific in self.ingredients:
            sum_calorific += ingred_calorific.get_calorific
        return sum_calorific
   
    @property
    def get_cost(self):
        sum_cost = ''
        for ingred_cost in self.ingredients:
            sum_cost += ingred_cost.get_cost      
        return sum_cost

    def __str__(self):
        return f'{self.title} ({self.get_calorific} kkal) - {self.get_cost} руб'  

