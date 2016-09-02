# FARS data


Homepage http://www.nhtsa.gov/FARS

Documentation listing https://crashstats.nhtsa.dot.gov/#/DocumentTypeList/4


FTP: ftp://ftp.nhtsa.dot.gov/fars/


# Working with a mirror

The FARS data is scattered across the [NHTSA FTP server](ftp://ftp.nhtsa.dot.gov/fars/). Rather than write a script just to walk the directory structure, I just ran __wget__ on it, and made a separate repo which contains more or less an exact mirror of [ftp.nhtsa.dot.gov/fars](ftp://ftp.nhtsa.dot.gov/fars/).

This repo is part of my wgetsnaps organization: https://github.com/wgetsnaps/ftp.nhtsa.dot.gov--fars
