# solicite o CPF do usuário
cpf = int(input("CPF: "))


# Crie a funcão que verifica o CPF
def test(result_1=0, result_2=0):
    # primeiro número * 10, segundo número * 9... Até o último número antes do traço
    for i in range(len(cpf)):
        number = len(cpf) - 1 - i
        result_1 += cpf[i] * number
    # primeiro número * 11, segundo número * 10... Até o penúltimo número
    for i in range(len(cpf)):
        number = len(cpf) - i
        result_2 += cpf[i] * number
    # ache o número de verificação
    rest_1 = result_1 * 10 // 11
    rest_2 = result_2 * 10 // 11
    # transforme o resto das divisões num único digito, caso ainda não seja
    if rest_1 == 10:
        rest_1 = 0
    if rest_2 == 10:
        rest_2 = 0
    # fazça a validação do CPF
    if rest_1 != cpf[10] and rest_2 != cpf[11]:
        validation = True
    else:
        validation = False
    return validation


# retire todos os caracteres e/ou letras do número de CPF
cpf = ''.join(i for i in cpf if i.isdigit())

# exiba a saída
if test:
    print('CPF válido.')
else:
    print('CPF inválido.')
