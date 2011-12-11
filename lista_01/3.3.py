import string
fox = 'The quick brown fox jumps over the lazy dog.'
fox_letters = set(l.upper() for l in fox if l.isalpha())

import string
letters = set(string.ascii_uppercase)
print fox_letters == letters
