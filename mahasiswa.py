type mahasiswa = tuple [str, str, str, float]

def get_nama(nama:mahasiswa) -> str:
    return nama[0]
def get_nim(nim:mahasiswa) -> str:
    return nim[1]
def get_ttl(ttl:mahasiswa)->str:
    return ttl[2]
def get_ipk(ipk:mahasiswa) ->float:
    return ipk[3]



#==Fungsi Utama==#

def max_ipk(mhs1:mahasiswa,mhs2:mahasiswa,mhs3:mahasiswa,mhs4:mahasiswa,mhs5:mahasiswa,mhs6:mahasiswa,mhs7:mahasiswa) -> str:
    return(
        get_nama(mhs1) if (get_ipk(mhs1)> get_ipk(mhs2)) and (get_ipk(mhs1) > get_ipk(mhs3)) and (get_ipk(mhs1) > get_ipk (mhs4)) and (get_ipk(mhs1) > get_ipk(mhs5)) and (get_ipk(mhs1)>get_ipk(mhs7)) and (get_ipk(mhs1)>get_ipk(mhs6)) else
        get_nama(mhs2) if (get_ipk(mhs2)> get_ipk(mhs1)) and (get_ipk(mhs2) > get_ipk(mhs3)) and (get_ipk(mhs2) > get_ipk (mhs4)) and (get_ipk(mhs2) > get_ipk(mhs5)) and (get_ipk(mhs2)>get_ipk(mhs7)) and (get_ipk(mhs2)>get_ipk(mhs6)) else
        get_nama(mhs3) if (get_ipk(mhs3)> get_ipk(mhs1)) and (get_ipk(mhs3) > get_ipk(mhs2)) and (get_ipk(mhs3) > get_ipk (mhs4)) and (get_ipk(mhs3) > get_ipk(mhs5)) and (get_ipk(mhs3)>get_ipk(mhs7)) and (get_ipk(mhs3)>get_ipk(mhs6)) else
        get_nama(mhs4) if (get_ipk(mhs4)> get_ipk(mhs1)) and (get_ipk(mhs4) > get_ipk(mhs3)) and (get_ipk(mhs4) > get_ipk (mhs2)) and (get_ipk(mhs4) > get_ipk(mhs5)) and (get_ipk(mhs4)>get_ipk(mhs7)) and (get_ipk(mhs4)>get_ipk(mhs6)) else
        get_nama(mhs5) if (get_ipk(mhs5)> get_ipk(mhs1)) and (get_ipk(mhs5) > get_ipk(mhs3)) and (get_ipk(mhs5) > get_ipk (mhs2)) and (get_ipk(mhs5) > get_ipk(mhs4)) and (get_ipk(mhs5)>get_ipk(mhs7)) and (get_ipk(mhs5)>get_ipk(mhs6)) else
        get_nama(mhs6) if (get_ipk(mhs6)> get_ipk(mhs1)) and (get_ipk(mhs6) > get_ipk(mhs3)) and (get_ipk(mhs6) > get_ipk (mhs2)) and (get_ipk(mhs6) > get_ipk(mhs4)) and (get_ipk(mhs6)>get_ipk(mhs7)) and (get_ipk(mhs6)>get_ipk(mhs5))
        else get_nama(mhs7)
        
    )

def min_ipk(mhs1:mahasiswa,mhs2:mahasiswa,mhs3:mahasiswa,mhs4:mahasiswa,mhs5:mahasiswa,mhs6:mahasiswa,mhs7:mahasiswa) -> str:
    return(
        get_nama(mhs1) if (get_ipk(mhs1)< get_ipk(mhs2)) and (get_ipk(mhs1) < get_ipk(mhs3)) and (get_ipk(mhs1) < get_ipk (mhs4)) and (get_ipk(mhs1) < get_ipk(mhs5)) and (get_ipk(mhs1)<get_ipk(mhs7)) and (get_ipk(mhs1)<get_ipk(mhs6)) else
        get_nama(mhs2) if (get_ipk(mhs2)< get_ipk(mhs1)) and (get_ipk(mhs2) < get_ipk(mhs3)) and (get_ipk(mhs2) < get_ipk (mhs4)) and (get_ipk(mhs2) < get_ipk(mhs5)) and (get_ipk(mhs2)<get_ipk(mhs7)) and (get_ipk(mhs2)<get_ipk(mhs6)) else
        get_nama(mhs3) if (get_ipk(mhs3)< get_ipk(mhs1)) and (get_ipk(mhs3) < get_ipk(mhs2)) and (get_ipk(mhs3) < get_ipk (mhs4)) and (get_ipk(mhs3) < get_ipk(mhs5)) and (get_ipk(mhs3)<get_ipk(mhs7)) and (get_ipk(mhs3)<get_ipk(mhs6)) else
        get_nama(mhs4) if (get_ipk(mhs4)< get_ipk(mhs1)) and (get_ipk(mhs4) < get_ipk(mhs3)) and (get_ipk(mhs4) < get_ipk (mhs2)) and (get_ipk(mhs4) < get_ipk(mhs5)) and (get_ipk(mhs4)<get_ipk(mhs7)) and (get_ipk(mhs4)<get_ipk(mhs6)) else
        get_nama(mhs5) if (get_ipk(mhs5)< get_ipk(mhs1)) and (get_ipk(mhs5) < get_ipk(mhs3)) and (get_ipk(mhs5) < get_ipk (mhs2)) and (get_ipk(mhs5) < get_ipk(mhs4)) and (get_ipk(mhs5)<get_ipk(mhs7)) and (get_ipk(mhs5)<get_ipk(mhs6)) else
        get_nama(mhs6) if (get_ipk(mhs6)< get_ipk(mhs1)) and (get_ipk(mhs6) < get_ipk(mhs3)) and (get_ipk(mhs6) < get_ipk (mhs2)) and (get_ipk(mhs6) < get_ipk(mhs4)) and (get_ipk(mhs6)<get_ipk(mhs7)) and (get_ipk(mhs6)<get_ipk(mhs5))
        else get_nama(mhs7)
        
    )


def is_cumlaude(mhs:mahasiswa)->bool:
    return get_ipk(mhs) >= 3.50

#==input==#
print(min_ipk(
    ("yanto","24060123","12-10-2000",3.9),
    ("andri","24060523","12-10-2000",2.9),
    ("yanti","24060623","12-10-2000",4.0),
    ("budi","24060723","12-10-2000",3.1),
    ("pendi","24060823","12-10-2000",3.2),
    ("karman","24060923","12-10-2000",3.3),
    ("karno","24060223","10-09-2001",3.4)
))

print(is_cumlaude(
    ("yanto","24060123","12-10-2000",3.9)
))