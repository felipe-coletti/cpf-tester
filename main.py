# cpf de exemplo
cpf = "123.456.789-10"


# Criar a funcão que verifica o CPF
def check(result=0, validation=False):
    # primeiro número * 10, segundo número * 9... Até o último número antes do traço
    for i in range(len(cpf)):
        n = len(cpf) - 1 - i
        result += int(cpf[i]) * n
    # achar o número de verificação
    result = result * 10 // 11
    # transformar num único digito, caso ainda não seja
    if result == 10:
        result = 0
    # verificar se o penúltimo número está correto
    if result == cpf[10]:
        validation = True
    result = 0
    # primeiro número * 11, segundo número * 10... Até o penúltimo número
    for i in range(len(cpf)):
        n = len(cpf) - i
        result += int(cpf[i]) * n
    # achar o número de verificação
    result = result * 10 // 11
    # transformar num único digito, caso ainda não seja
    if result == 10:
        result = 0
    # verificar se o último número não está correto para remover a validação, se for necessário
    if result != cpf[11]:
        validation = False
    return validation


# retirar todos os caracteres e/ou letras do número de CPF
cpf = ''.join(i for i in cpf if i.isdigit())

# exibir o resultado
if check:
    print('CPF válido.')
else:
    print('CPF inválido.')
