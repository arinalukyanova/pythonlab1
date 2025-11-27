import argparse
from pathlib import Path

from lab03.text_stats import text_stats


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, type=Path)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частота строк")
    stats_parser.add_argument("--input", type=str, required=True)
    stats_parser.add_argument("--top", type=int, default=5)
    stats_parser.add_argument("-p", action="store_true", help="Output in table form")

    args = parser.parse_args()

    if not args.command:
        parser.error("You")

    if args.command == "cat":
        with args.input.open("r", encoding="utf-8") as f:
            for number, text in enumerate(f):
                if args.n:
                    print(f"{number + 1}: {text.strip()}")
                else:
                    print(text.strip())
    elif args.command == "stats":
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
        text_stats(text, n=args.top)


if __name__ == "__main__":
    main()
