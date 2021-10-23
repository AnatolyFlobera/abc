class MyClass:
    def __init__(self, dict):
        self.dict = dict
    def summa (self, a, b):
        c = self.dict.get(a, 0)
        d = self.dict.get(b, 0)
        if c!=0 and d!=0: print ("Sum of 2 lists =", sum(c)+sum(d))
        else: print("0")

ex1 = MyClass({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
ex2 = MyClass({'one': [111, 11], 'two': [22, 20, 222], 'thre': [3, 33, 33]})
ex3 = MyClass({'x': [-11, 1, 11, -1], 'y': [2, 2, -2, 22], 'z': [3, -3]})

ex1.summa('a', 'b') # Two keys
ex1.summa('c', 'g') # No key

ex2.summa('one', 'two') # Two keys
ex2.summa('one', 'six') # No key

ex3.summa('x', 'z') # Two keys
ex3.summa('x', 'y') # Two keys