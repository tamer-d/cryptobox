def _validate_key(key):
    """Le mot-clé doit être une chaîne non vide de lettres A-Z. Retourne la clé en majuscules."""
    if not isinstance(key, str) or not key:
        raise ValueError("Le mot-clé doit être une chaîne non vide.")
    key = key.upper()
    if not all("A" <= c <= "Z" for c in key):
        raise ValueError("Le mot-clé ne doit contenir que des lettres de A à Z.")
    return key


def _clean(text):
    """Met en majuscules et ne garde que les lettres A-Z."""
    return "".join(c for c in text.upper() if "A" <= c <= "Z")


def _column_order(key):
    """Indices des colonnes dans l'ordre de lecture (alphabétique, égalités de gauche à droite)."""
    return sorted(range(len(key)), key=lambda i: (key[i], i))


def encrypt(text, key):
    """Chiffre `text` par transposition en colonnes avec le mot-clé `key`."""
    key = _validate_key(key)
    letters = _clean(text)
    n = len(key)
    return "".join(letters[col::n] for col in _column_order(key))


def decrypt(text, key):
    """Déchiffre un texte chiffré par `encrypt` avec le même mot-clé."""
    key = _validate_key(key)
    letters = _clean(text)
    n = len(key)
    full, extra = divmod(len(letters), n)

    # Découper le texte chiffré en colonnes, dans l'ordre de lecture
    columns = [""] * n
    pos = 0
    for col in _column_order(key):
        length = full + (1 if col < extra else 0)
        columns[col] = letters[pos : pos + length]
        pos += length

    # Relire la grille ligne par ligne
    result = []
    for row in range(full + (1 if extra else 0)):
        for col in range(n):
            if row < len(columns[col]):
                result.append(columns[col][row])
    return "".join(result)
