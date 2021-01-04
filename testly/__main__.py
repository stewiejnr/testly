import sys, getopt
import os
from testly import __version__

def main(argv):
    print("Copyright \N{COPYRIGHT SIGN} 2021 Stewartium, RPhipps ::: testly v{}\n".format(__version__))
    return sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])    