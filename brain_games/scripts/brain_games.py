#!/usr/bin/env python3
from brain_games.scripts.cli import welcome_user


def main():
    print("poetry run python -m brain_games.scripts.brain_games\n"
          "Welcome to the Brain Games!")
    welcome_user()


if __name__ == "__main__":
    main()
