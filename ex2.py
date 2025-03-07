import random
from Ex1 import euclide_etendu, exponentiation_modulaire_rapide

def miller_rabin(n, k=100):
    if n % 2 == 0:
        if n == 2:
            return (True, -1)
        return (False, 2)
    
    m = -1
    q = n - 1
    r = 0
    while r == 0:
        d = q
        q, r = q // 2, q % 2
        m += 1
    
    for _ in range(k):
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
    
def generate_prime(k, i_max=10000):
    i = 0
    while i < i_max:
        p = random.randint(2**(k-1), 2**k - 1)  # Générer un nombre k-bit
        if p % 2 == 0:  # S'assurer qu'il est impair
            p += 1
        is_prime, _ = miller_rabin(p)
        if is_prime:
            return p
        i += 1
    raise RuntimeError(f"Aucun nombre premier trouvé après {i_max} tentatives.")

# Génération d'un nombre premier de 1024 bits
k = 1024
prime_k_bits = generate_prime(k)
print(f"Nombre premier de {k} bits généré : {prime_k_bits}\n")
