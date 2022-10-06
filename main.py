cpf = input('CPF: ')


def test(result_1=0, result_2=0):
    for i in range(len(cpf) - 2):
        number = len(cpf) - 1 - i
        result_1 += int(cpf[i]) * number
    for i in range(len(cpf) - 1):
        number = len(cpf) - i
        result_2 += int(cpf[i]) * number
    rest_1 = (result_1 * 10) % 11
    rest_2 = (result_2 * 10) % 11
    if rest_1 == 10:
        rest_1 = 0
    if rest_2 == 10:
        rest_2 = 0
    if rest_1 == int(cpf[len(cpf) - 2]) and rest_2 == int(cpf[len(cpf) - 1]):
        return True
    else:
        return False


cpf = ''.join(i for i in cpf if i.isdigit())

if test():
    print('CPF válido.')
else:
    print('CPF inválido.')
