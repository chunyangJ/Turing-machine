#!/usr/bin/env python3


class CQuadruplet:
    """quadruplet de la machine de Turing.

    Une instance de quadruplet est une transition.

    Attributes:
        etatI(int), caractere(str), action(str), etatF(int), __provenance(str)

    Method:
        afficher(): affiche le quadruplet et sa provenance.
    """
    def __init__(self, etat_entree, caractere, action, etat_sortie,
                 provenance):
        """Initialise un quadruplet.

        Args:
            etat_entree(int): l'état d'entrée d'une transition
            caractere(str): un élément de {'0', '1'}, la valeur lue par la tête
            action(str): un élément de {'G', 'D',S '1', '0', 'P', 'I'}
            etat_sortie(int): l'état de sortie d'une transition
            provenance(str): user-friendly, qui indique la provenance de
            cette transition, un élément de {"FIN", BCL", "SI ", "GAU", "DRO",
            "BAT", "ZER", "PAU", "IMP"}
        """
        self.etatI = etat_entree
        self.caractere = caractere
        self.action = action
        self.etatF = etat_sortie
        self.__provenance = provenance

    def afficher(self):
        """affiche le quadruplet (y compris la provenance) sur le stdout."""
        print(self.__provenance, self.etatI, self.caractere, self.action,
              self.etatF)
