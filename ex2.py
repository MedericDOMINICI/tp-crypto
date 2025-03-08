import random
from Ex1 import euclide_etendu, exponentiation_modulaire_rapide

# Algorithme de Miller-Rabin
def miller_rabin(n, k=100):
    if n % 2 == 0:
        if n == 2:
            return (True, -1)
        else:
            return (False, 2)
    
    m = -1
    q = n - 1
    r = 0
    while r == 0:
        d = q
        q, r = q // 2, q % 2
        m += 1
    
    for i in range(k):
        a = random.randint(2, n - 1)
        g, _,_ = euclide_etendu(n, a)
        if g != 1:
            return (False, g)
        
        p = exponentiation_modulaire_rapide(a, d, n)
        if p != 1:
            b1 = True
            j = 0
            while b1 and j <= m - 1:
                b1 = p != n - 1
                p = exponentiation_modulaire_rapide(p, 2, n)
                j += 1
            if b1:
                return (False, a)
    
    return (True, -1)

# Exemple du cours
n = 103328006334666582188478564007333624855622630219933
p = 12345679801994567990089459

# Vérification de n
est_premier, tem = miller_rabin(n)
if est_premier:
    print(f"Le nombre {n} ressemble fortement à un nombre premier.")
else:
    print(f"Le nombre {n} est composite. Témoin de composition : {tem}.")
    
# Vérification de p
est_premier, tem = miller_rabin(p)
if est_premier:
    print(f"Le nombre {p} ressemble fortement à un nombre premier.")
else:
    print(f"Le nombre {p} est composite. Témoin de composition : {tem}.")
    
def generer_premier(k, i_max=10000):
    i = 0
    while i < i_max: # Nombre d'essai maximum
        p = random.randint(2**(k-1), 2**k - 1)  # Generation aléatoire d'un nombre de k-bits
        if p % 2 == 0:  # On s'assure qu'il est impair
            p += 1
        est_premier, _ = miller_rabin(p)
        if est_premier:
            return p
        i += 1
    raise RuntimeError(f"Aucun nombre premier trouvé après {i_max} tentatives.")

k = 1024
premier_a_k_bits = generer_premier(k)
print(f"Nombre premier de {k} bits généré : {premier_a_k_bits}\n")
