cpf = '12345678909'


# Criar a funcão que verifica o CPF
def test(result_1=0, result_2=0):
    print(len(cpf))
    # primeiro número * 10, segundo número * 9... Até o último número antes do traço
    for i in range(len(cpf) - 2):
        number = len(cpf) - 1 - i
        result_1 += int(cpf[i]) * number
    # primeiro número * 11, segundo número * 10... Até o penúltimo número
    for i in range(len(cpf) - 1):
        number = len(cpf) - i
        result_2 += int(cpf[i]) * number
    # achar o número de verificação
    print(result_1)
    print(result_2)
    rest_1 = result_1 * 10 % 11
    rest_2 = result_2 * 10 % 11
    print(rest_1)
    print(rest_2)
    # transformar num único digito, caso ainda não seja
    if rest_1 == 10:
        rest_1 = 0
    if rest_2 == 10:
        rest_2 = 0
    print(rest_1)
    print(rest_2)
    # fazer a validação do CPF
    print(rest_1)
    print(cpf[9])
    print(rest_2)
    print(cpf[10])
    if rest_1 == len(cpf) - 2 and rest_2 == len(cpf) - 1:
        validation = True
    else:
        validation = False
    return validation


# retirar todos os caracteres e/ou letras do número de CPF
cpf = ''.join(i for i in cpf if i.isdigit())

# exibir o resultado
if test():
    print('CPF válido.')
else:
    print('CPF inválido.')
