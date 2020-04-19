import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--per-day', metavar='PER_DAY', nargs=1, default=[0], type=int)
parser.add_argument('--per-week', metavar='PER_WEEK', nargs=1, default=[0], type=int)
parser.add_argument('--per-month', metavar='PER_MONTH', nargs=1, default=[0], type=int)
parser.add_argument('--per-year', metavar='PER_YEAR', nargs=1, default=[0], type=int)
parser.add_argument('--get-by', choices=['day', 'month', 'year'], default='day', type=str)

args = parser.parse_args()

if args.get_by == 'day':
    day = 1
elif args.get_by == 'month':
    day = 30
elif args.get_by == 'year':
    day = 360

boy = int((args.per_day[0] + args.per_week[0] / 7 + args.per_month[0] / 30
           + args.per_year[0] / 360) * day)

print(f'{boy}')
