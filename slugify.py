"""String slugification helpers."""

import re
import unicodedata

_NON_ALPHANUMERIC = re.compile(r"[\W_]+")


def slugify(text: str) -> str:
    """Convert *text* into a URL-friendly slug.

    Lowercases the input, strips diacritics, collapses runs of
    non-alphanumeric characters into a single hyphen, and trims any
    leading or trailing hyphens.
    """
    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return _NON_ALPHANUMERIC.sub("-", stripped.lower()).strip("-")
