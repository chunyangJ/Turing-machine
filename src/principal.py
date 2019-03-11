#!/usr/bin/env python3
# usage: python3 principle <path-to-programmeTS> [n1 [n2]]
import sys

from CCompilateur import CCompilateur
from CExecution import CExecution
from CMachine import CMachine
from CRuban import CRuban


def main():
    """Compile et exécute le programme source TS en entrée."""
    chaine = lireProgramme()
    c = CCompilateur(chaine)
    c.compiler()
    MT = CMachine(sys.argv[1], chaine, c.pTuring)
    c = None

    n1, n2 = lireArguments()
    R = CRuban(n1, n2)  # le constructeur prend 2 args (l'oeil est au milieu)
    exec = CExecution(MT, 1, R)  # état initial: 1
    exec.interprete()


def lireProgramme():
    """lit le programme source TS

    Return:
        chaine: chaîne de caractères du programme source TS
    """
    if len(sys.argv) <= 1:
        usage()
        sys.stderr.write("paramètres d'appel incorrects\n")
        sys.exit(1)
    chaine = ""
    try:
        with open(sys.argv[1], encoding="iso-8859-1") as f_stream:
            while True:
                c = f_stream.read(1)
                if not c:
                    break
                chaine += c
    except FileNotFoundError as Error_no_file:
        usage()
        sys.stderr.write("{} {}\n".format(sys.argv[0], Error_no_file))
        sys.exit(1)
    except IOError as Error_io:
        usage()
        sys.stderr.write("{} {}\n".format(
            sys.argv[0], Error_io))
        sys.exit(1)
    return chaine


def lireArguments():
    """lit les arguments pour le programme source

    Returns:
        (n1, n2): arguments pour le programme source TS
    """
    try:
        if len(sys.argv) >= 4:
            n1 = int(sys.argv[2])
            n2 = int(sys.argv[3])
        elif len(sys.argv) == 3:
            n1 = int(sys.argv[2])
            n2 = -1
        elif len(sys.argv) == 2:
            n1 = -1
            n2 = -1
        else:
            n1 = 0
            n2 = 0
    except ValueError as Error_val:
        usage()
        sys.stderr.write("{} {}\n".format(sys.argv[1], Error_val))
        sys.exit(1)
    return (n1, n2)


def usage():
    """usage: python3 principle <path-to-programmeTS> [n1 [n2]]
        n1: entier positif, argument du programme TS
        n2: entier positif, argument du programme TS"""
    print(usage.__doc__)

if __name__ == '__main__':
    main()
