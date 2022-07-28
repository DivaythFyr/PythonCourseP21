import math

#x = 'trtr'
#y = math.sqrt(x)



def protectDividingOnZero(number1, number2):
    if number2 != 0:
        print(number1 / number2)
    else:
        print("You can't divide on zero")

#protectDividingOnZero(1, 0)


def TryDividingOnZero(number1, number2):
    try: # пытаемся выполнить рисоковое действие
        print(number1/number2)

    except: # если что-то идет не так, то внутри except прописываем, что будем делать
        print("Бесконечность")
#TryDividingOnZero(1, 0)



# Желательно в раздел exception прописывать конкретное на какое исключение как реагировать

def dfdf():
    try:
        print(1 / 0)
        print(b + a)
    except:
        print('ошибка')
#dfdf()


def rtr():
    try:
        print(1 / 0)
        print(b + a)
    except NameError:
        print('Ошибка, что это за переменные?')
    except ZeroDivisionError:
        print('нельзя делить на ноль')

#rtr()


# Если вы хотите обработать несколько исключений одним и тем же способом,
# перечислите их так except (исключение1, исключение2)

def dfdff():
    try:
        print(1 / 0)
        print(b + a)
    except (NameError, ZeroDivisionError):
        print('Это деление на ноль или неназванные переменные')
#dfdff()

