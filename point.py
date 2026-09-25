type Point = tuple[float,float]

def makepoint (x: float, y: float) -> Point:
    return (x,y)

def getAbsis(p:Point) -> float :
    return p [0]
def getordinat(p: Point) -> float:
    return p[1]
def JarakTitik(t1: Point, t2: Point) -> float :
    return (
        (getAbsis(t1) - getAbsis(t2)) ** 2 +
        (getordinat(t1) - getordinat(t2)) ** 2 
    ) ** 0.5
def isTitikOrigin(t: Point) -> bool:
    return getAbsis(t) == 0 and getordinat(t) == 0 
print(makepoint(2, 7))
print(getAbsis(makepoint(2,7)))
print(getordinat(makepoint(2,7)))
print(JarakTitik(makepoint(4,3), makepoint (0,0)))

