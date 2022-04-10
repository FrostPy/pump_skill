def fizz_buzz(m,n):
    s = 0
    for i in range(m,n+1):
        if i % 3 == 0 and i % 5 == 0:
            s += i
    return s

fizz_buzz(0,15)     



def plural_form(number:int,form_1:str,form_2:str,form_3:str):
    c = list(str(number))
    #print(c)
    if number == 1:
        return form_1
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

print(plural_form(1,'student','studenta','studentov'))                