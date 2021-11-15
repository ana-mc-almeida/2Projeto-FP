'''
Ana Margarida Almeida
ist1102618
ana.margarida.almeida@tecnico.ulisboa.pt
'''


def argumentos_invalidos(funct):
    raise ValueError(funct + ": argumentos invalidos")


def is_str_n_nula(string):
    return type(string) == str and len(string) > 0


def is_int_positivo(num):
    return type(num) == int and num >= 0

#
#   TAD posicao
#


def cria_posicao(x, y):
    '''
    cria_posicao: int x int -> posicao

    Devolve a posição correspondente às coordenadas recebidas.
    '''
    if not (is_int_positivo(x) and is_int_positivo(y)):
        argumentos_invalidos("cria_posicao")
    return (x, y)


def cria_copia_posicao(posicao):
    '''
    cria_copia_posicao: posicao -> posicao

    Devolve uma cópia da posição recebida
    '''
    return posicao.copy()


def obter_pos_x(posicao):
    '''
    obter_pos_x: posicao -> int

    Devolve a abcissa da posição dada
    '''
    return posicao[0]


def obter_pos_y(posicao):
    '''
    obter_pos_y: posicao -> int

    Devolve a ordenada da posição dada
    '''
    return posicao[1]


def eh_posicao(arg):
    '''
    universal -> booleano

    Devolve True caso o argumento dado seja um TAD posicao.
    Caso contrário, devolve False.
    '''
    return type(arg) == tuple and len(arg) == 2 and is_int_positivo(arg[0]) and is_int_positivo(arg[1])


def posicoes_iguais(posicao1, posicao2):
    '''
    posicoes_iguais: posicao x posicao -> booleano

    Devolve True caso os argumentos dados sejam posições iguais.
    Caso contrário, devolve False.
    '''
    return eh_posicao(posicao1) and eh_posicao(posicao2) and posicao2 == posicao1


def posicao_para_str(posicao):
    '''
    posicao_para_str: posicao -> str

    Devolve a cadeia de caracteres '(x, y)' que representa as coordenadas da posição dada.
    '''
    return str(posicao)


def obter_posicoes_adjacentes(posicao):
    '''
    obter_posicoes_adjacentes: posicao -> tuplo

    Devolve um tuplo com as posições adjacentes à posição dada.
    '''
    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)

    if x < 1 and y > 0:
        return (cria_posicao(x, y-1), cria_posicao(x+1, y), cria_posicao(x, y+1))
    if x > 0 and y < 1:
        return (cria_posicao(x+1, y), cria_posicao(x, y+1), cria_posicao(x-1, y))
    return (cria_posicao(x, y-1), cria_posicao(x+1, y), cria_posicao(x, y+1), cria_posicao(x-1, y))


def ordenar_posicoes(posicoes):
    '''
    ordenar_posicoes: tuplo -> tuplo

    Devolve um tuplo com posições ordenadas por ordem de leitura do prado.
    '''
    return sorted(posicoes, key=lambda posicao: (obter_pos_y(posicao), obter_pos_x(posicao)))

#
#   TAD animal
#


def valida_cria_animal(especie, freq_reproducao, freq_alimentacao):
    '''
    valida_cria_animal: universal,  universal,  universal -> booleano


    '''
    return is_str_n_nula(especie) and is_int_positivo(freq_reproducao) and (type(freq_alimentacao) == int and freq_alimentacao >= 0)


def cria_animal(especie, freq_reproducao, freq_alimentacao):
    '''
    cria_animal: str, int, int -> animal

    Devolve o animal correspondente às informações recebidas.
    '''
    if valida_cria_animal(especie, freq_reproducao, freq_alimentacao):
        return {"especie": especie, "idade": 0, "freq_alimentacao": freq_alimentacao, "fome": 0, "freq_reproducao": freq_reproducao}
    argumentos_invalidos("cria_animal")


def cria_copia_animal(animal):
    '''
    cria_copia_animal: animal -> animal

    Devolve uma cópia do animal recebido.
    '''
    return animal.copy()


def obter_especie(animal):
    '''
    obter_especie: animal -> str

    Devolve a espécie do animal recebido.
    '''
    return animal["especie"]


def obter_freq_reproducao(animal):
    '''
    obter_freq_reproducao: animal -> int

    Devolve a frequência de reprodução do animal recebido.
    '''
    return animal["freq_reproducao"]


def obter_freq_alimentacao(animal):
    '''
    obter_freq_alimentacao: animal -> int

    Devolve a frequência de alimentação do animal recebido.
    '''
    return animal["freq_alimentacao"]


def obter_idade(animal):
    '''
    obter_idade: animal -> int

    Devolve a idade do animal recebido.
    '''
    return animal["idade"]


def obter_fome(animal):
    '''
    obter_fome: animal -> int

    Devolve a fome do animal recebido.
    '''
    return animal["fome"]


def aumenta_idade(animal):
    '''
    aumenta_idade: animal -> animal

    Devolve o animal dado, com mais 1 de idade.
    '''
    animal["idade"] += 1
    return animal


def reset_idade(animal):
    '''
    reset_idade: animal -> animal

    Devolve o animal dado, alterando a sua idade para 0.
    '''
    animal["idade"] = 0
    return animal


def eh_animal(arg):
    '''
    eh_animal: universal -> booleano

    Devolve True caso o argumento dado seja um TAD animal.
    Caso contrário, devolve False.
    '''
    if type(arg) == dict and len(arg) == 5 and {"especie", "idade", "fome", "freq_alimentacao", "freq_reproducao"} <= arg.keys():
        return valida_cria_animal(obter_especie(arg), obter_freq_reproducao(arg), obter_freq_alimentacao(arg)) and is_int_positivo(obter_fome(arg)) and is_int_positivo(obter_idade(arg))
    return False


