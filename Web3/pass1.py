class PasswordError(Exception):
    pass
    # print('error-PasswordError')


class LengthError(PasswordError):
    pass
    #  print('error-LengthError')


class LetterError(PasswordError):
    pass
    #     print('error-LetterError')


class DigitError(PasswordError):
    pass
    #    print('error-DigitError')


class SequenceError(PasswordError):
    pass
    #    print('error-SequenceError')


def check_password():
    # pas = input()

    # pas = 'aaaDadsRTYweerfeg12'
    pas = 'asfdaaaaaaaaaaaA1'
    # pas = 'GБвИНddифпГxFGH1'

    # result = [int(item) for item in pas]
    ch = {'dig': False}
    try:
        pass_status = False

        if Length_pass(pas):
            pass_status = True
            # print(pas.lower())
        else:
            raise LengthError

        if Letter_pass(pas) and pass_status:
            pass_status = True
        else:
            raise LetterError

        if Digit_pass(pas) and pass_status:
            # print("Digit_pass")
            pass_status = True
        else:
            raise DigitError

        if Sequence_pass(pas) and pass_status:
            pass_status = True
            # print("Sequence_pass")
        else:
            raise LetterError

        if pass_status:
            print('ok')
        else:
            print('error')

    except ValueError:
        print('error')

    except LengthError:
        print('error-Length')
    except LetterError:
        print('error-Letter')
    except DigitError:
        print('error-Digit')
    except SequenceError:
        print('error-Sequence')


def check_num(pas):
    # print(pas)
    if pas.isdigit():
        return True
    else:
        return False


def Length_pass(pas):
    # try:
    if len(pas) > 8:
        # pass_status = True
        return True
    else:
        raise LengthError
    #
    # except LengthError:
    #     print('error-Length')


def Letter_pass(pas):
    # try:
    if (pas.islower() or pas.isupper()):
        raise LetterError
    else:
        # pass_status = True
        # print(pass_status)
        return True

    # except LetterError:
    #     print('error-Letter')


def Digit_pass(pas):
    # try:
    digit_status = False
    for i in list(pas):
        # print(i)

        if check_num(i):
            digit_status = True
            # ch.update({'dig': True})

    if digit_status:
        return True
    else:
        raise DigitError


def Sequence_pass(pas):
    sequence_status = True
    keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']

    # try:
    for i in range(len(keyboard)):
        # print(keyboard_lat_1[i])
        for j in range(len(keyboard[i])):
            # print(keyboard_lat_1[i][j])
            # print(f' j = {j}   {keyboard[i][j:j+3]}')
            # print(f' j = {j}')
            if len(keyboard[i][j:j + 3]) == 3:
                # print(f' j = {j}   {keyboard[i][j:j + 3]}')
                # pas = pas.islower()
                if keyboard[i][j:j + 3] in pas.lower():
                    sequence_status = False
                    # print(f' j = {j}   {keyboard[i][j:j + 3]}')
                    raise SequenceError

    if sequence_status:
        return True

    # except SequenceError:
    #     print('error')


check_password()
