import math


def fac(n:int):
    temp = n
    while n > 1:
        temp *= n-1
        n -= 1

    return temp

def suivant(u:int):
    if (u%2 == 0):
        return u//2
    return 3*u+1

def syracus(u:int):
    while u > 1:
        u = suivant(u)
    return u

def nombre_syracus(u:int):
    steps = 0
    while u > 1:
        u = suivant(u)
        steps += 1
    return steps

def etoile():
    print('*',end='')

def diese() :
    print('#',end='')

def nouvelle_ligne() :
    print()

def tapis_a():
    i = 0
    while i < 9:
        n = 0
        while n < 9:
            etoile()
            n += 1
        nouvelle_ligne()
        i += 1

def tapis_b():
    i = 0
    while i < 9:
        n = 0
        while n < 4:
            etoile()
            diese()
            if (n == 3):
                etoile()
            n += 1
        nouvelle_ligne()
        i += 1

def tapis_c():
    i = 0
    while i < 9:
        n = 0
        while n < 4:
            if (i % 2 == 0):
                etoile()
                diese()
                if (n == 3):
                    etoile()
                n += 1
            else:
                diese()
                etoile()
                if (n == 3):
                    diese()
                n += 1
        nouvelle_ligne()
        i += 1

def tapis_d():
    i = 0
    while i < 9:
        n = 0

        if (i == 2 or i == 5 or i == 8):
            while n < 9:
                etoile()
                n += 1
        else:
            while n < 4:
                if (i % 2 == 0):
                    etoile()
                    diese()
                    if (n == 3):
                        etoile()
                    n += 1
                else:
                    diese()
                    etoile()
                    if (n == 3):
                        diese()
                    n += 1
        nouvelle_ligne()
        i += 1

def fermat(n:int) -> int:
    return 2**(2**n) + 1

def premier_fateur(n:int) -> int:
    i = 2
    while i < n:
        if (n % i == 0):
            return i
        i += 1
    return n

def premier_facteur(n: int) -> int:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return n

def trouver_fermat_non_premier():
    n = 0
    while True:
        fermat_n = fermat(n)
        facteur = premier_facteur(fermat_n)
        if facteur != fermat_n:
            print(f"Le premier n tel que fermat({n}) n'est pas premier est: {n}")
            print(f"Un diviseur premier de fermat({n}) est: {facteur}")
            break
        n += 1

def deriver(f, a, h):
    return (f(a + h) - f(a)) / h

def resoudre(f, a0, h):
    a = a0
    while abs(f(a)) > h:
        f_prime = deriver(f, a, h)
        a = a - f(a) / f_prime
    return a

f = lambda x: x**2 - 2

a0 = 1.0
h = 1e-5

approx_sqrt_2 = resoudre(f, a0, h)

print(f"Approximation de sqrt(2): {approx_sqrt_2}")