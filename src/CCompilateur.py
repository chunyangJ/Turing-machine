#!/usr/bin/env python3
import sys
from CQuadruplet import CQuadruplet


class CCompilateur:
    """Compilateur de programme TS.

    Un compilateur "traduit" le programme source TS en langage de
    machine de Turing (reconnaissable à Python), ie un tableau de quadruplets.

    Attributes:
        ZU(str): class variable, '0' ou '1', symbole
        XX(int): class variable, sert à générer de nouveaux états
        __programme(str): chaîne de caractères du programme source TS
        pTuring(list): tableau de quadruplets
        __pile(list): sert à marquer le début de la compilation,
        ainsi que la boucle et la fin (de boucle)
        __p(int): position d'un caractète dans le programme source TS
        __etatDEntree(int): état d'entrée

    Methods:
        __nouvelEtat(), initCompiler(), compiler(), __AXIOME(), __PROGRAMME(
        ), __INSTRUCTION(), __FIN(), __COMMENTAIRE(), __BOUCLE(), __SI(),
        __GAUCHE(), __DROITE(), __BATON(), __ZERO(), __PAUSE(), __IMPRIMER(
        ), __PARENTHESE_OUVRANTE(), __PARENTHESE_FERMANTE(),
        __ACCOLADE_FERMANTE(), __ZERO_OU_UN(), __ESPACE();
        __error_carac(carac), __error_mot_cle(mot_cle), __error_autre(autre).

    """
    ZU = None
    XX = None

    def __nouvelEtat(self):
        """génère un nouvel état

        Returns:
            XX: class type, nouvel état
        """
        type(self).XX += 1

        return type(self).XX

    def __init__(self, c):
        """initialise un compilateur pour le programme source

        Args:
            c: chaîne de caractères de programme source TS
        """
        assert isinstance(c, str)
        self.__programme = str(c)
        self.initCompiler()


    def initCompiler(self):
        """initialise le compilateur

        """
        self.pTuring = list()
        self.__pile = list()
        self.__p = 0
        type(self).XX = -1


    def compiler(self):
        """compile

        indique l'erreur de syntaxe en foction de code d'erreurs retourné par
        l'éxécution de __AXIOME()
        """
        self.initCompiler()
        self.__pile.append(self.__nouvelEtat())
        self.__etatDEntree = self.__nouvelEtat()

        e = self.__AXIOME()
        if e != 0:
            print("erreur de syntaxe : ", end="")
            switch = {
                '2': (self.__error_mot_cle, 'si'),
                '3': (self.__error_carac, '('),
                '4': (self.__error_carac, ')'),
                '5': (self.__error_carac, '}'),
                '7': (self.__error_carac, 'G'),
                '8': (self.__error_carac, 'D'),
                '9': (self.__error_mot_cle, 'fin'),
                '10': (self.__error_carac, '1'),
                '11': (self.__error_carac, '0'),
                '12': (self.__error_carac, 'P'),
                '13': (self.__error_carac, 'I'),
                '14': (self.__error_carac, '#'),
                '15': (self.__error_mot_cle, 'boucle'),
                '19': (self.__error_autre, 'instruction attendue'),
                '20': (self.__error_carac, '%'),
                '22': (self.__error_carac, '0 ou 1'),
            }
            error_decision = switch.get(str(e), (self.__error_autre, 'erreur inconnue'))
            error_decision[0](error_decision[1])
            print(
                " à la position {} du programme source :\n{}".format(
                    self.__p, self.__programme[0:self.__p])
            )
            sys.exit(1)

    def __AXIOME(self):
        """ __AXIOME() ---> __PROGRAMME() __ESPACES() '#'

        Return:
            e: code d'erreur
        """
        e = None
        e = self.__PROGRAMME()
        if e != 0:
            return e
        e = self.__ESPACES()
        if self.__programme[self.__p] != '#':
            return 14
        self.__p += 1
        return 0

    def __PROGRAMME(self):
        """__PROGRAMME() ---> '#' | '}' | __INSTRUCTION() __ESPACES()
        __PROGRAMME()

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] == '#':
            return 0
        if self.__programme[self.__p] == '}':
            return 0

        e = None
        e = self.__INSTRCUTION()
        if e != 0:
            return e
        e = self.__ESPACES()
        e = self.__PROGRAMME()
        if e != 0:
            return e

        return 0

    def __INSTRCUTION(self):
        """__INSTRUCTION ---> __GAUCHE() | __BOUCLE() | __SI() | __FIN() |
        __DROITE() | __BATON() | __ZERO() | __PAUSE() | __IMPRIMER() |
        __COMMENTAIRE()

        Return:
            e: code d'erreur
        """
        e = None
        if self.__programme[self.__p] == 'G':
            e = self.__GAUCHE()
            if e != 0:
                return e
            return 0
        elif self.__programme[self.__p] == 'b':
            e = self.__BOUCLE()
            if e != 0:
                return e
            return 0
        elif self.__programme[self.__p] == 's':
            e = self.__SI()
            if e != 0:
                return e
            return 0
        elif self.__programme[self.__p] == 'f':
            e = self.__FIN()
            if e != 0:
                return e
            return 0
        elif self.__programme[self.__p] == 'D':
            e = self.__DROITE()
            if e != 0:
                return e
            return 0
        elif self.__programme[self.__p] == '1':
            e = self.__BATON()
            if e != 0:
                return e
            return 0
        elif self.__programme[self.__p] == '0':
            e = self.__ZERO()
            if e != 0:
                return 0
            return e
        elif self.__programme[self.__p] == 'P':
            e = self.__PAUSE()
            if e != 0:
                return e
            return 0
        elif self.__programme[self.__p] == 'I':
            e = self.__IMPRIMER()
            if e != 0:
                return e
            return 0
        elif self.__programme[self.__p] == '%':
            e = self.__COMMENTAIRE()
            if e != 0:
                return e
            return 0

        return 19

    def __FIN(self):
        """ __FIN() ---> 'f' 'i' 'n'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != 'f':
            return 9
        self.__p += 1
        if self.__programme[self.__p] != 'i':
            return 9
        self.__p += 1
        if self.__programme[self.__p] != 'n':
            return 9
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        q1 = self.__pile[-1] # peek()

        self.pTuring.append(CQuadruplet(q0, '0', '0', q1, "FIN"))
        self.pTuring.append(CQuadruplet(q0, '1', '1', q1, "FIN"))
        self.__etatDEntree = etatDeSortie

        return 0

    def __COMMENTAIRE(self):
        """__COMMENTAIRE ---> '%'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != '%':
            return 20

        while True:
            self.__p += 1
            if self.__programme[self.__p] == '\n':
                break

        return 0

    def __BOUCLE(self):
        """__BOUCLE ---> 'b' 'o' 'u' 'c' 'l' 'e' __ESPACES() __PROGRAMME()
        __ESPACES() __ACCOLADE_FERMANTE()

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != 'b':
            return 15
        self.__p += 1
        if self.__programme[self.__p] != 'o':
            return 15
        self.__p += 1
        if self.__programme[self.__p] != 'u':
            return 15
        self.__p += 1
        if self.__programme[self.__p] != 'c':
            return 15
        self.__p += 1
        if self.__programme[self.__p] != 'l':
            return 15
        self.__p += 1
        if self.__programme[self.__p] != 'e':
            return 15
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        self.__pile.append(etatDeSortie)

        e = None
        e = self.__ESPACES()
        e = self.__PROGRAMME()
        if e != 0:
            return e
        e = self.__ESPACES()
        e = self.__ACCOLADE_FERMANTE()
        if e != 0:
            return e

        self.pTuring.append(CQuadruplet(self.__etatDEntree, '0', '0', q0,
                                        "BLC"))
        self.pTuring.append(CQuadruplet(self.__etatDEntree, '1', '1', q0,
                                        "BLC"))
        self.__etatDEntree = etatDeSortie

        self.__pile.pop()

        return 0

    def __SI(self):
        """__SI() ---> 's' 'i' __ESPACES() __PARENTHESE_OUVRANTE()
        __ESPACES() __ZERO_OU_UN() __ESPACES() __PARENTHESE_FERMANTE()
        __ESPACES() __PROGRAMME() __ESPACES() __ACCOLADE_FERMANTE()

        Returns:
            e: code d'erreur
        """
        if self.__programme[self.__p] != 's':
            return 2
        self.__p += 1
        if self.__programme[self.__p] != 'i':
            return 2
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        q1 = self.__nouvelEtat()

        e = None
        e = self.__ESPACES()
        e = self.__PARENTHESE_OUVRANTE()
        if e != 0:
            return e
        e = self.__ESPACES()
        e = self.__ZERO_OU_UN()
        if e != 0:
            return e
        c0 = type(self).ZU
        e = self.__ESPACES()
        e = self.__PARENTHESE_FERMANTE()
        if e != 0:
            return e
        if c0 == '0':
            self.pTuring.append(CQuadruplet(q0, '0', '0', q1, "SI "))
            self.pTuring.append(CQuadruplet(q0, '1', '1', etatDeSortie, "SI "))
        else:
            self.pTuring.append(CQuadruplet(q0, '0', '0', etatDeSortie, "SI "))
            self.pTuring.append(CQuadruplet(q0, '1', '1', q1, "SI "))

        e = self.__ESPACES()
        self.__etatDEntree = q1
        e = self.__PROGRAMME()
        if e != 0:
            return e
        e = self.__ESPACES()
        e = self.__ACCOLADE_FERMANTE()
        if e != 0:
            return e

        self.pTuring.append(CQuadruplet(self.__etatDEntree, '0', '0', etatDeSortie, "SI "))
        self.pTuring.append(CQuadruplet(self.__etatDEntree, '1', '1', etatDeSortie, "SI "))
        self.__etatDEntree = etatDeSortie

        return 0

    def __GAUCHE(self):
        """__GAUCHE() ---> 'G'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != 'G':
            return 7
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        self.pTuring.append(CQuadruplet(q0, '0', 'G', etatDeSortie, "GAU"))
        self.pTuring.append(CQuadruplet(q0, '1', 'G', etatDeSortie, "GAU"))
        self.__etatDEntree = etatDeSortie

        return 0

    def __DROITE(self):
        """__DROITE() ---> 'D'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != 'D':
            return 8
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        self.pTuring.append(CQuadruplet(q0, '0', 'D', etatDeSortie, "DRO"))
        self.pTuring.append(CQuadruplet(q0, '1', 'D', etatDeSortie, "DRO"))
        self.__etatDEntree = etatDeSortie

        return 0

    def __BATON(self):
        """__BATON() ---> '1'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != '1':
            return 10
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        self.pTuring.append(CQuadruplet(q0, '0', '1', etatDeSortie, "BAT"))
        self.pTuring.append(CQuadruplet(q0, '1', '1', etatDeSortie, "BAT"))
        self.__etatDEntree = etatDeSortie

        return 0

    def __ZERO(self):
        """__ZERO() ---> '0'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != '0':
            return 11
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        self.pTuring.append(CQuadruplet(q0, '0', '0', etatDeSortie, "ZER"))
        self.pTuring.append(CQuadruplet(q0, '1', '0', etatDeSortie, "ZER"))
        self.__etatDEntree = etatDeSortie

        return 0

    def __PAUSE(self):
        """__PAUSE() ---> 'P'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != 'P':
            return 12
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        self.pTuring.append(CQuadruplet(q0, '0', 'P', etatDeSortie, "PAU"))
        self.pTuring.append(CQuadruplet(q0, '1', 'P', etatDeSortie, "PAU"))
        self.__etatDEntree = etatDeSortie

        return 0

    def __IMPRIMER(self):
        """__IMPRIMER() ---> 'I'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != 'I':
            return 13
        self.__p += 1

        q0 = self.__etatDEntree
        etatDeSortie = self.__nouvelEtat()
        self.pTuring.append(CQuadruplet(q0, '0', 'I', etatDeSortie, "IMP"))
        self.pTuring.append(CQuadruplet(q0, '1', 'I', etatDeSortie, "IMP"))
        self.__etatDEntree = etatDeSortie

        return 0

    def __PARENTHESE_OUVRANTE(self):
        """__PARENTHESE_OUVRANTE() ---> '('

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != '(':
            return 3
        self.__p += 1

        return 0

    def __PARENTHESE_FERMANTE(self):
        """__PARENTHESE_FERMANTE() ---> ')'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != ')':
            return 4
        self.__p += 1

        return 0


    def __ACCOLADE_FERMANTE(self):
        """__ACCOLADE_FERMANTE() ---> '}'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] != '}':
            return 5
        self.__p += 1

        return 0

    def __ZERO_OU_UN(self):
        """__ZERO_OU_UN() ---> '0' | '1'

        Return:
            e: code d'erreur
        """
        if self.__programme[self.__p] not in "01":
            return 22
        type(self).ZU = self.__programme[self.__p]
        self.__p += 1

        return 0

    def __ESPACES(self):
        """__ESPACES() ---> '\t' | '\n' | '\r' | ' '

        Return:
            e: code d'erreur
        """
        while True:
            if self.__programme[self.__p] not in "\t\n\r ":
                break
            self.__p += 1

        return 0

# les cas infra indiquent des erreurs syntaxes du programme source

    def __error_carac(self, carac):
        """affiche erreur syntaxe en fonction de type de caractère attendu.
        Arg:
           carac(str): caractère attendu
        """
        print("caractère {} attendu".format(carac), end="")

    def __error_mot_cle(self, mot_cle):
        """affiche erreur syntaxe en fonction de type de mot clé attendu.
        Arg:
           mot_cle(str): mot clé attendu
        """
        print("mot clé <{}> attendu".format(mot_cle), end="")

    def __error_autre(self, autre):
        """affiche d'autre type d'erreur syntaxe.

        Arg:
           autre(str): autre type d'erreur
        """
        print(autre, end="")


