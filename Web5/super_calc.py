import argparse

parser = argparse.ArgumentParser()
parser.add_argument('summ', metavar='summ', nargs='*', type=str)

args = parser.parse_args()


def sum_arg(summ1, summ2):
    try:
        print(int(summ1) + int(summ2))
    except ValueError:
        print('ValueError')


def print_error(message):
    if __name__ == "__main__":
        print('Welcome to my program')
    print(f'ERROR: {message}!!')


def main():
    # print(f'args.arg[0] = {args.arg[0]}')
    # print("Main part of my_module.py")
    # print(f'args.summ1 = {args.summ}')
    if len(args.summ) == 0:
        print('NO PARAMS')
    elif len(args.summ) == 1:
        print('TOO FEW PARAMS')
    elif len(args.summ) == 2:

        sum_arg(args.summ[0], args.summ[1])
    else:
        print('TOO MUCH PARAMS')


if __name__ == "__main__":
    main()
