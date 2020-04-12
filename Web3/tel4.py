class PhoneError(Exception):
    pass


class CodePhoneError(PhoneError):
    pass


def get_tel_number():
    tel = input()
    # tel = '5160940487'
    # # # tel =  '+3599399672905'

    try:
        tel = tel_clear(tel)
        if tel[:1] == '8':
            tel = '+7' + tel[1:]
        if tel[:1] != '+':
            raise NameError

        kod = valid_kode(tel)
        if len(tel[1:]) == 11:
            if kod == '+7':
                tel_operator(tel[len(kod):3 + len(kod)])
            print(tel)
        else:
            raise IndexError
    except ValueError:
        print('не определяется оператор сотовой связи')
    except NameError:
        print('неверный формат')
    except IndexError:
        print('неверное количество цифр')
    except ZeroDivisionError as e:
        print('Поделили на 0')
    except Exception as e:
        print(e)
    # finally:
    #     print('Идем дальше')


def tel_operator(phone_number):
    mts = [str(i) for i in range(910, 919)]
    mts1 = [str(i) for i in range(980, 990)]
    mts = mts + mts1
    meg = [str(i) for i in range(920, 940)]
    bil = [str(i) for i in range(902, 907)]
    bil1 = [str(i) for i in range(960, 970)]
    bil = bil + bil1
    sot = mts + meg + bil
    if phone_number in sot:
        pass
    else:
        raise ValueError
    pass


def tel_kod(phone_number):
    pass


def clear_simv(phone_number):
    c = ['(', ')', '-']
    for i in c:
        phone_number = phone_number.strip().replace(i, "")
    if phone_number[2:].isdigit():
        return phone_number
    else:
        raise NameError


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
                raise NameError
    if len(stack) == 0 and bracket == 1:
        return True
    else:
        raise NameError


def valid_kode(phone_number):
    spis_kod = ['+359', '+7', '8', '+55', '+1']
    kod_valid = False
    for i in spis_kod:
        if phone_number.startswith(i):
            kod = i
            kod_valid = True
    if kod_valid:
        return kod
    else:
        raise CodePhoneError('не определяется код страны')


def tel_clear(phone_number):
    phone_number = phone_number.strip().replace(' ', '')
    phone_number = phone_number.strip().replace('\t', '')
    if phone_number.find('--') == -1:
        if phone_number.find(')') != -1 or phone_number.find('(') != -1:
            if check(phone_number):

                return clear_simv(phone_number)
            else:
                print('error')
        else:
            return clear_simv(phone_number)
    else:
        raise NameError


def validNumber(phone_number):
    for i, c in enumerate(phone_number):
        if i in [3, 7]:
            if c != '-':
                return False
        elif not c.isalnum():
            return False
    return True


get_tel_number()
