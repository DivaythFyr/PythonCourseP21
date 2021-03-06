# Рекурсия - это метод решения задач, при котором функция вызывает саму себя в процессе исполнения
# Чаще всего это реализуется следующим образом:
# В if прописывается условие, которое затрагивает последнее из возможных для решения задач состояний
# в else возвращается вызов функции с видоизмененным аргументом (например, меньше на один, чем предыдущий)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

#print(fact(3))

# Задача: написать функцию, которая суммирует все числа в списке
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
#print(list_sum([4, 44, 3]))


# Задача: функция принимает позицию числа и возвращает число из последовательности Фибоначчи
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def Fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return (Fib(num - 1) + (Fib(num - 2)))
#print(Fib(6))


# Задача: функция принимает число и возвращает сумму всех цифр внутри него
# Чтобы обратиться к числу более высокого порядка (например, к 2 в 24, воспользуйтесь int(n / 10)
# Чтобы обратиться к числу более низкого порядка (например, к 4 в 24), воспользуйтесь n % 10
def sumDigits(n):
    if n == 0:
        return n
    else:
        return n % 10 + sumDigits(int(n / 10))

#print(sumDigits(24))


# Задача: функция принимает число, и возвращает сумму n + (n-2) + (n-4)
# пока n - x >= 0
# Например recNsub2sum(4) -> 6, recNsub2sum(6) -> 12

def recNsub2sum(n):
    if n <= 0:
        return n
    else:
        return n + recNsub2sum(n - 2)
#print(recNsub2sum(4))


# Задача: функция принимает список чисел, внутри может быть еще список чисел
# Добавить цикл из задачи с суммой чисел в списке, чтобы проверять:
# если это список чисел, то используем рекурсию по отношению к нему
# если это число, то просто суммируем с переменной, которая в начале работы функции равна нулю

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == list:
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
#print(recursive_list_sum([3, 3, [2, 2]]))
