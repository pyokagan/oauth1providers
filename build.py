#! /usr/bin/python3
import yaml
from argparse import ArgumentParser
from os.path import splitext, basename
import json
import sys

def main():
    p = ArgumentParser()
    p.add_argument("files", nargs="+")
    args = p.parse_args()
    out = dict()
    for path in args.files:
        name = splitext(basename(path))[0]
        f = open(path, "r")
        out[name] = yaml.load(f)
        f.close()
    json.dump(out, sys.stdout)
if __name__ == "__main__":
    main()

