def origem_destino_iguais(origem, destino, lista_de_erros):
    """ verifica se origem e destino sao iguais """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino nao pode ser igual'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ verifica se tem algum numero """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = f'{nome_campo} invalido: não pode incluir numeros'


def data_ida_maior_que_data_volta(ida, volta, lista_de_erros):
    """ verifica se data de ida é menor que de volta """
    if ida > volta:
        lista_de_erros['data_volta'] = 'Data de volta nao pode ser menor que data da pesquisa'


def data_ida_menor_que_data_pesquisa(ida, pesquisa, lista_de_erros):
    """ verifica se data de ida é menor que de hoje """
    if ida < pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida nao pode ser menor que data de hoje'
