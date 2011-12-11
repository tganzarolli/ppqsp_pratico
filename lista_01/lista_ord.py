
'''
Testes de `__contains__` mixin de `Sequence`
(faz busca linear via `__getitem__`)::

    >>> lo = ListaOrdenada([3,2,1])
    >>> 1 in lo, 2 in lo, 3 in lo
    (True, True, True)
    >>> 0 in lo, 4 in lo
    (False, False)
    >>> lo = ListaOrdenada([3,2,4,1])
    >>> 1 in lo, 2 in lo, 3 in lo, 4 in lo
    (True, True, True, True)
    >>> 0 in lo, 5 in lo
    (False, False)
    >>> lo = ListaOrdenada([7])
    >>> 6 in lo, 7 in lo, 8 in lo
    (False, True, False)
    >>> lo = ListaOrdenada([])
    >>> 0 in lo
    False

Testes de `add`::

    >>> lo = ListaOrdenada([])
    >>> lo.add(3); list(lo)
    [3]
    >>> lo.add(5); list(lo) 
    [3, 5]
    >>> lo.add(4); list(lo) 
    [3, 4, 5]
    >>> lo.add(2); list(lo) 
    [2, 3, 4, 5]
    >>> lo.add(3); list(lo) 
    [2, 3, 3, 4, 5]

Testes de `index`::

    >>> lo = ListaOrdenada([2, 3, 3, 4, 5])
    >>> lo.index(3)
    1
    >>> lo.index(5)
    4
    >>> lo.index(2)
    0
    >>> lo = ListaOrdenada(range(100))
    >>> lo.index(98)
    98
    >>> lo.index(100)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/bin/../../System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/_abcoll.py", line 527, in index
        raise ValueError
    ValueError
    
Testes de `count`::

    >>> lo = ListaOrdenada([2, 3, 3, 4, 5])
    >>> lo.count(100)
    0
    >>> lo.count(2)
    1
    >>> lo.count(3)
    2

'''

from collections import Sequence
from busca_bin import busca_bin

class ListaOrdenada(Sequence):
    def __init__(self, iteravel):
        self.__lista = list(sorted(iteravel))

    def __getitem__(self, index):
        return self.__lista[index]

    def __len__(self):
        return len(self.__lista)
        
    def __contains__(self, item):
        return (busca_bin(self, item) >= 0)

    def index(self, item):
        index = busca_bin(self, item)
        index = self.trata_vizinho(item, index)
        if (index < 0):
            raise ValueError()
        else:
            return index

    def count(self, item):
        try:
            index = self.index(item)
        except ValueError,e:
            return 0
            
        i = index + 1
        count = 1
        while (i < len(self.__lista)):
            if not self.__lista[i] == item:
                break
            count+=1
            i+=1
        return count

    def trata_vizinho(self, item, index):
        i = index
        while (i > 0):
            if not self.__lista[i-1] == item:
                break
            i -= 1
        return i
        

    def add(self, novo):
        index = busca_bin(self, novo, True)
        try:
            if (novo > self.__lista[index]):
                index += 1
        except IndexError, e:
            pass
        self.__lista.insert(index, novo)

def desempenho():
    from timeit import repeat
    from pprint import pprint
    tam = 10**5
    expr = '''0 in l, %d in l, %d in l''' % (tam/2, tam)
    prep = '\n'.join([
        '''from __main__ import ListaOrdenada''',
        '''l = ListaOrdenada(range(%d))''' % tam])
    res = repeat(expr, prep, number=10)
    print(min(res))

def teste():
    import doctest
    return doctest.testmod()[0] # devolver falhas

if __name__=='__main__':
    falhas = teste()
    if not falhas:
        desempenho()
