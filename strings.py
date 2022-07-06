# Символ ''' позволяет писать многострочные строки
password = '''1234
1234'''
#print(password, end=' ')

# строки можно складывать и умножать
hello = 'hello'
world = 'world'
#print(hello + ' ' + world)

#print(5 * 'a')

# Мы можем обращаться к элементам строки как к элементам списка
#for i in range(len(password)):
    #print(password[i], sep='') # если не указать end, то print будет печатать на новой строчке, а с end через символ, который мы указали

# Задание: создаете любую строчку. В цикле проверяете: если порядковый номер символа четный, то
# символ умножаете на два, если нечетный, то умножаете на три. Возвращаете новую строчку.

#strinG = 'dfdfdfdfdfd'
#strinG += 'F' добавление символа в конец строки

# if i % 2 == 0 Проверка на четность
# empty_string += string[i] * 2
string = 'Follow me, brothers!'
increased_str = ''
for i in range(len(string)):
    if i % 2 == 0:
        increased_str += string[i] * 2
    else:
        increased_str += string[i] * 3
#print(increased_str)



# срезы можете делать также, как и со списками
#print(increased_str[1:6])


# Чтобы посмотреть, есть ли какой-либо элемент в строке, можно воспользоваться операторами in и not in
#print('1' in string)
# Задача: если в строке буквы не английского алфавита, то не печатать их
alphabet = 'abcdefghijklmnopqrstuvwxyz, '
many_lang = 'hello, я из russia'
only_en = ''

#  if many_lang[i] in alphabet:

for i in range(len(many_lang)):
    if many_lang[i] in alphabet:
        only_en += many_lang[i]
#print(only_en)





# строку можно удалить целиком, но нельзя удалять элемент строки
#del password[0]
# к строке нельзя применить методы append() и insert()
#password.append('5')

# Чтобы удалить элемент строки из какой-то конкретной позиции:
string = 'abcdefgggg'
position = 5
#print(string[:position] + string[(position + 1):]) #удалить на конкретной позиции
#print(string.replace('g', '')) # удалить какой-то конкретный элемент.


# Задача: имеется список чисел и строк, например:
# [1, 3, '4', 6, 'cloud', 5, 'throne', 'fgfgf'].
# Если элемент в списке - число, то сделать из него строку,
# если элемент - строка, то сделать число.
# Если строка не сможет превратиться в число,
# то к строке прибавьте строку '1'.
# Чтобы проверить, может ли строчка превратиться в число,
# воспользуйтесь встроенным методом isnumeric()
# Например, string = '4',  string.isnumeric() будет выводить True


# Для данного списка программа выведет ['1', '3', 4, '6', 'cloud1', '5', 'throne1', 'fgfgf1']
str_int_list = [1, 3, '4', 6, 'cloud', 5, 'throne', 'fgfgf']
for i in range(len(str_int_list)):
    if type(str_int_list[i]) == int:
        str_int_list[i] = str(str_int_list[i])
    elif str_int_list[i].isnumeric() == False:
        str_int_list[i] += '1'
    else:
        str_int_list[i] = int(str_int_list[i])

#print(str_int_list)



