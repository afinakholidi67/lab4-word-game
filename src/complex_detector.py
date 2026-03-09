"""Utility to detect complex numbers.

Provides `is_complex(value, require_imag=True)` which returns True when
`value` is a complex number or a string representing a complex number.

By default `require_imag=True` so the function returns True only when the
imaginary part is non-zero. Set `require_imag=False` to accept pure real
values (e.g. "3" or 3.0) as valid.
"""

from typing import Any

__all__ = ["is_complex"]


def is_complex(value: Any, require_imag: bool = True) -> bool:
    """Return True if ``value`` is or represents a complex number.

    Args:
        value: A Python value (complex, number, or string) to test.
        require_imag: If True, only consider values with a non-zero
            imaginary part as complex.

    Examples:
        >>> is_complex(3+4j)
        True
        >>> is_complex("3+4j")
        True
        >>> is_complex("3")
        False
        >>> is_complex("3", require_imag=False)
        True
    """
    # Native complex type
    if isinstance(value, complex):
        return (value.imag != 0) if require_imag else True

    # Plain numbers: treat as complex only when imaginary part is allowed
    if isinstance(value, (int, float)):
        return False if require_imag else True

    # Strings: try to parse with built-in `complex()` after trimming
    if isinstance(value, str):
        s = value.strip()
        if not s:
            return False
        # Allow parentheses around the literal like "(3+4j)"
        if s.startswith("(") and s.endswith(")"):
            s = s[1:-1].strip()

        # Quick reject: if we require an imaginary part but there's no 'j'
        if require_imag and ("j" not in s and "J" not in s):
            return False

        try:
            c = complex(s)
        except (ValueError, TypeError):
            return False

        return (c.imag != 0) if require_imag else True

    # Other types (lists, dicts, etc.) are not considered complex
    return False
