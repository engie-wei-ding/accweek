class PorteFeuille():

    def __init__(self, montant=0):
        self._balance = montant

    @property
    def montant(self):
        return self._balance

    @montant.setter
    def montant(self, montant):
        self._balance = montant
        return self

    def depenser(self, montant):
        if self._balance < montant:
            raise ValueError("Operation refusee! Pas assez d'argent")
        else:
            self._balance -= montant
        return self

    def deposer(self, montant):
        self._balance += montant
        return self

    def __str__(self):
        return 'balance : {}'.format(self._balance)
