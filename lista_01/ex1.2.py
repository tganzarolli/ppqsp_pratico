from baralho import Baralho

class BaralhoMisturado(Baralho):
    
    def __iter__(self):
        indexes = [n for n in range(len(self.cartas))]
        from random import shuffle
        random.shuffle(indexes)
        for index in indexes:
            yield self.cartas[index]

b = BaralhoMisturado()

for carta in b:
    print carta
print "-----------------------------------#*#*#*#------------------------------------"
for carta in b:
    print carta