class PorteFeuille():

    def __init__(self, initial_montant=0):
        self.balance = initial_montant

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, montant):
        if isinstance(montant, str):
            raise ValueError('Montant doit etre numerique')
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
