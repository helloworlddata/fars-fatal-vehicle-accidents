"""
Recursively finds *.dbf files in `srcdir` and extracts CSVs to `destdir`
"""

import argparse
from loggy import loggy
from pathlib import Path
import re
from sys import stdout

from utils import derive_file_meta, dbf_to_dict

DBF_PATTERN = re.compile(r'\.dbf', re.IGNORECASE)

LOGGY = loggy('extract_csvs')


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Converts DBF files found in `srcdir` into CSVs, saved into `destdir`")
    parser.add_argument('srcdir', type=str, help="a directory in which DBF files are found")
    parser.add_argument('destdir', type=str, help="a directory to which CSV files are extracted")
    args = parser.parse_args()
    srcpath = Path(args.srcdir)
    destpath = Path(args.destdir)
    if not destpath.exists() or not srcpath.exists():
        raise IOError("Both srcdir, %s, and destdir, %s, must be valid directories" % (srcpath, destpath))

    dbfpaths = [fname for fname in list(srcpath.rglob('*')) if DBF_PATTERN.search(str(fname))]
    LOGGY.info("%s DBF files found" % len(dbfpaths))
    for dpath in dbfpaths:
        LOGGY.info(dpath)
