from listas_redutoras import m,n

print zip(m, n)
for i in (x for (x,y) in zip(m, n)):
    print i
print all(x for (x,y) in zip(m, n))