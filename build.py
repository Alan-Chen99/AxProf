import subprocess
from pathlib import Path


def build():
    subprocess.run(
        ["make"], cwd=Path(__file__).parent / "axprof" / "checkerGen", check=True
    )


if __name__ == "__main__":
    build()
