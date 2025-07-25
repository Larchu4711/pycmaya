"""Command line interface for pycmaya."""

from __future__ import annotations

from . import format_now


def main() -> None:
    """Entry point for the ``pycmaya`` command."""
    print(format_now())


if __name__ == "__main__":  # pragma: no cover - executed only when called directly
    main()
