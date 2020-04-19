import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', metavar='barbie', nargs='*', default=[50], type=int)
parser.add_argument('--cars', metavar='cars', nargs='*', default=[50], type=int)
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], metavar='movie',
                    nargs='*', default=['other'], type=str)

args = parser.parse_args()

if args.movie[0] == 'melodrama':
    movie = 0
elif args.movie[0] == 'football':
    movie = 100
elif args.movie[0] == 'other':
    movie = 50

if 0 <= args.barbie[0] <= 100:
    barbie = args.barbie[0]
else:
    barbie = 50

if 0 <= args.cars[0] <= 100:
    cars = args.cars[0]
else:
    cars = 50

boy = int((100 - barbie + cars + movie) / 3)
girl = 100 - int(boy)

print(f'boy: {boy}')
print(f'girl: {girl}')
