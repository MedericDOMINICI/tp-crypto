import random
from math import *

# Euclide étendu

def euclide_etendu(a, b):
    if (a==0 and b==0):
        return (0,0,0)
    else:
        a_p = abs(a)
        b_p = abs(b)
        u = 0
        v = 1
        u_p = 1
        v_p = 0
        while(a_p != 0):
            q = b_p // a_p
            r = b_p % a_p

            b_p = a_p
            a_p = r

            u_temp = u
            v_temp = v

            u = u_p
            v = v_p

            u_p = u_temp - q*u_p
            v_p = v_temp - q*v_p
        d = b_p
        if (a<0):
            u = -1*u
        if (b<0):
            v = -1*v
        return d,u,v

#print(euclide_etendu(97, 1024))

def indicatrice_euler(n):
    x = []
    for i in range(1,n):
        d,u,v = euclide_etendu(i, n)
        if d == 1:
            x.append(i)
    return x, len(x)

#print(indicatrice_euler(42))

def inverse_a_modulo_n(a, n):
    #Z_nZ, phi_n = indicatrice_euler(a, n)
    d,u,v = euclide_etendu(a, n)
    return u;

#print(inverse_a_modulo_n(13,42))

def exponentiation_modulaire_rapide(x, d, n):
    r = 1
    x1 = x%n
    d1 = d
    while d1 != 0:
        if d1%2 == 1:
            r = (r*x1)%n
        x1 = (x1*x1)%n
        d1 = d1 //2
    return r

#print(exponentiation_modulaire_rapide(2,30,9))

def RSA_chiffrage(m, e, n):
    a = exponentiation_modulaire_rapide(m,e,n)
    return a

#print(RSA_chiffrage(3, 7, 13*17))

def RSA_dechiffrage(n, e, a): 
    phi_n = indicatrice_euler(n)[1]
    if e == 1 or euclide_etendu(e, phi_n)[0] != 1:
        return "Mauvais choix de e"
    d = inverse_a_modulo_n(e, phi_n)
    return exponentiation_modulaire_rapide(a,d,n)

#print(RSA_dechiffrage(221,7,12))
