# foundry/whoami.py
"""Report which interpreter is running this file, and which environment it is standing in.

Nothing here is about Foundry. It is about the machine: every fact below is read out of the
running interpreter itself, so the answer cannot be a setting someone believes.
"""

import sys


def report() -> dict[str, str]:
    """The four facts that identify a running Python, read from the interpreter, not from PATH."""
    return {
        "version": sys.version.split()[0],
        "executable": sys.executable,
        "prefix": sys.prefix,
        "in_venv": str(sys.prefix != sys.base_prefix),
    }


def main() -> None:
    for name, value in report().items():
        print(f"{name:<11}{value}")


if __name__ == "__main__":
    main()
