def fizz_buzz(m,n):
    s = 0
    if m == n:
        s = n
        return s
    else:     
       for i in range(m,n+1):
          if i % 3 == 0 and i % 5 == 0:
            s += i
    return s



def plural_form(number:int,form_1:str,form_2:str,form_3:str):
    c = list(str(number))
    #print(c)
    if number == 1:
        return form_1
    elif 2 <= number <= 4:
        return form_2
    elif 5 <= number <= 20:
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


print(fizz_buzz(0,3))

def html(args,**kwargs):
    
    def decorator(dec_func):
       
       def wrapper(attribute):
             res_wrapper = dec_func(attribute)
             if kwargs:
                 res_wrapper = f'{res_wrapper}'
                 attributes = ''
                 for k,v in kwargs.items():
                    attributes += f' {k}="{v}"'
                 res_wrapper = f'<{args}{attributes}>{res_wrapper}</{args}>'
             else:
                res_wrapper = f'<{args}>{res_wrapper}</{args}>'
             return res_wrapper
       return wrapper                   
    return decorator           


    
        
@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
   return str(input_value)
   

