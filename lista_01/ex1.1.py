from baralho import Baralho

# Classes de iteradores:

# Primeira implementacao, pouco pythonica
class InverseIter(object):
    
    def __init__(self, cartas):
        self.cartas=list(cartas)
        self.cartas.reverse()
        self.pos = -1
        
    def next(self):
        self.pos +=1
        try:
            return self.cartas[self.pos]
        except IndexError:
                   raise StopIteration
        
    def __iter__(self):
        return self

#Segunda, mais pythonica, ja usando expressoes geradoras
class InverseIterGenExpr(object):

    def __init__(self, cartas):
        self.cartas=list(cartas)
        self.cartas.reverse()
        self.gen_expr = (carta for carta in self.cartas)

    def next(self):
        return self.gen_expr.next() 

    def __iter__(self):
        return self

#so com reversed
class InverseIterGenExprPlus(object):

    def __init__(self, cartas):
        self.gen_expr = reversed(cartas)

    def next(self):
        return self.gen_expr.next() 

    def __iter__(self):
        return self

#Classes de baralho inverso

class BaralhoInverso(Baralho):
    
    def __init__(self, iter_class):
        super(BaralhoInverso, self).__init__()
        self.iter_class=iter_class

    def __iter__(self):
        return self.iter_class(self.cartas)
        
class BaralhoInversoXPTO(BaralhoInverso):
    pass

class BaralhoInversoPlus(BaralhoInverso):
    
    def __init__(self, iter_class):
        super(BaralhoInversoPlus, self).__init__(iter_class)
        self.cartas_reversas = list(self.cartas)
        self.cartas_reversas.reverse()

    def iter_genexp(self):
        return (carta for carta in self.cartas_reversas)
        
    def iter_object(self):
        return self.iter_class(self.cartas_reversas)
        
    def iter_genfun(self):
        for carta in self.cartas_reversas:
            yield carta

b = BaralhoInversoXPTO(InverseIter) #funciona, ao contrario de Java, sem construtor explicito na subclasse :-)
for carta in b:
    print carta

print "-----------------------------------#*#*#*#------------------------------------"
b = BaralhoInverso(InverseIterGenExpr)
for carta in b:
    print carta
    
print "-----------------------------------#*#*#*#------------------------------------"
b = BaralhoInverso(InverseIterGenExprPlus)
for carta in b:
    print carta
print "-----------------------------------#*#*#*#------------------------------------"
b = BaralhoInversoPlus(InverseIterGenExprPlus)
print b.iter_genexp()
print b.iter_object()
print b.iter_genfun()
print "========"
for carta in b.iter_genexp():
    print carta
print "========"
for carta in b.iter_object():
    print carta
print "========"
for carta in b.iter_genfun():
    print carta
print "========"
