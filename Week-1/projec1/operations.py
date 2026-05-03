from masfofah import Masfofah

def masfofah_asfar(rows, cols):
    return Masfofah([[0]*cols for _ in range(rows)])

def masfofah_wahidat(rows, cols):
    return Masfofah([[1]*cols for _ in range(rows)])

def i9n3_masfofatan(lst):
    return Masfofah(lst)

def i9n3_sho3a3an(lst):
    return Masfofah([lst])

def identity_masfofah(n):
    m = masfofah_asfar(n, n)
    for i in range(n):
        m[i][i] = 1
    return m

def elementwise_product(m1, m2):
    for i in range(len(m1)):
        m1[i].element_wise_product(m2[i])