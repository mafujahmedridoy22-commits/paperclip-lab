# paperclip-lab

Sandbox repo for the Paperclip agent pipeline:

- **GFI Scout** finds labelled issues worth doing.
- **GFI Builder** implements one issue on a branch and opens a PR.
- **GFI Reviewer** reviews the diff, checks CI, and merges on green.

Work lands on `main` only through pull requests with a passing `test` check.
Python and TypeScript are both welcome; CI runs whatever tests exist.
