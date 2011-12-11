fox = 'The quick brown fox jumps over the lazy dog.'
fox_letters = set(l.upper() for l in fox if l.isalpha())
print len(fox_letters)

