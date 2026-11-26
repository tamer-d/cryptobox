from cryptobox.classic import caesar, substitution, transposition

CIPHERTEXT = "LXHXLXVBTNDX"
SUBST_KEY = "VYMXKQDTSRGCZFAJBUIPLONEWH"  # couche 1
TRANSP_KEY = "SOLDAT"  # couche 3


def main():
    # Couche 3 : la transposition ne dépend pas de k, on la retire une seule fois
    after_l3 = transposition.decrypt(CIPHERTEXT, TRANSP_KEY)

    print("=== CryptoBox | Challenge binôme 30 ===")
    print(f"Message intercepté     : {CIPHERTEXT}")
    print(f"Après couche 3 (transp.): {after_l3}")
    print()
    print("  k | message déchiffré")
    print("----+------------------")

    # Couche 2 : César, clé inconnue -> on teste les 25 clés
    for k in range(1, 26):
        after_l2 = caesar.decrypt(after_l3, k)
        # Couche 1 : substitution
        plain = substitution.decrypt(after_l2, SUBST_KEY)
        print(f"{k:>3} | {plain}")


if __name__ == "__main__":
    main()
