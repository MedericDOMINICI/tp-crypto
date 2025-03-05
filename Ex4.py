import matplotlib.pyplot as plt
import numpy as np
import math

def crible_eratosthene(n):
    T = [1 for i in range(0,n)]
    T[1] = 0
    for i in range (2, n):
        if T[i] !=0:
            p = i*i
            while p <= n-1:
                T[p] = 0
                p = p + i
    L = []
    for i in range(2,n):
        if T[i] == 1:
            L.append(i)
    return L

def nb_de_nb_premier_inf_a_n(n):
    return len(crible_eratosthene(n))

'''
n = 100000000
nb_premier = crible_eratosthene(n)
print(f"Il y a {len(nb_premier)} inferieurs à {n}")
'''

def calculer_pi_de_n_et_n_sur_log_n(n):
    x = []
    l = []
    for i in range(2,n):
        nb = nb_de_nb_premier_inf_a_n(i)
        x.append(i)
        l.append(nb)

    ln_x = [n/math.log(n) for n in x]
    
    return x, l, ln_x

def calculer_erreur_estimation(n):
    x, l, ln_x = calculer_pi_de_n_et_n_sur_log_n(n)
    print(len(x), len(l), len(ln_x))
    erreur = [(abs(l[n]-ln_x[n]))/l[n] for n in range(1,len(x))]
    erreur.insert(0, 0)
    return x, erreur

def plot_pi_n(n):
    x, l, ln_x = calculer_pi_de_n_et_n_sur_log_n(n)
    fix, ax = plt.subplots()
    ax.plot(x, l)
    ax.plot(x, ln_x)
    plt.show()

#plot_pi_n(1000)

def plot_erreur_estimation(n):
    x, erreur = calculer_erreur_estimation(n)
    fix, ax = plt.subplots()
    ax.plot(x, erreur)
    plt.show()

plot_erreur_estimation(1000)
