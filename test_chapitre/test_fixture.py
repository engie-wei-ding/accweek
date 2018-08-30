import pytest

from chapitre_fixture import PorteFeuille

def test_1():
    mon_porte_feuille = PorteFeuille()
    assert mon_porte_feuille._balance == 0

def test_2():
    mon_porte_feuille = PorteFeuille()
    mon_porte_feuille.deposer(50)
    assert mon_porte_feuille._balance == 50

def test_3():
    mon_porte_feuille = PorteFeuille(initial_montant = 100)
    mon_porte_feuille.deposer(50)
    assert mon_porte_feuille._balance == 150

@pytest.fixture
def porte_feuille_vide():
    return PorteFeuille()

# porte_feuille_vide : un instant de classe PorteFeuille avec initial_montant = 0
def test_4(porte_feuille_vide):
    porte_feuille_vide.deposer(50)
    assert porte_feuille_vide._balance == 50

@pytest.fixture
def porte_feulle_50_euros():
    return PorteFeuille(initial_montant=50)

def test_5(porte_feulle_50_euros):
    porte_feulle_50_euros.deposer(50)
    assert porte_feulle_50_euros._balance == 100

def test_6(porte_feulle_50_euros):
    with pytest.raises(ValueError):
        porte_feulle_50_euros.depenser(100)


#use pytest.mark.parametrize to simulate the different situations

@pytest.mark.parametrize("deposer_montant, denperser_montant, balance_montant",[
                            (100, 50, 50),
                            (25, 5, 20),
                            (1000, 0, 1000)
])
def test_7(deposer_montant, denperser_montant, balance_montant):
    mon_porte_feuille = PorteFeuille()
    mon_porte_feuille.deposer(deposer_montant)
    mon_porte_feuille.depenser(denperser_montant)
    assert mon_porte_feuille._balance == balance_montant

#use fixture with pytest.mark.parametrize


@pytest.mark.parametrize("deposer_montant, denperser_montant, balance_montant",[
                            (100, 50, 100),
                            (25, 5, 70),
                            (1000, 0, 1050)
])
def test_8(porte_feulle_50_euros, deposer_montant, denperser_montant, balance_montant):
    porte_feulle_50_euros.deposer(deposer_montant)
    porte_feulle_50_euros.depenser(denperser_montant)
    assert porte_feulle_50_euros._balance == balance_montant










