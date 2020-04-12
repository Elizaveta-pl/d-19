def get_tel_number():
    # tel = input()
    tel = '8--04635(22)r	9'

    try:
        tel = tel_clear(tel)
        if tel.find(')') != -1 or tel.find('(') != -1:
            if check(tel):
                print(clear_simv(tel))
            else:
                print('error')
        else:
            print(clear_simv(tel))
    except ValueError:
        print('error')
    except IndexError:
        print('Мы за границей списка')
    except ZeroDivisionError as e:
        print('Поделили на 0')
    except Exception as e:
        print('Непредвиденная ошибка %s' % e)
    # finally:
    #     print('Идем дальше')


def clear_simv(phone_number):
    c = ['(', ')', '-']
    for i in c:
        phone_number = phone_number.strip().replace(i, "")
    if phone_number[1:].isalnum():
        if len(phone_number[1:]) == 11:
            return phone_number
        else:
            raise ValueError
    else:
        raise ValueError


# Функция для проверки скобок
def check(phone_number):
    bracket = phone_number.count('(')
    stack = []
    for i in phone_number:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if (len(stack) > 0):
                stack.pop()
            else:
                raise ValueError
    if len(stack) == 0 and bracket == 1:
        return True
    else:
        raise ValueError


def tel_clear(phone_number):
    spis = ['+7', '8']
    phone_number = phone_number.strip().replace(' ', '')
    phone_number = phone_number.strip().replace('\t', '')
    if phone_number[:1] in spis or phone_number[:2] in spis:
        if phone_number[-1].isdigit() and (phone_number.find('--') == -1):
            if phone_number[:1] == '8':
                return '+7' + phone_number[1:]
            else:
                return phone_number
        else:
            raise ValueError
    else:
        raise ValueError


def validNumber(phone_number):
    for i, c in enumerate(phone_number):
        if i in [3, 7]:
            if c != '-':
                return False
        elif not c.isalnum():
            return False
    return True


get_tel_number()
