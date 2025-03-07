from Ex1 import euclide_etendu, exponentiation_modulaire_rapide, inverse_a_modulo_n
from ex2 import generate_prime

def generate_rsa_keys(k=512, e=115670849):
    while True:
        p = generate_prime(k)
        q = generate_prime(k)
        if p != q:
            n = p * q
            phi_n = (p - 1) * (q - 1)
            if euclide_etendu(e, phi_n)[0] == 1:
                return p, q, n, phi_n, e

p, q, n, phi_n, e = generate_rsa_keys()

n_etudiant = 123456789
c = exponentiation_modulaire_rapide(n_etudiant, e, n)

d = inverse_a_modulo_n(e, phi_n) % phi_n
m_decrypted = exponentiation_modulaire_rapide(c, d, n)

print(f"Message original : {n_etudiant}")
print(f"Chiffrement : {c}")
print(f"Déchiffrement : {m_decrypted}")
print(f"Déchiffrement réussi ? {m_decrypted == n_etudiant}")
