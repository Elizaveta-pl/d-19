import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('arg', metavar='arg', nargs='*', default='no args',
                    type=str)
args = parser.parse_args()

if isinstance(args.arg, str):
    print(args.arg)
else:
    for i in args.arg:
        print(i)

