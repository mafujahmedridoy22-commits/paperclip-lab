import unittest

from slugify import slugify


class SlugifyTests(unittest.TestCase):
    def test_lowercases(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_spaces_become_a_single_hyphen(self):
        self.assertEqual(slugify("a  b   c"), "a-b-c")

    def test_punctuation_is_collapsed(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_underscores_are_treated_as_separators(self):
        self.assertEqual(slugify("snake_case_text"), "snake-case-text")

    def test_consecutive_separators_become_one_hyphen(self):
        self.assertEqual(slugify("foo__--bar"), "foo-bar")

    def test_strips_accents(self):
        self.assertEqual(slugify("Café déjà vu"), "cafe-deja-vu")

    def test_unicode_letters_are_preserved(self):
        self.assertEqual(slugify("日本語 テスト"), "日本語-テスト")

    def test_trims_leading_and_trailing_hyphens(self):
        self.assertEqual(slugify("  --foo bar--  "), "foo-bar")

    def test_whitespace_other_than_spaces(self):
        self.assertEqual(slugify("a\tb\nc"), "a-b-c")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()
