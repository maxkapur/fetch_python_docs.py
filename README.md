# fetch_python_docs.py

A Python script to idempotently download, extract, and locally serve a mirror of
[docs.python.org](https://docs.python.org/).

## Installation and usage

The script uses only the standard library and `requests`, so in most
environments (e.g. Ubuntu) you can just run the script in your shell:

```
# Open docs in web browser
./fetch_python_docs.py --open
# Start the web server but don't open anything
./fetch_python_docs.py --serve
# Just downlaod/extract docs
./fetch_python_docs.py
```

## Why not just use `pydoc -b`?

The color scheme.
