type mahasiswa = tuple [str, str, str, float]

def get_nama(nama:mahasiswa) -> str:
    return nama[0]
def get_nim(nim:mahasiswa) -> str:
    return nim[1]
def get_ttl(ttl:mahasiswa)->str:
    return ttl[2]
def get_ipk(ipk:mahasiswa) ->float:
    return ipk[3]

def max_2(m1:mahasiswa,m2:mahasiswa)->mahasiswa:
    return m1 if get_ipk(m1) >= get_ipk(m2) else m2

def min_2(m1:mahasiswa,m2:mahasiswa)-> mahasiswa:
    return m1 if get_ipk(m1) <= get_ipk(m2) else m2


def max_ipk(mhs1, mhs2, mhs3, mhs4, mhs5, mhs6, mhs7) -> mahasiswa:
    return max_2(mhs1, max_2(mhs2, max_2(mhs3, max_2(mhs4, max_2(mhs5, max_2(mhs6, mhs7)))))) 

def min_ipk(mhs1, mhs2, mhs3, mhs4, mhs5, mhs6, mhs7) -> mahasiswa:
    return min_2(mhs1, min_2(mhs2, min_2(mhs3, min_2(mhs4, min_2(mhs5, min_2(mhs6, mhs7))))))

def is_cumlaude(mhs:mahasiswa)->bool:
    return get_ipk(mhs) >= 3.50

print(max_ipk(
    get_nama(("yanto","24060123","12-10-2000",3.9)),
    get_nama(("andri","24060523","12-10-2000",2.9)),
    get_nama(("yanti","24060623","12-10-2000",4.0)),
    get_nama(("budi","24060723","12-10-2000",3.1)),
    get_nama(("pendi","24060823","12-10-2000",3.2)),
    get_nama(("karman","24060923","12-10-2000",3.3)),
    get_nama(("karno","24060223","10-09-2001",3.4))
))

print(min_ipk(
    get_nama(("yanto","24060123","12-10-2000",3.9)),
    get_nama(("andri","24060523","12-10-2000",2.9)),
    get_nama(("yanti","24060623","12-10-2000",4.0)),
    get_nama(("budi","24060723","12-10-2000",3.1)),
    get_nama(("pendi","24060823","12-10-2000",3.2)),
    get_nama(("karman","24060923","12-10-2000",3.3)),
    get_nama(("karno","24060223","10-09-2001",3.4))
))

print(is_cumlaude(
    (("yanto","24060123","12-10-2000",3.9))
))