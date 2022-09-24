cpf = '12345678909'


def test(result_1=0, result_2=0):
    print(len(cpf))
    for i in range(len(cpf) - 2):
        number = len(cpf) - 1 - i
        result_1 += int(cpf[i]) * number
    for i in range(len(cpf) - 1):
        number = len(cpf) - i
        result_2 += int(cpf[i]) * number
    print(result_1)
    print(result_2)
    rest_1 = (result_1 * 10) % 11
    rest_2 = (result_2 * 10) % 11
    print(rest_1)
    print(rest_2)
    if rest_1 == 10:
        rest_1 = 0
    if rest_2 == 10:
        rest_2 = 0
    print(rest_1)
    print(rest_2)
    print(cpf[9])
    print(cpf[10])
    if rest_1 == cpf[len(cpf) - 2] and rest_2 == cpf[len(cpf) - 1]:
        return True
    else:
        return False


cpf = ''.join(i for i in cpf if i.isdigit())

if test():
    print('CPF válido.')
else:
    print('CPF inválido.')
