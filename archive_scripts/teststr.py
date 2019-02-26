#!/usr/bin/python
import argparse

def printstuff():
    with open(args.file, "w") as f:
        f.write("Hello World")
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    printstuff()