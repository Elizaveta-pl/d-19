import argparse

parser = argparse.ArgumentParser()
parser.add_argument('source', nargs='?', default='', type=str)
parser.add_argument('--count', action="store_true")
parser.add_argument('--num', action="store_true")
parser.add_argument('--sort', action="store_true")

args = parser.parse_args()


def sum_arg(summ1, summ2):
    print(int(summ1) + int(summ2))


def m_cat(src_file):
    try:
        f_src = open(src_file, encoding="utf8")
        text = [i.rstrip() for i in f_src]
        if (args.sort):
            text = sorted(text)
        j = 0
        for i in text:
            if (args.num):
                print(f'{j} {i}')
                j += 1
            else:
                print(f'{i}')
        if (args.count):
            print(f'rows count: {len(text)}')
        f_src.close()
    except ValueError:
        print('ValueError')
    except IndexError:
        print('ERROR')
    except FileNotFoundError:
        print('ERROR')


def print_error(message):
    if __name__ == "__main__":
        print('Welcome to my program')
    print(f'ERROR: {message}!!')


def main():
    # print(f'args.arg[0] = {args.arg[0]}')
    # print("Main part of my_module.py")
    # print(f'args.summ1 = {args.summ}')
    if args.source != '':
        m_cat(args.source)


if __name__ == "__main__":
    main()