def eh_predador(arg):
    '''
    eh_predador: universal -> booleano

    Devolve True caso o argumento dado seja um TAD animal do tipo predador.
    Caso contrário, devolve False.
    '''
    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    '''
    eh_presa: universal -> booleano

    Devolve True caso o argumento dado seja um TAD animal do tipo presa.
    Caso contrário, devolve False.
    '''
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


def aumenta_fome(animal):
    '''
    aumenta_fome: animal -> animal

    Devolve o animal dado com mais 1 de fome, caso seja predador.
    Caso seja presa, o animal não é alterado.
    '''
    if eh_predador(animal):
        animal["fome"] += 1
    return animal


def reset_fome(animal):
    '''
    reset_fome: animal -> animal

    Devolve o animal dado, alterando a sua fome para 0, caso seja predador.
    Caso seja presa, o animal não é alterado.
    '''
    if eh_predador(animal):
        animal["fome"] = 0
    return animal


def animais_iguais(animal1, animal2):
    '''
    animais_iguais: animal, animal -> booleano

    Devolve True caso os argumentos dados sejam animais iguais.
    Caso contrário, devolve False.
    '''
    return animal1 == animal2


def animal_para_char(animal):
    '''
    animal_para_char: animal -> str

    Devolve o primeiro caracter da espécie do animal recebido.
    Caso este animal seja um predador o caracter será maiúsculo.
    Caso contrário, o caracter será minúsculo.
    '''
    especie = obter_especie(animal)
    if eh_predador(animal):
        return especie[0].upper()
    return especie[0].lower()


def animal_para_str(animal):
    '''
    animal_para_str: animal -> str

    Devolve a string que representa o animal, no seguinte formato:
    - Caso seja predador: <especie> [<idade>/<frequência de reprodução>;<fome>/<frequência de alimentação>]
    - Caso seja presa: <especie> [<idade>/<frequência de reprodução>]
    '''
    result = f"{obter_especie(animal)} [{obter_idade(animal)}/{obter_freq_reproducao(animal)}"

    if eh_predador(animal):
        result = f"{result};{obter_fome(animal)}/{obter_freq_alimentacao(animal)}"

    result = f"{result}]"

    return result


def eh_animal_fertil(animal):
    '''
    eh_animal_fertil: animal -> booleano

    Devolve True caso o animal dado tenha atingido a idade de reprodução.
    Caso contrário, devolve False.
    '''
    return obter_idade(animal) >= obter_freq_reproducao(animal)


def eh_animal_faminto(animal):
    '''
    eh_animal_faminto: animal -> booleano

    Devolve True caso o animal dado tenha um valor de fome igual ou superior à sua frequência de alimentação.
    Caso contrário, devolve False.
    '''
    if eh_presa(animal):
        return False
    return obter_fome(animal) >= obter_freq_alimentacao(animal)


def reproduz_animal(animal):
    '''
    reproduz_animal: animal -> animal

    Devolve um novo animal da mesma espécie do animal recebido, idade e fome igual a 0.
    Modifica destrutivamente animal recebido, alterando a sua idade para 0.
    '''
    novo_animal = cria_copia_animal(animal)
    novo_animal = reset_fome(novo_animal)
    novo_animal = reset_idade(novo_animal)
    animal = reset_idade(animal)
    return novo_animal


#
# TAD prado
#


def cria_prado():
    '''
    cria_prado: posicao, tuplo, tuplo, tuplo -> prado
    '''
    pass


def cria_copia_prado(prado):
    '''
    cria_copia_prado: prado -> prado
    '''
    pass


def obter_tamanho_x(prado):
    '''
    obter_tamanho_x: prado -> int
    '''
    pass


def obter_tamanho_y(prado):
    '''
    cria_prado: prado -> int
    '''
    pass


def obter_numero_predadores(prado):
    '''
    obter_numero_predadores: prado -> int
    '''
    pass


def obter_numero_presas(prado):
    '''
    obter_numero_presas: prado -> int
    '''
    pass


def obter_posicao_animais(prado):
    '''
    obter_posicao_animais: prado -> tuplo posicoes
    '''
    pass


def obter_animal():
    '''
    obter_animal: prado, posicao -> animal
    '''
    pass


def eliminar_animal(prado):
    '''
    eliminar_animal: prado, posicao -> prado
    '''
    pass


def mover_animal(prado):
    '''
    mover_animal: prado, posicao, posicao -> prado
    '''
    pass


def inserir_animal(prado):
    '''
    inserir_animal: prado, animal, posicao -> prado
    '''
    pass


def eh_prado(prado):
    '''
    eh_prado: universal -> booleano
    '''
    pass


def eh_posicao_animal(prado):
    '''
    eh_posicao_animal: prado, posicao -> booleano
    '''
    pass


def eh_posicao_obstaculo(prado):
    '''
    eh_posicao_obstaculo: prado, posicao -> booleano
    '''
    pass


def eh_posicao_livre(prado):
    '''
    eh_posicao_livre: prado, posicao -> booleano
    '''
    pass


def prados_iguais(prado):
    '''
    prados_iguais: prado, prado -> booleano
    '''
    pass


def prado_para_str(prado):
    '''
    prado_para_str: prado -> str
    '''
    pass


def obter_valor_numerico(prado):
    '''
    obter_valor_numerico: prado, posicao -> int
    '''
    pass


def obter_movimento(prado):
    '''
    obter_movimento: prado, posicao -> posicao
    '''
    pass

#
#
#


def geracao():
    '''
    geracao: prado -> prado
    '''
    pass


def simula_ecossistema():
    '''
    simula_ecossistema: str, int, booleano -> tuplo
    '''
    pass
