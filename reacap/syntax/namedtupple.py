from collections import namedtuple

Point = namedtuple('Point', 'x y z')
newP = Point(3, 4, 6)

PointByList = namedtuple('Point', ['x', 'y', 'k'])
newPl = PointByList(3, 4, 6)
print(newPl)

PointByDict = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0})
print(PointByDict(x=3, y=1, z=3))


newP = newP._replace(y=10)
print(newP)
