from listas import homens, mulheres

print dict(zip(homens,mulheres))
print "-------"
casais = [(h,m) for h in homens for m in mulheres]
print len(casais)
print casais
print "-------"
casais = [(h,m) for h in homens if len(h) >=4 for m in mulheres if len(m) >=4]
print len(casais)
print casais
print "-------"