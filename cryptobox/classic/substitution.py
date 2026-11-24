ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def _validate_key(key):
    """Vérifie que la clé contient les 26 lettres, chacune une fois. Retourne la clé en majuscules."""
    if not isinstance(key, str):
        raise ValueError("La clé doit être une chaîne de 26 lettres.")
    key = key.upper()
    if len(key) != 26 or set(key) != set(ALPHABET):
        raise ValueError(
            "La clé doit contenir les 26 lettres de A à Z, chacune une seule fois."
        )
    return key


def _translate(text, source, target):
    """Remplace chaque lettre de `source` par la lettre de même rang dans `target`."""
    table = dict(zip(source, target))
    return "".join(table.get(c, c) for c in text.upper())


def encrypt(text, key):
    """Chiffre `text` : la lettre de rang i de l'alphabet devient la lettre de rang i de la clé."""
    key = _validate_key(key)
    return _translate(text, ALPHABET, key)


def decrypt(text, key):
    """Déchiffre `text` : on applique la table inverse (clé vers alphabet)."""
    key = _validate_key(key)
    return _translate(text, key, ALPHABET)
