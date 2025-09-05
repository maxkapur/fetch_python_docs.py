# fetch_python_docs.py

A Python script to idempotently download, extract, and locally serve a mirror of
[docs.python.org](https://docs.python.org/).

## Installation and usage

The script uses only the standard library and `requests`, so in most
environments (e.g. Ubuntu) you can just run the script in your shell:

```
# Just download/extract docs
./fetch_python_docs.py
# Also define a systemd user service
./fetch_python_docs.py --systemd
```

The docs are downloaded to within the git repository. You can either open the
files manually, or by running `systemctl --user start python-docs` and opening
`localhost:8004` in a browser.

## Why not just use `pydoc -b`?

The color scheme.
