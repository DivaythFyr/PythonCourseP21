# Классы - сущности, свойства которых зависят от наследования или преемственности от других классов

# Для начала разберем на примере того, как реализуется стек.
# Стек - это объект с двумя методами: push и pop. Элементы попадают туда как монеты в стопку - каждый по очереди. Если
# Если в стопку попала последняя монета и нам нужно вытащить монету, то последние монеты будут первыми изыматься

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

# Объектно-ориентированный подход
class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

stackObject = Stack() # Чтобы создать объект с определенным классом - пользуемся такой конструкцией.
#print(stackObject.__stack)
#stackObject.push(3)
#print(stackObject.pop())

# Каждый класс должен начинаться с функции __init__, у нее обязательно должен быть параметр self.
# Благодаря self внутри init задаются свойства и методы, которыми смогут пользоваться другие функции класса,
# а также классы, унаследованные от него

# Чтобы унаследовать от класса, нужно при объявлении потомка в круглых скобках указать имя родителя
# В функции init, перед еще одним init написать имя класса родителя
# Если мы пользуемся похожими методами от класса родителя - то пишем имя родителя, точку, метод родителя, задаем аргументы

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum

stack1Object = AddingStack()

for i in range(5):
    stack1Object.push(i)
#print(stack1Object.getSum())

for i in range(5):
    pass
    #print(stack1Object.pop())






# У каждого объекта, унаследованного от класса, может быть свой собственный набор дополнительных свойств
# Либо какое-либо из свойств может не применяться

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
    def setSecond(self, val):
        self.second = val

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(4)
exampleObject3 = ExampleClass(4)
exampleObject3.third = 4 # Задали свойство, которого не было у класса

#print(exampleObject1.__dict__)
#print(exampleObject2.__dict__)
#print(exampleObject3.__dict__)


class ListOfNumbers:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)


#OneZero = ListOfNumbers()
#OneZero.push(6)
#print(OneZero.list)



# Функция init дает указанные нами свойства и методы объекту при его инициализации. Если создать переменную вне
# конструктора init, то он будет характерен для всего класса и абсолютно всегда будет наследоваться объектам.
class Example_Class:
    a = 1
    def __init__(self, val):
        self.b = val

ExampleObject = Example_Class(2)
#print(hasattr(ExampleObject, 'b'))
#print(hasattr(ExampleObject, 'a'))
#print(hasattr(Example_Class, 'b'))
#print(hasattr(Example_Class, 'a'))


# Если попытаться распечатать объект, то мы получим следующее

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
sun = Star("The Sun", "Milky Way")
#print(sun)


# Чтобы выводить информацию об объекте, нужно пользоваться конструктором __str__
# В конструкторе __str__ мы пишем return и указываем, что возвращаем. При использовании print на объект, с этого момента,
# Будет показываться

class Planet:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


Mars = Planet('Mars', 'Milky Way')
#print(Mars)


# Чтобы проверить, является ли один из классов унаследованным от другого, можно воспользоваться методом issubclass()

class Two():
    pass

class TwentyTwo(Two):
    pass

class TwoHundredTwentyTwo(TwentyTwo):
    pass
#print(issubclass(Two, TwentyTwo))
#print(issubclass(TwoHundredTwentyTwo, Two))


# чтобы проверить, сделан ли объект по определенному классу, можно воспользоваться методом isinstance()
TwoSuns = Two()

#print(isinstance(TwoSuns, Two))


# Если мы хотим потомку дать свойства его суперкласса, то мы можем воспользоваться такой записью
class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name}"

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")
#print(obj)

# super() позволяет обратиться к любой сущности суперкласса. Например, вызвать метод суперкласса.



# У одного класса может быть много суперклассов

class Living():
    status = 'living'

class NonLiving():
    status = 'nonliving'

class Virus( Living, NonLiving):
    pass

virus = Virus()

#print(virus.status, virus.status)


# Если два суперкласса имеют одинаковые переменные или методы, то при объявлении будет вызываться тот, который был задан
# левее в скобках подкласса



class Human:
    def __init__(self, NSP, birthday, phone_number, country, address):
        self.NSP = NSP
        self.birthday = birthday
        self.phone_number = phone_number
        self.country = country
        self.address = address

    def show_personal_data(self):
        return str('His name is ' + self.NSP + ', he was born in ' + self.birthday)

Human1 = Human('Petr Yan', '12 June 1978', '89349076709', 'Russia', 'Voronezh')
print(Human1.show_personal_data())


class Country():
    def __init__(self, capital, square, region_quantity, population):
         self.capital = capital
         self.square = square
         self.region_quantity = region_quantity
         self.population = population

    def __str__(self):
         return f'The capital is {self.capital}'

Russia = Country('Moscow', '1893', 85 ,'148000000')
print(Russia)
