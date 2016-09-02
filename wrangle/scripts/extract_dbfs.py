"""
Recursively finds *.zip files (with DBF in their path name) in `srcdir`
    and extracts DBF files to `destdir`
"""

import argparse
from loggy import loggy
from pathlib import Path
import re
from sys import stdout
from zipfile import ZipFile

ZIPF_PATTERN = re.compile(r'dbf.*?\.zip', re.IGNORECASE)


LOGGY = loggy('extract_dbfs')


if __name__ == '__main__':
    parser = argparse.ArgumentParser("This does something")
    parser.add_argument('srcdir', type=str, help="a directory in which ZIP files are found")
    parser.add_argument('destdir', type=str, help="a directory to which DBF files are extracted")
    args = parser.parse_args()
    srcpath = Path(args.srcdir)
    destpath = Path(args.destdir)
    if not destpath.exists() or not srcpath.exists():
        raise IOError("Both srcdir, %s, and destdir, %s, must be valid directories" % (srcpath, destpath))

    zippaths = [fname for fname in list(srcpath.rglob('*')) if ZIPF_PATTERN.search(str(fname))]
    LOGGY.info("%s ZIP files found with DBF in the pathname" % len(zippaths))
    for fpath in zippaths:
        fstrpath = str(fpath)
        # extract the filename starting from the year subdirectory
        # e.g 1987/DBF/FARS1987.zip
        #   from wrangle/corral/fetched/fars/1987/DBF/FARS1987.zip
        destsubdir = Path(re.search('\d{4}/.+', fstrpath).group())

        LOGGY.info("Unzipping: %s" % fstrpath)
        with ZipFile(fstrpath) as zfile:
            for af in zfile.filelist:
                LOGGY.info("\tExtracting: %s" % af.filename)
                apath = destsubdir.joinpath(af.filename)
                adir = apath.parent
                adir.mkdir(parents=True, exist_ok=True)
                LOGGY.info("\t\tinto: %s (%s MB)" % (apath, round(af.file_size / 1000000, 1)))
                zfile.extract(af, path=str(adir))

