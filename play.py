# Root-level launcher: pick a playground.py to run without cd'ing into its folder.
# AI WRITTEN

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {".venv", "__pycache__", ".git", ".pytest_cache"}


def find_playgrounds():
    playgrounds = [
        p for p in ROOT.rglob("playground.py")
        if not SKIP_DIRS & set(p.relative_to(ROOT).parts)
    ]
    return sorted(playgrounds, key=lambda p: p.relative_to(ROOT).as_posix())


def main():
    playgrounds = find_playgrounds()

    if not playgrounds:
        print("No playground.py files found.")
        sys.exit(1)

    while True:
        print("\nAvailable playgrounds:")
        for i, p in enumerate(playgrounds, start=1):
            label = p.parent.name
            print(f"  {i}. {label}")
        print(f"  {len(playgrounds) + 1}. EXIT")

        choice = input("\nSelect a playground to run: ").strip()

        if choice == str(len(playgrounds) + 1) or choice.lower() == "exit":
            return

        try:
            index = int(choice) - 1
            if index < 0:
                raise ValueError
            target = playgrounds[index]
        except (ValueError, IndexError):
            print("Invalid choice, try again.")
            continue

        print(f"\nRunning {target.parent.relative_to(ROOT).as_posix()}/playground.py ...\n")
        # Run from the playground's own directory so its relative sys.path
        # setup (walking up to find `lists`, etc.) resolves the same way it
        # would if you had cd'd there and run it directly.
        subprocess.run([sys.executable, target.name], cwd=target.parent)


if __name__ == "__main__":
    main()
