# fetch_python_docs.py

A Python script to idempotently download, extract, and locally serve a mirror of
[docs.python.org](https://docs.python.org/).

**Installation/usage:** It only uses the standard library, so you can just run
`./fetch_python_docs.py --serve` in your shell, or omit `--serve` to only
download.

**Platforms?** Assumes Linux with `curl` and `tar` available for now.

**Why not use `pydoc -b`?** The color scheme.
