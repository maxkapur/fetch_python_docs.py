#!/usr/bin/env python
"""Idempotently download, extract, and serve a mirror of <docs.python.org>."""

import argparse
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

HERE = Path(__file__).parent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Idempotently download/serve Python docs from a local copy"
    )
    parser.add_argument("--serve", action="store_true")
    parsed = parser.parse_args()

    major, minor, *_ = sys.version_info
    url = f"https://docs.python.org/3/archives/python-{major}.{minor}-docs-html.tar.bz2"
    outfile = HERE / f"python-{major}.{minor}-docs-html.tar.bz2"

    print(f"Downloading {url}")
    if outfile.is_file():
        print(f"{outfile} already exists")
    else:
        # -s: silent mode
        # -S: but show errors
        # -L: follow redirect
        # -f: fail fast on HTTP error
        subprocess.run(["curl", "-sSLf", url, "--output", outfile], cwd=HERE).check_returncode()

    print(f"Extracting {outfile}")
    outdir = HERE / f"python-{major}.{minor}-docs-html"
    if (outdir / "index.html").is_file():
        print(f"{outdir}/index.html already exists")
    else:
        subprocess.run(["tar", "vxf", outfile], cwd=HERE).check_returncode()

    if parsed.serve:
        # Use a different port from 8000 to avoid conflicting with other
        # instances of http.server
        server = subprocess.Popen(
            [sys.executable, "-m", "http.server", "-d", outdir, "8004"]
        )
        time.sleep(0.5)
        webbrowser.open("http://localhost:8004")

        try:
            server.wait()
        except KeyboardInterrupt:
            server.terminate()
