A = ord("A")


def _normalize_key(key):
    """Vérifie que la clé est un entier et la ramène entre 0 et 25."""
    if isinstance(key, bool) or not isinstance(key, int):
        raise ValueError("La clé César doit être un entier.")
    return key % 26


def encrypt(text, key):
    """Chiffre `text` avec un décalage `key`. Retourne le texte en majuscules."""
    shift = _normalize_key(key)
    result = []
    for c in text.upper():
        if "A" <= c <= "Z":
            result.append(chr((ord(c) - A + shift) % 26 + A))
        else:
            result.append(c)  # espaces, ponctuation, chiffres, accents : inchangés
    return "".join(result)


def decrypt(text, key):
    """Déchiffre `text` chiffré avec le décalage `key`."""
    _normalize_key(key)  # même validation que encrypt
    return encrypt(text, -key)


def brute_force(text):
    """Retourne un dict {k: texte déchiffré avec k} pour k de 1 à 25."""
    return {k: decrypt(text, k) for k in range(1, 26)}
