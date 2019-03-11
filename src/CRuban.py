#!/usr/bin/env python3
import sys


class CRuban:
    """un ruban (taille finie) de la machine de Turing.

    Attributes:
        DIM(int): class variable, taille du ruban.
        ruban(list): la bande, vide par défaut (remplie par '0')
        oeil(int): la position de la tête de lecture.

    Methods:
        cellule(i), affecter(i, v), afficher()
    """
    DIM = 70  # type: int

    def __init__(self, *args):
        """Initialise l'instance ruban en fonction de nombre de arguments.

        Deux nombres sont séparés par 00 sur le ruban,
        les nombres en entrée sont représentés en unaire sur le ruban,
        la position de l'oeil est toujours au milieu sauf que p soit désigné.

        Examples: 1 représente 0, 11 représente 1, 111 représente 2, ...

        Args:
            *args: (n1, n2) ou (p, n1, n2)
        """
        self.ruban = ['0'] * type(self).DIM
        if len(args) == 3:
            # la position de l'oeil est désignée
            p, n1, n2 = args
            if int(type(self).DIM / 2) < n1 + n2 + 4:
                sys.stderr.write("[ValueError] valeurs trop grandes\n")
                sys.exit(1)
            k = p
            for i in range(n1 + 1):
                self.ruban[k] = '1'
                k += 1
            k += 2
            for i in range(n2 + 1):
                self.ruban[k] = '1'
                k += 1
            self.oeil = p
        elif len(args) == 2:
            n1, n2 = args
            if int(type(self).DIM / 2) < n1 + n2 + 4:
                sys.stderr.write("[ValueError] valeurs trop grandes\n")
                sys.exit(1)
            p = int(type(self).DIM / 2)
            k = p
            for i in range(n1 + 1):
                self.ruban[k] = '1'
                k += 1
            k += 2
            for i in range(n2 + 1):
                self.ruban[k] = '1'
                k += 1
            self.oeil = p
        else:
            # 0, 1 or more than 3 args
            self.oeil = int(type(self).DIM / 2)

    def cellule(self, i):
        """récupère la valeur de la case i du ruban.

        Arg:
            i(int): la position de la case voulue.
        Return:
            la valeur de la case.
        """
        return self.ruban[i]

    def affecter(self, i, v):
        """affecte la valeur v à la case i du ruban.

        Args:
            i(int): la position de la case voulue.
            v(str): la valeur à affecter.
        """
        self.ruban[i] = v

    def afficher(self):
        """affiche le ruban sur le stdout.

        La première ligne est le ruban,
        la deuxième ligne montre la position de la tête.
        """
        for i in range(len(self.ruban)):
            print(self.ruban[i], end='')
        print('\n', ' ' * self.oeil, 'X', sep='')
