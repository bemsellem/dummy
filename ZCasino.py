#! /usr/bin/env python3
import os
from random import randrange
from math import ceil

cash = 100
jeu = ""

while jeu.upper() != "Q":
    mise = -1
    while mise <= 0 and mise > cash:
        mise = input("Quelle mise voulez vous parier ?")
        try:
            mise = int(mise)
        except ValueError:
            print("Votre saisie n'est pas un nombre.")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        elif mise > cash:
            print("Vous ne pouvez pas miser plus que ce que vous possédez.")
    cash -= mise

    case = -1
    while not 0 <= case <= 49:
        case = input("Sur quelle case voulez vous parier ?")
        try:
            case = int(case)
        except ValueError:
            print("Votre saisie n'est pas un nombre.")
            mise = -1
            continue
        if mise < 0:
            print("La case saisie est négative.")
        elif mise > 49:
            print("Vous ne pouvez pas miser sur un numéro plus grand que 49.")

    lancer = randrange(50)
    if lancer == case:
        print("Vous gagnez",str(3 * mise),"dollars.")
        cash += cash + cash * 3
    elif (lancer%2 == mise%2):
        print("Vous gagnez",str(ceil(0.5 * mise)),"dollars.")
        cash += cash + ceil(0.5 * cash)
    else:
        print("Vous avez perdu.")

    if cash == 0:
        print("Vous êtes ruiné")
        jeu = "Q"
    else:
        print("Votre solde est de", cash, "dollars.")
        jeu = input("Voulez-vous continuer à jouer (o / q) ?")

os.system("pause")
