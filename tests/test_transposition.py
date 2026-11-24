import pytest
from cryptobox.classic.transposition import encrypt, decrypt


def test_exemple_enonce():
    assert encrypt("RENDEZVOUSAMIDI", "PORTE") == "ESIEVMRZANOIDUD"


def test_exemple_enonce_dechiffrement():
    assert decrypt("ESIEVMRZANOIDUD", "PORTE") == "RENDEZVOUSAMIDI"


def test_derniere_ligne_incomplete():
    # grille : ABC / DEF / G   ; ordre des colonnes : B, A, C
    assert encrypt("ABCDEFG", "BAC") == "BEADGCF"
    assert decrypt("BEADGCF", "BAC") == "ABCDEFG"


def test_lettres_repetees_gauche_a_droite():
    # grille : ABC / DEF ; ordre des colonnes : A(0), A(2), B(1)
    assert encrypt("ABCDEF", "ABA") == "ADCFBE"
    assert decrypt("ADCFBE", "ABA") == "ABCDEF"


def test_non_lettres_retirees():
    assert encrypt("Rendez-vous, Amidi !", "PORTE") == "ESIEVMRZANOIDUD"


@pytest.mark.parametrize(
    "key", ["SOLDAT", "PORTE", "LETTRE", "A", "ZYXWVUTSRQPONMLKJIHGFEDCBA"]
)
def test_aller_retour_toutes_longueurs(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for length in range(0, 60):
        message = (alphabet * 3)[:length]
        assert decrypt(encrypt(message, key), key) == message


@pytest.mark.parametrize("bad_key", ["", "123", "PO RTE", None, 42])
def test_cle_invalide(bad_key):
    with pytest.raises(ValueError):
        encrypt("ABC", bad_key)
    with pytest.raises(ValueError):
        decrypt("ABC", bad_key)
