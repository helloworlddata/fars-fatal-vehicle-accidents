from dbfread import DBF
from pathlib import Path
import re


PUERTORICO_PATTERN = re.compile(r'Puerto|Rico|PR(?![A-z])', re.IGNORECASE)



def dbf_to_dict(filepath):
    """
    filepath: str or Path; name of DBF file
    Returns: list; a list of OrderedDicts

    Assumes your system can hold everything in memory while doing a DBF to list of dicts
     because screw it, this is taking too long to write
    """
    return list(DBF(str(filepath)))


def derive_file_meta(filepath):
    """
    filepath: str or Path; name of file (presumably, a DBF),
        e.g. 1975/DBF/FARS1975.zip
        or   1992/Auxiliary_FARS_Files/Auxiliary_FARS_DBF_1992.ZIP
        or   2015/Puerto\ Rico/FARS2015PuertoRicoDBF.zip

    Returns: dict; e.g. {'year': 1992, 'region': 'national'}
                        {'year': 2015, 'region': 'puerto-rico'}
    """
    pathstr = str(filepath)
    pathparts = Path(filepath).parts
    d = {}
    d['year'] = next(p for p in pathparts if re.match(r'\d{4}', p))
    d['region'] = 'puerto-rico' if PUERTORICO_PATTERN.match(pathstr) else 'national'
    return d
