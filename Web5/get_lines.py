import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', metavar='barbie', default=[0], nargs=1, type=str)
args = parser.parse_args()


def some_func():
    print("func is running")
    if __name__ == "__main__":
        print("I was called without ##import##")


def count_lines(path_file):
    if path_file == 0:
        return 0
    else:
        try:
            f = open(path_file, encoding="utf8")
            text = [i.rstrip() for i in f]
            return len(text)
            f.close()
        except FileNotFoundError:
            return 0


def main():
    print(count_lines(args.file[0]))


if __name__ == "__main__":
    main()
