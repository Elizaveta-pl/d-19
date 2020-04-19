import argparse

parser = argparse.ArgumentParser()
parser.add_argument('source', nargs='?', default='', type=str)
parser.add_argument('destination', nargs='?', default='', type=str)
parser.add_argument('--lines', nargs=1, default=[0], type=int)
parser.add_argument('--upper', action="store_true")
args = parser.parse_args()


def f_src(src_file):
    f_src = open(src_file, encoding="utf8")
    dst_file = args.destination
    d_file = open(dst_file, 'w', encoding="utf8")
    text = [i for i in f_src]

    if args.lines[0] == 0:
        line = len(text)
    elif len(text) <= args.lines[0]:
        line = len(text)
    else:
        line = args.lines[0]

    for i in range(line):
        if (args.upper):
            d_file.write(text[i].upper())
        else:
            d_file.write(text[i])
    # if len(text) == 0:
    #     d_file.write('\n')

    f_src.close()
    d_file.close()


def f_dst(dst_file):
    d_file = open(dst_file, 'w', encoding="utf8")
    return d_file


if args.source != '':
    f_src(args.source)
