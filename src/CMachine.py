#!/usr/bin/env python3


class CMachine:
    """une machine de Turing

    Attributes:
         __nomDuFichier(str)
         __programmeSource(str)
         programmeT(list)

    Method:
        afficher()
    """
    def __init__(self, nom_fichier, programme_source, programme_turing):
        """Initialise l'instance machine en fonction de programme source

        Args:
            nom_fichier: nom du fichier du programme TS
            programme_source: programme TS
            programme_turing: programme compilé par le compilateur (une
            liste de quadruplet)
        """
        self.__nomDuFichier = nom_fichier
        self.__programmeSource = programme_source
        self.programmeT = [prog for prog in programme_turing]

    def afficher(self):
        """imprime le programme(liste de quadruplet).
        """
        for i in range(len(self.programmeT)):
            self.programmeT[i].afficher()
