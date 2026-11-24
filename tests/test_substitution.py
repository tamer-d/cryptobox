import pytest
from cryptobox.classic.substitution import encrypt, decrypt

KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_exemple_enonce():
    assert encrypt("ATTAQUE", KEY) == "QZZQJXT"


def test_aller_retour():
    assert decrypt("QZZQJXT", KEY) == "ATTAQUE"
    assert decrypt(encrypt(ALPHABET, KEY), KEY) == ALPHABET


def test_cle_identite():
    assert encrypt("Bonjour", ALPHABET) == "BONJOUR"


def test_non_lettres_conserves():
    assert encrypt("Attaque à l'aube !", KEY) == "QZZQJXT À S'QXWT !"


def test_cle_en_minuscules():
    assert encrypt("ATTAQUE", KEY.lower()) == "QZZQJXT"


@pytest.mark.parametrize(
    "bad_key",
    [
        "ABC",  # trop courte
        "A" * 26,  # lettres répétées
        "1234567890" * 2 + "ABCDEF",  # pas des lettres
        "QWERTYUIOPASDFGHJKLZXCVBN",  # 25 lettres
        "",  # vide
        None,  # pas une chaîne
    ],
)
def test_cle_invalide(bad_key):
    with pytest.raises(ValueError):
        encrypt("ABC", bad_key)
    with pytest.raises(ValueError):
        decrypt("ABC", bad_key)
