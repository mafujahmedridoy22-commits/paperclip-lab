"""paperclip command-line entry point."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="paperclip")
    subparsers = parser.add_subparsers(dest="command", required=True)

    hello = subparsers.add_parser("hello", help="greet someone")
    hello.add_argument("name", help="name of the person to greet")

    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    if args.command == "hello":
        print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
