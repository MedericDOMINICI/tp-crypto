from Ex1 import euclide_etendu, exponentiation_modulaire_rapide, inverse_a_modulo_n
from ex2 import generer_premier

def generer_cle_rsa(k=512, e=115670849):
    while True:
        p = generer_premier(k)
        q = generer_premier(k)
        if p != q:
            n = p * q
            phi_n = (p - 1) * (q - 1)
            if euclide_etendu(e, phi_n)[0] == 1:
                return p, q, n, phi_n, e

p, q, n, phi_n, e = generer_cle_rsa()

n_etudiant = 123456789
c = exponentiation_modulaire_rapide(n_etudiant, e, n)

d = inverse_a_modulo_n(e, phi_n) % phi_n
m_decrypted = exponentiation_modulaire_rapide(c, d, n)

print(f"Message original : {n_etudiant}")
print(f"Chiffrement : {c}")
print(f"Déchiffrement : {m_decrypted}")
print(f"Déchiffrement réussi ? {m_decrypted == n_etudiant}")
