# бинарный поиск

# названиеМассива.sort() встроенная сортировка
def binary_search(item, list):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high # на каждом обороте цикла будет инициализироваться порядковый номер среднего элемента
        guess = list[mid] # и сам средний элемент относительно этого порядкового номера

        if guess == item:
            return mid
        if item < guess: # если элемент меньше того, что посередине
            high = mid - 1 # то самой верхней границей становится элемент до среднего
        else:
            low = mid + 1
    return None # элемента нет в списке
#print(binary_search(5, [16, 2, 3, 4, 5]))


# сортировка выбором

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#print(findSmallest([]))

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) #
    return newArr
#print(selectionSort([1, 2, 2, 4, 4, 4, 3, 3]))


