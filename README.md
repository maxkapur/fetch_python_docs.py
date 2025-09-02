# fetch_python_docs.py

A Python script to idempotently download, extract, and locally serve a mirror of
[docs.python.org](https://docs.python.org/).

## Installation and usage

The script uses only the standard library and `requests`, so in most
environments (e.g. Ubuntu) you can just run the script in your shell:

```
./fetch_python_docs.py --serve
```

Omit `--serve` to only download and extract.

## Why not just use `pydoc -b`?

The color scheme.
