import argparse
from loggy import loggy
from sys import stdout

myloggy = loggy('loggy')


if __name__ == '__main__':
    parser = argparse.ArgumentParser("This does something")
#    parser.add_argument('infile', type=argparse.FileType('r'))
#    parser.add_argument('--someval', type=int, help="")
    myloggy.info("This is a log message")
    stdout.write("This is goodbye")
