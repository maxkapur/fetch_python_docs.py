#!/usr/bin/env python
"""Idempotently download, extract, and serve a mirror of <docs.python.org>."""

import argparse
import http.client
import subprocess
import sys
import tarfile
import time
import webbrowser
from pathlib import Path

import requests

HERE = Path(__file__).parent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Idempotently download/serve Python docs from a local copy"
    )
    parser.add_argument("--serve", action="store_true")
    parsed = parser.parse_args()

    major, minor, *_ = sys.version_info
    url = f"https://docs.python.org/{major}.{minor}/archives/python-{major}.{minor}-docs-html.tar.bz2"
    outfile = HERE / f"python-{major}.{minor}-docs-html.tar.bz2"

    print(f"Downloading {url}")
    if outfile.is_file():
        print(f"{outfile} already exists")
    else:
        with requests.get(url) as r, open(outfile, "wb") as f:
            if r.status_code != 200:
                descr = http.client.responses[r.status_code]
                raise RuntimeError(f"{r.status_code = } ({descr})")
            f.write(r.content)
            print(f"Saved to {outfile} ({len(r.content)} bytes)")

    print(f"Extracting {outfile}")
    assert outfile.is_file()
    outdir = HERE / f"python-{major}.{minor}-docs-html"
    if (outdir / "index.html").is_file():
        print(f"{outdir}/index.html already exists")
    else:
        with tarfile.open(outfile) as f:
            f.extractall(path=HERE, filter="data")  # Extracting HERE creates outdir
        assert (outdir / "index.html").is_file()

    if parsed.serve:
        # Use a different port from 8000 to avoid conflicting with other
        # instances of http.server
        server = subprocess.Popen(
            [sys.executable, "-m", "http.server", "-d", outdir.absolute(), "8004"]
        )
        time.sleep(0.5)
        webbrowser.open("http://localhost:8004")

        try:
            server.wait()
        except KeyboardInterrupt:
            server.terminate()
