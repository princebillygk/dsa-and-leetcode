from collections import Counter

c = Counter(a=4, b=1, c=0, d=2)
d = Counter(['a',  'b', 'b', 'c'])
print(c | d)
print(c & d)
print(c+d)
print(c-d)

c.subtract(d)
print(c)
c.update(d)
print(c)

c.clear()
print(c)
