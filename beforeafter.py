type Waktu = tuple [int, int, int]
def Make_waktu(a:int,b:int,c:int)->tuple:
    return (a,b,c)
def getdetik(detik:Waktu) -> int :
    return detik[2]
def getmenit(menit:Waktu) -> int :
    return menit[1]
def getjam(jam:Waktu) -> int :
    return jam[0]

def detiksincemidnight(j:Waktu) -> int:
    return ((getjam(j)*3600) +  (getmenit(j)*60) + (getdetik(j)))

def is_halfday(j:Waktu)->bool:
    return((getjam(j)) == 12 and (getmenit(j)) == 0 and (getdetik(j)) == 0)

def isbefore_isAfter(w1:Waktu, w2:Waktu)->bool:
    if (getjam(w1) > getjam(w2)) and ((getmenit(w1) <= getmenit(w2)) or (getdetik(w1) <= getdetik(w2))) : return  True
    elif (getmenit(w1) > getmenit(w2) and (getdetik(w1) <= getdetik(w2))): return  True
    elif (getdetik (w1) > getdetik (w2)) and (getmenit(w1) <= getmenit(w2)): return  True
    else: return  False






print(detiksincemidnight(((2),(30),(0))))
print(is_halfday((12,0,0)))

print(isbefore_isAfter(
    ((2,30,10)),
    ((2,10,10))
))