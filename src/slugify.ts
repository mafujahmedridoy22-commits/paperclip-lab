/**
 * String slugification helpers.
 *
 * Mirrors the behaviour of the Python `slugify` helper in `slugify.py`:
 * lowercases the input, strips diacritics, collapses runs of
 * non-alphanumeric characters into a single hyphen, and trims any
 * leading or trailing hyphens.
 */

const NON_ALPHANUMERIC = /[^\p{L}\p{N}]+/gu;

export function slugify(text: string): string {
  const decomposed = text.normalize("NFKD");
  const stripped = decomposed.replace(/\p{M}/gu, "");
  return stripped.toLowerCase().replace(NON_ALPHANUMERIC, "-").replace(/^-+|-+$/g, "");
}
