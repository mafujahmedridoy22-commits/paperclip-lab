import { test } from "node:test";
import assert from "node:assert/strict";
import { slugify } from "./slugify.ts";

test("lowercases", () => {
  assert.equal(slugify("Hello World"), "hello-world");
});

test("spaces become a single hyphen", () => {
  assert.equal(slugify("a  b   c"), "a-b-c");
});

test("punctuation is collapsed", () => {
  assert.equal(slugify("Hello, World!"), "hello-world");
});

test("underscores are treated as separators", () => {
  assert.equal(slugify("snake_case_text"), "snake-case-text");
});

test("consecutive separators become one hyphen", () => {
  assert.equal(slugify("foo__--bar"), "foo-bar");
});

test("strips accents", () => {
  assert.equal(slugify("Café déjà vu"), "cafe-deja-vu");
});

test("unicode letters are preserved", () => {
  assert.equal(slugify("日本語 テスト"), "日本語-テスト");
});

test("trims leading and trailing hyphens", () => {
  assert.equal(slugify("  --foo bar--  "), "foo-bar");
});

test("whitespace other than spaces", () => {
  assert.equal(slugify("a\tb\nc"), "a-b-c");
});

test("empty string", () => {
  assert.equal(slugify(""), "");
});
