# fetch_python_docs.py

A Python script to idempotently download, extract, and locally serve a mirror of
[docs.python.org](https://docs.python.org/).

## Installation and usage

The script has minimal dependencies (`requests` and `send2trash`), so in most
environments (e.g. Ubuntu) you can just run the script in your shell:

```shell
sudo apt install python3-requests python3-send2trash  # if needed
./fetch_python_docs.py --systemd
```

This downloads the docs to within the git repository, then defines, starts, and
enables a systemd user service. You can browse the docs by going to
`localhost:8004` in a web browser.

To skip the systemd integration and just download the docs, use the following
command instead:

```shell
./fetch_python_docs.py
```

The docs are downloaded to within the git repository and you can open
`/python-3.xx-docs-html/index.html` manually.

To reverse installation, use the `--clean` flag:

```shell
./fetch_python_docs.py --clean
```

## Why not just use `pydoc -b`?

The color scheme.
