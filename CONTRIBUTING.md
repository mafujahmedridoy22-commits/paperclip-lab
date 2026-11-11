# Contributing

Thanks for contributing to paperclip-lab. This repo is a sandbox for the
Paperclip agent pipeline, so keep changes small, focused, and testable.

## Branch and PR workflow

- Never push directly to `main`. It is protected and accepts changes only
  through pull requests.
- Branch off `main` for every change, e.g. `fix/<issue>-<short-slug>`.
- Keep one logical change per branch and per PR.
- Use Conventional Commits for the commit message (e.g. `feat: ...`,
  `fix: ...`, `docs: ...`).
- Open the PR against `main`. The required `test` check must pass before the
  PR can be merged.

## Running tests locally

Run the same checks the CI workflow runs.

Python tests:

```sh
python -m unittest discover -v
```

Node tests (when a `package.json` is present):

```sh
npm test
```

There is no need to run anything for documentation-only changes.
