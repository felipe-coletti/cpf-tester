# solicita o CPF do usuário
cpf = input('CPF: ')

# estado onde o CPF do usuário foi registrado
state = 'São Paulo'

# lista com o 9º dígito do CPF para cada estado
states = {
    'Rio Grande do Sul': 0,
    'Distrito Federal': 1,
    'Goiás': 1,
    'Mato Grosso': 1,
    'Mato Grosso do Sul': 1,
    'Tocantins': 1,
    'Amazonas': 2,
    'Pará': 2,
    'Roraima': 2,
    'Amapá': 2,
    'Acre': 2,
    'Rondônia': 2,
    'Ceará': 3,
    'Maranhão': 3,
    'Piauí': 3,
    'Paraíba': 4,
    'Pernambuco': 4,
    'Alagoas': 4,
    'Rio Grande do Norte': 4,
    'Bahia': 5,
    'Sergipe': 5,
    'Minas Gerais': 6,
    'Rio de Janeiro': 7,
    'Espírito Santo': 7,
    'São Paulo': 8,
    'Paraná': 9,
    'Santa Catarina': 9
}


# verifica se o CPF é válido
def test(result_1=0, result_2=0):
    # n0 * 10, n1 * 9...
    for i in range(len(cpf) - 2):
        number = len(cpf) - 1 - i
        result_1 += int(cpf[i]) * number
    # n0 * 11, n1 * 10...
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


# verifica se os números não são todos iguais
def no_repeats(repeats=0):
    for i in range(len(cpf)):
        if cpf[i] == cpf[i - 1]:
            repeats += 1
    if repeats < 11:
        return True
    else:
        return False


# remove letras e caracteres estranhos do CPF
cpf = ''.join(i for i in cpf if i.isdigit())

# exibe o resultado
if int(cpf[8]) == states[state] and test() and no_repeats():
    print('CPF válido.')
else:
    print('CPF inválido.')
