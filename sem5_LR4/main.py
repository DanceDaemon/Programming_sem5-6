def fib(n):
    """
    Список чисел ряда Фибоначчи 

    Возвращает значения не превосходящие данное n

    Например: 
    n = 1, lst = [0, 1, 1]
    n = 2, lst = [0, 1, 1, 2]
    n = 5, [0, 1, 1, 2, 3, 5]

    """
    lst = [0, 1]

    if n < 0:
        return None
    
    elif n == 0:
        return [0]

    else:
        while True:
            new_el = lst[-1] + lst[-2]
            if new_el > n:
                break
            lst.append(new_el)

        return lst


class FibonacciLst: 
    # итератор, возвращающий n элементов (по количеству элементов iterable-объекта)

    def __init__(self, instance):
        self.instance = instance   
        self.idx = 0 # инициализируем индекс для перебора элементов


    def __iter__(self):
        return self # возвращает экземпляр класса, реализующего протокол итераторов


    def __fib_rec(self, n):
        if n == 0: 
            return 0
        elif n == 1: 
            return 1
        else:
            return self.__fib_rec(n-1)+self.__fib_rec(n-2)


    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx] # получаем очередной элемент из iterable
                
            except IndexError:
                raise StopIteration

            el = self.__fib_rec(res) 
            self.idx += 1
            return el


class FibonacciLstMax: 
    # итератор, возвращающий числа, принадлежащие ряду Фибоначчи

    def __init__(self, instance):
        self.instance = instance   
        self.res_lst = fib(self.instance[-1])
        self.idx = 0 # инициализируем индекс для перебора элементов


    def __iter__(self):
        return self # возвращает экземпляр класса, реализующего протокол итераторов

    def __next__(self):

        while True:
            try:
                res = self.res_lst[self.idx] # получаем очередной элемент из iterable
                
            except IndexError:
                raise StopIteration

            
            self.idx += 1
            return res


from itertools import islice


def fib_iter(iterable):
    l = FibonacciLst(iterable)
    return list(islice(l, len(iterable)))    
    

def fib_iter_max(iterable):
    l = FibonacciLstMax(iterable)
    return list(islice(l, len(iterable))) 


def my_genn(n): 
    # генератор, возвращающий n первых элементов ряда Фибоначчи

    a, b = 0, 1    
    for _ in range(n):        
        yield a        
        a, b = b, a + b
        

if __name__ == '__main__':
    print(fib(7))
    print(list(FibonacciLst(list(range(10)))))
    print(list(FibonacciLstMax(list(range(10)))))
    print(fib_iter(range(14)))
    print(fib_iter_max(range(14)))

    print(list(my_genn(10)))