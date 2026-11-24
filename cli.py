import argparse
import sys

from cryptobox.classic import caesar, substitution, transposition


def read_text(value):
    """Retourne le texte donné, ou lit l'entrée standard si value vaut '-'."""
    return sys.stdin.read() if value == "-" else value


def format_brute(text, results, highlight=None):
    """Met en forme le résultat de la force brute sous forme de petit tableau."""
    text = text.strip().replace("\n", " ")
    rows = {k: c.replace("\n", " ") for k, c in results.items()}
    keys = list(rows)
    width = max([len("texte déchiffré")] + [len(c) for c in rows.values()])
    separator = f"{'-' * 3}-+-{'-' * width}"

    lines = [
        "=== CryptoBox | César : force brute ===",
        f"Texte chiffré : {text}",
        f"Clés testées  : {len(rows)} (k = {keys[0]} à {keys[-1]})",
        "",
        f"{'k':>3} | texte déchiffré",
        separator,
    ]
    for k, candidate in rows.items():
        mark = ""
        if highlight and highlight.upper() in candidate:
            mark = "  <-- correspondance"
        lines.append(f"{k:>3} | {candidate}{mark}")
    lines.append(separator)
    lines.append(f"Terminé : {len(rows)} clés testées.")
    return "\n".join(lines)


def add_cipher(methods, name, module, help_text, key_help, key_type=str):
    """Ajoute la méthode `name` avec ses actions encrypt et decrypt."""
    method = methods.add_parser(name, help=help_text)
    actions = method.add_subparsers(dest="action", required=True)
    for action in ("encrypt", "decrypt"):
        p = actions.add_parser(action, help=f"{action} un message")
        p.add_argument("text", help="le message, ou '-' pour lire l'entrée standard")
        p.add_argument("-k", "--key", required=True, type=key_type, help=key_help)
        p.set_defaults(func=getattr(module, action))
    return actions


def build_parser():
    parser = argparse.ArgumentParser(
        prog="cryptobox",
        description="CryptoBox : outils de cryptographie classique.",
    )
    methods = parser.add_subparsers(dest="method", required=True)

    caesar_actions = add_cipher(
        methods, "caesar", caesar, "chiffre de César", "décalage (entier)", key_type=int
    )
    brute = caesar_actions.add_parser("brute", help="teste les 25 clés")
    brute.add_argument("text", help="le message, ou '-' pour lire l'entrée standard")
    brute.add_argument(
        "--contains",
        metavar="MOT",
        help="repère les clés dont le résultat contient ce mot",
    )

    add_cipher(
        methods,
        "substitution",
        substitution,
        "substitution simple",
        "clé de 26 lettres distinctes",
    )
    add_cipher(
        methods,
        "transposition",
        transposition,
        "transposition par colonnes",
        "mot-clé (lettres A-Z)",
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        text = read_text(args.text)
        if args.action == "brute":
            results = caesar.brute_force(text)
            print(format_brute(text, results, args.contains))
        else:
            print(args.func(text, args.key))
    except ValueError as error:
        print(f"Erreur : {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
