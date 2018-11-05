# -*-coding:utf-8 -*

"""module multipli contenant la fonction table"""

import os

def table(nb, maxi=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à maxi * nb"""
    i = 0
    while i < maxi:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

# test de la fonction table
if __name__ == "__main__":
    table(4)
    os.system("pause")
