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
        e.g. /tmp/farsdbfs/1975/DBF/FARS1975.zip/PERSON.dbf
        or   /tmp/farsdbfs/2000/Auxiliary_FARS_Files/Auxiliary_PR_DBF_2000.ZIP/RICO/RICO/VEH_AUX.dbf

    Returns: dict;
        e.g.

        /tmp/farsdbfs/1975/DBF/FARS1975.zip/PERSON.dbf
        {'year': 1975, 'type': 'person', 'scope': 'main', 'region': 'national',
         'subtype': None}


        /tmp/farsdbfs/2000/Auxiliary_FARS_Files/Auxiliary_PR_DBF_2000.ZIP/RICO/RICO/VEH_AUX.dbf
        {'year': 2000, 'type': 'vehicle',  'scope': 'auxiliary', 'region': 'puerto-rico',
         'subtype': None}

        /tmp/farsdbfs/2012/National/DBF/FARS2012.zip/miacc.dbf
        {'year': 2012, 'type': 'accident',  'scope': 'main', 'region': 'national',
         'subtype': 'alcohol-multiple-imputation'}

        /tmp/farsdbfs/2012/Puerto Rico/PuertoRico2012DBF.zip/midrvacc.dbf
        {'year': 2012, 'type': 'driver-accident',  'scope': 'main', 'region': 'puerto-rico',
         'subtype': 'alcohol-multiple-imputation'}

    """
    pathstr = str(filepath)
    pathparts = Path(filepath).parts
    d = {}
    d['year'] = next(p for p in pathparts if re.match(r'\d{4}', p))
    d['region'] = 'puerto-rico' if PUERTORICO_PATTERN.match(pathstr) else 'national'
    return d
