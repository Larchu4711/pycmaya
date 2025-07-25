"""pycmaya module providing a simple datetime formatter using maya."""

from __future__ import annotations

import maya

__all__ = ["__version__", "format_now"]
__version__ = "0.1.0"

def format_now() -> str:
    """Return the current time in RFC 3339 format using ``maya``.

    Returns
    -------
    str
        Current time as RFC 3339 formatted string.
    """
    return maya.now().rfc3339()
