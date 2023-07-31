from typing import Deque
from collections import deque

d: Deque = deque("hello", maxlen=5)
d.append('4')
d.appendleft('5')
print(d.pop())
print(d.popleft())
print(d)
d.extend('456')
print(d)
d.extend([1, 2, 3, 4])
print(d)
d.extendleft([1, 2, 3, 4])
print(d)

d.rotate(-3)
print(d)

d.clear()
print(d)
