import sys


def sorted_dict_val(dict):
    rev = False
    # sorted_by_val = sorted(dict.items(), key=lambda kv: kv[1], reverse=rev)
    sorted_dict_by_val = {i[0]: i[1] for i in sorted(dict.items(), key=lambda kv: kv[1], reverse=rev)}
    return sorted_dict_by_val


def sorted_dict_key(dict):
    rev = False
    sorted_by_key = {k: dict[k] for k in sorted(dict.keys(), reverse=rev)}
    return sorted_by_key


try:
    t = {sys.argv[i].split('=')[0]: sys.argv[i].split('=')[1] for i in
         range(len(sys.argv)) if sys.argv[i].find('=') != -1}
    # if sys.argv[1] == '--sort':
    if '--sort' in sys.argv:
        for key, val in sorted_dict_key(t).items():
            print(f'Key: {key} Value: {val}')
    else:
        for key, val in t.items():
            print(f'Key: {key} Value: {val}')

except ValueError:
    print('ValueError')
except IndexError:
    print('NO PARAMS')
