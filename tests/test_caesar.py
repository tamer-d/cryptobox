import pytest
from cryptobox.classic.caesar import encrypt, decrypt, brute_force


def test_exemple_enonce():
    assert encrypt("BONJOUR", 3) == "ERQMRXU"


def test_aller_retour():
    assert decrypt(encrypt("BONJOUR", 3), 3) == "BONJOUR"


def test_cle_modulo():
    assert encrypt("ABC", 29) == encrypt("ABC", 3)
    assert encrypt("ABC", -1) == "ZAB"


def test_non_lettres_conserves():
    assert encrypt("Bonjour, le monde !", 3) == "ERQMRXU, OH PRQGH !"


def test_cle_invalide():
    with pytest.raises(ValueError):
        encrypt("ABC", "x")


def test_brute_force():
    resultats = brute_force("ERQMRXU")
    assert len(resultats) == 25
    assert resultats[3] == "BONJOUR"
