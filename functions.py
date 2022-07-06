# Функция - это часть кода, которая работает, только если ее вызвать
# В функцию, как правило, вводят аргументы
# Функция способна возвращать данные

def my_function():
    print('Функция была вызвана')

#my_function()


# Аргументы - переменные, на месте которых данные будут переданы в
# функцию и использованы

def PrintAnimal(animal, plant):
    print(animal, plant)
#PrintAnimal(plant='дуб')


# Выводить аргументы можно не только в том порядке,
# в котором они были заданы

def My_Dogs(dog1, dog2, dog3):
    print('Мои песики, начиная с самого любимого: ' + dog2 + ', ' + dog3 + ', ' + dog1)
#My_Dogs('Шарик', 'Фунтик', 'Вася')


# Каждому аргументу можно задать значение по умолчанию
def my_planet(planet = "The Earth"):
  print("I am from " + planet)

#my_planet()
my_planet('Mars')

# В качестве аргументов может быть любой тип данных

def Printfruit(food):
  for x in food:
    print(x)

#Printfruit(["apple", "banana", "cherry"])


# Задача: преобразуйте данный код в функцию
#name = input()
#print('His name is ' + name)

def function(name):
    print('His name is ' + name)

# Задача: преобразуйте данный код в функцию

#number_list = [1, 2, 2, 5, 6, 4]
#for i in range(len(number_list)):
    #number_list[i] += 1
#print(number_list)


def functIon(number_list):
    for i in range(len(number_list)):
        number_list[i] += 1
    print(number_list)
#functIon([3, 3, 3, 3, 4])

# Задача: преобразуйте данный код в функцию
# i = 100
# while i != 1:
#     i -= 1


# Задача: напишите функцию, которая берет список чисел и перемножает все эти числа


# Задача: напишите функцию, которая принимает строку и делает ее наоборот


# Задача: функция принимает число, принимает диапазон range
# она должна проверить, находится ли число в диапазоне

def checkRange(n, range):
    print(n in range)

# checkRange(2, range(0, 5))
# Задача: Функция принимает список чисел и возвращает только четные числа


# TTAATT
#
#Задача: Функция принимает строку и возвращает True, если строка является
# палиндромом.
# Чтобы сделать строку наоборот, напишите string[::-1]

def checkPalindrome(string):
    if string[::-1] == string:
        print(True)
    else:
        print(True)

#checkPalindrome('AATTAAGGAATTAA')



