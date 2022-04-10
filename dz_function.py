from unittest import result


def fizz_buzz(m,n):
    s = 0
    for i in range(m,n + 1):
        if i % 3 == 0 and i % 5 == 0:
            s += i
    return print(s) 

fizz_buzz(1000,20000)


def plural_form(number:int,form_1:str,form_2:str,form_3:str):
    c = list(str(number))
    #print(c)
    if 5 <= number <= 20:
        return form_3
    elif number > 20:
        if 2 <=int(c[-1]) <= 4:
            return form_2
        elif int(c[-1]) == 1:
            return form_1
        elif int(c[-1]) == 0:
            return form_3
        if 5 <=int(c[-1]) <= 9:
             return form_3    

print(plural_form(993,'яблоко','яблока','яблок'))



def html_decor(*args,**kwargs):
    def decorator(dec_func):
        def wrapper(attribute):
          res_wrapper = dec_func(attribute)
          #attributes = ''
          if kwargs:
              res_wrapper = f'{res_wrapper}'
              attributes = ''
              for k,v in kwargs.items():
                attributes += f'{k}="{v} "'
              for ind in args:
                  res_wrapper = f'<{ind} {attributes}>{res_wrapper}</{ind}>'
          else:
              for ind in args:
                res_wrapper = f'<{ind}>{res_wrapper}</{ind}>'
          return res_wrapper
        return wrapper                   
    return decorator           


    
        
    





@html_decor('body')
@html_decor('div', width=200, height=100)
@html_decor('a', href='https://yandex.ru/')
def to_string(input_value):
   return str(input_value)
   

print(to_string('ссылка на яндекс'))