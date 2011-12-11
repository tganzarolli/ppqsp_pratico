import string
letters = set(string.ascii_uppercase)

jabuti = 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
jabuti_letras = set(l.upper() for l in jabuti if l.isalpha())
for j in sorted(set(jabuti_letras)):
    print j
print len(jabuti_letras)

#o que existe em A e nao existe B
print letters - jabuti_letras
#o que existe unicamente em A ou em B. Symmetric difference
print letters ^ jabuti_letras