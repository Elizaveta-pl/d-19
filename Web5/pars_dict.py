import argparse

parser = argparse.ArgumentParser()
parser.add_argument('source', nargs='*', default='', type=str)
parser.add_argument('--sort', action="store_true")

args = parser.parse_args()


def sum_arg(summ1, summ2):
    print(int(summ1) + int(summ2))


def sorted_dict_key(dict):
    rev = False
    sorted_by_key = {k: dict[k] for k in sorted(dict.keys(), reverse=rev)}
    return sorted_by_key


def dict(sousce):
    try:
        t = {args.source[i].split('=')[0]: args.source[i].split('=')[1] for i in
             range(len(args.source)) if args.source[i].find('=') != -1}
        max_val = len(max(t.keys())) + 2
        # final_dict = {k: v for k, v in key.items() if v == max_val}
        # print(final_dict)
        if (args.sort):
            for key, val in sorted_dict_key(t).items():
                print(f'Key: {key.ljust(max_val, " ")} Value: {val}')
        else:
            for key, val in t.items():
                print(f'Key: {key.ljust(max_val, " ")} Value: {val}')

    except ValueError:
        print('ValueError')
    except IndexError:
        print('NO PARAMS')


def print_error(message):
    if __name__ == "__main__":
        print('Welcome to my program')
    print(f'ERROR: {message}!!')


def main():
    # print(f'args.arg[0] = {args.arg[0]}')
    # print("Main part of my_module.py")
    # print(f'args.summ1 = {args.summ}')
    if args.source != '':
        dict(args.source)


if __name__ == "__main__":
    main()
