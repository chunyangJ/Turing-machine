#!/usr/bin/env python3
import sys

from CRuban import CRuban


class CExecution:
    """une exécution de suite de programmes de la machine de Turing.

    Attributes:
        MT(CMachine), etatCrt(int), ruban(CRuban)

    Methods:
        interprete(): effectue la transition,
        __case1(arg), __case2(arg), __case3(arg), __case4(arg), __case5(arg)

    """
    def __init__(self, machine_turing, etat_courant, ruban):
        """initialise une instance d'exécution.

        Args:
            machine_turing:
            etat_courant:
            ruban:
        """
        self.MT = machine_turing
        self.etatCrt = etat_courant
        self.ruban = ruban

    def interprete(self):
        """parse les règles de transitions et les traduits en langage Python.

        Selon l'état d'entrée et le symbole lu sous la tête de lecture,
        fait l'action et passe à l'état suivant.
        """
        while True:
            c = None
            c = self.ruban.cellule(self.ruban.oeil)
            quad = None
            i = 0
            b1 = False
            while True:
                if i >= len(self.MT.programmeT):
                    b1 = True
                    break
                quad = self.MT.programmeT[i]
                if (quad.etatI == self.etatCrt) and (quad.caractere == c):
                    break
                i += 1

            if b1:
                break
            switch = {
                'G': self.__case1,
                'D': self.__case2,
                '1': self.__case3,
                '0': self.__case3,
                'P': self.__case4,
                'I': self.__case5,
            }
            switch[quad.action](quad.action)
            self.etatCrt = quad.etatF

    # Les actions que la tête de lecture peuvent effectuer

    def __case1(self, arg):
        """déplace la tête de lecture d'une position vers la gauche.

        Arg:
            arg: 'G'
        """
        self.ruban.oeil -= 1
        if 0 > self.ruban.oeil:
            sys.stderr.write("[Error] plus de place à gauche\n")
            sys.exit(1)

    def __case2(self, arg):
        """déplace la tête de lecture d'une position vers la droite.

        Arg:
            arg: 'D'
        """
        self.ruban.oeil += 1
        if CRuban.DIM <= self.ruban.oeil:
            sys.stderr.write("[Error] plus de place à droite\n")
            sys.exit(1)

    def __case3(self, arg):
        """écrit un symbole à la place du symbole sous la tête de lecture.

        Arg:
           arg: '0', le symbole sous la tête de lecture devient '0' (efface),
               '1', le symbole sous la tête de lecture devient '1' (écrit).
        """
        self.ruban.affecter(self.ruban.oeil, arg)

    @staticmethod
    def __case4(arg):
        """pause, attend un stdin pour continuer.

        Arg:
           arg: 'P'
        """
        try:
            input("appuyer sur une touche pour continuer : ")
        except IOError as e:
            sys.stderr.write(e)
            sys.exit(1)

    def __case5(self, arg):
        """imprime le ruban sur le stdout.

        Arg:
           arg: 'I'
        """
        self.ruban.afficher()
