# CPF de exemplo
cpf = '123.456.789-10'


# Criar a funcão que verifica o CPF
def check(result_1=0, result_2=0):
    # primeiro número * 10, segundo número * 9... Até o último número antes do traço
    for i in range(len(cpf)):
        number = len(cpf) - 1 - i
        result_1 += int(cpf[i]) * number
    # primeiro número * 11, segundo número * 10... Até o penúltimo número
    for i in range(len(cpf)):
        number = len(cpf) - i
        result_2 += int(cpf[i]) * number
    # achar o número de verificação
    result_1 = result_1 * 10 // 11
    result_2 = result_2 * 10 // 11
    # transformar num único digito, caso ainda não seja
    if result_1 == 10:
        result_1 = 0
    if result_2 == 10:
        result_2 = 0
    # fazer a validação do CPF
    if result_1 != cpf[10] and result_2 != cpf[11]:
        validation = True
    else:
        validation = False
    return validation


# retirar todos os caracteres e/ou letras do número de CPF
cpf = ''.join(i for i in cpf if i.isdigit())

# exibir o resultado
if check:
    print('CPF válido.')
else:
    print('CPF inválido.')
