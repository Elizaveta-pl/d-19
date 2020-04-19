import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', metavar='arg', default='', nargs='*', type=str)
args = parser.parse_args()


def print_error(message):
    if __name__ == "__main__":
        print('Welcome to my program')
    print(f'ERROR: {message}!!')


def main():
    # print(f'args.arg[0] = {args.arg[0]}')
    # print("Main part of my_module.py")
    print_error(args.arg[0])


if __name__ == "__main__":
    main()
