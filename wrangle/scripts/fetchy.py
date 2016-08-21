import argparse
from loggy import loggy
import requests
from sys import stdout


LOGGY = loggy('fetch_data')

SRC_URLS = {
    'key1': 'http://example.com/1',
    'key2': 'http://example.com/2',
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Downloads data from example.com")
    parser.add_argument('somekey', type=str, help="SOMEKEY to download from: %s" % ','.join(SRC_URLS.keys()))
    args = parser.parse_args()
    if args.somekey not in SRC_URLS.keys():
        raise IOError("Year argument must be: %s" % ', '.join(SRC_URLS.keys()))

    url = SRC_URLS[args.somekey]
    LOGGY.info("Downloading: %s" % url)

    resp = requests.get(url, stream=True)
    for chunk in resp.iter_content(chunk_size=1024):
        if chunk:
            stdout.write(chunk)
