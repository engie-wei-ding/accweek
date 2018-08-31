class PorteFeuille():

    def __init__(self, montant=0):
        self._balance = montant

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, montant):
        self._balance = montant
        return self

    def depenser(self, montant):
        if self.balance < montant:
            raise ValueError("Operation refusee! Pas assez d'argent")
        else:
            self.balance -= montant
        return self

    def deposer(self, montant):
        self.balance += montant
        return self

    def __str__(self):
        return 'balance : {}'.format(self.balance)
