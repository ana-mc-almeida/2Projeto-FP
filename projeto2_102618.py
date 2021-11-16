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
    novo_animal = reset_idade((reset_fome(cria_copia_animal(animal))))
    animal = reset_idade(animal)
    # return novo_animal, animal
    return novo_animal


# animal = aumenta_idade(cria_animal("anan", 45, 5))
# print(reproduz_animal(animal))
# print(animal)

#
# TAD prado
#


def print_prado(prado):  # não é para o projeto
    for y in range(len(prado)):
        for x in range(len(prado[y])):
            if eh_animal(prado[y][x]):
                print("a", end=" ")
            else:
                print(prado[y][x], end=" ")
        print()


def cria_prado(ultima_posicao, rochedos, animais, posicoes_animais):
    '''
    cria_prado: posicao, tuplo, tuplo, tuplo -> prado

    '''
    def valida_cria_prado():
        if not(eh_posicao(ultima_posicao) and type(rochedos) == type(animais) == type(posicoes_animais) and len(animais) == len(posicoes_animais)):
            argumentos_invalidos("cria_prado")

    def criar_estrutura_prado(max_x, max_y):
        for y in range(max_y+1):
            prado.append([])
            for x in range(max_x+1):
                if y == 0 or y == max_y or x == 0 or x == max_x:
                    prado[y] += "r"
                else:
                    prado[y] += "."

    def colocar_rochedos(rochedos):
        for rochedo in rochedos:
            prado[obter_pos_y(rochedo)][obter_pos_x(rochedo)] = "r"

    def colocar_animais(animais, posicoes):
        for i in range(len(posicoes)):
            posicao = posicoes[i]
            prado[obter_pos_y(posicao)][obter_pos_x(posicao)] = animais[i]
        return prado

    valida_cria_prado()

    prado = []
    max_x = obter_pos_x(ultima_posicao)
    max_y = obter_pos_y(ultima_posicao)

    criar_estrutura_prado(max_x, max_y)
    colocar_rochedos(rochedos)
    colocar_animais(animais, posicoes_animais)

    # print_prado(prado)
    return(prado)


def cria_copia_prado(prado):
    '''
    cria_copia_prado: prado -> prado

    Devolve uma cópia do prado recebido.
    '''
    return [[x for x in linha] for linha in prado]


def obter_tamanho_x(prado):
    '''
    obter_tamanho_x: prado -> int

    Devolve o valor inteiro que corresponde à dimensão Nx do prado recebido.
    '''
    return len(prado[0])


def obter_tamanho_y(prado):
    '''
    cria_prado: prado -> int

    Devolve o valor inteiro que corresponde à dimensão Ny do prado recebido.
    '''
    return len(prado)


def obter_numero_predadores(prado):
    '''
    obter_numero_predadores: prado -> int

    Devolve o número de predadores do prado.
    '''
    count = 0
    for y in range(1, len(prado)):
        for x in range(1, len(prado[y])):
            if eh_predador(prado[y][x]):
                count += 1
    return count


def obter_numero_presas(prado):
    '''
    obter_numero_presas: prado -> int

    Devolve o número de presas do prado.
    '''
    count = 0
    for y in range(1, len(prado)):
        for x in range(1, len(prado[y])):
            if eh_presa(prado[y][x]):
                count += 1
    return count


def obter_posicao_animais(prado):
    '''
    obter_posicao_animais: prado -> tuplo posicoes

    Devolve um tuplo com todas as posições em que se encontra um animal.
    Estas posições estão ordenadas por ordem de leitura do prado.
    '''
    posicoes = ()
    for y in range(1, len(prado)):
        for x in range(1, len(prado[y])):
            if eh_presa(prado[y][x]) or eh_predador(prado[y][x]):
                posicoes += (cria_posicao(x, y),)
    return posicoes


def obter_animal(prado, posicao):
    '''
    obter_animal: prado, posicao -> animal

    Devolve o animal do prado que se encontra na posição dada.
    '''
    return prado[obter_pos_y(posicao)][obter_pos_x(posicao)]


def eliminar_animal(prado, posicao):
    '''
    eliminar_animal: prado, posicao -> prado

    Devolve o prado, depois de eliminar o animal que se encontrava na posição recebida.
    '''
    prado[obter_pos_y(posicao)][obter_pos_x(posicao)] = "."
    return prado


def inserir_animal(prado, animal, posicao):
    '''
    inserir_animal: prado, animal, posicao -> prado

    Devolve o prado, depois de adicionado à posição recebida o animal dado.
    '''
    prado[obter_pos_y(posicao)][obter_pos_x(posicao)] = animal
    return prado


def mover_animal(prado, posicao_inicial, posicao_nova):
    '''
    mover_animal: prado, posicao, posicao -> prado

    Devolve o prado, depois de movimentado o animal da posição inicial para a nova posição.
    '''
    animal = obter_animal(prado, posicao_inicial)
    prado = inserir_animal(prado, animal, posicao_nova)
    prado = eliminar_animal(prado, posicao_inicial)

    return prado


def eh_prado(prado):
    '''
    eh_prado: universal -> booleano

    Devolve True caso o argumento dado seja um TAD prado.
    Caso contrário, devolve False.
    '''
    return type(prado) == list and all(map(lambda y: type(y) == list and y != [], prado))


def eh_posicao_animal(prado, posicao):
    '''
    eh_posicao_animal: prado, posicao -> booleano

    Devolve True caso a posição dada do prado esteja ocupada por um animal.
    Caso contrário, devolve False.
    '''
    return eh_animal(obter_animal(prado, posicao))


def eh_posicao_obstaculo(prado, posicao):
    '''
    eh_posicao_obstaculo: prado, posicao -> booleano

    Devolve True caso a posição dada do prado seja um rochedo.
    Caso contrário, devolve False.
    '''
    # return obter_pos_y(posicao) <= obter_tamanho_y(prado) and obter_pos_x(posicao) <= obter_tamanho_x(prado) and obter_animal(prado, posicao) == "r"
    return obter_animal(prado, posicao) == "r"


def eh_posicao_livre(prado, posicao):
    '''
    eh_posicao_livre: prado, posicao -> booleano

    Devolve True caso a posição dada do prado esteja livre.
    Caso contrário, devolve False.
    '''
    return obter_animal(prado, posicao) == "."


def prados_iguais(prado1, prado2):
    '''
    prados_iguais: prado, prado -> booleano
    '''
    return prado1 == prado2


def prado_para_str(prado):
    '''
    prado_para_str: prado -> str

    Devolve uma cadeia de caracteres que representa o prado.
    '''
    result = ""
    max_x = obter_tamanho_x(prado)
    max_y = obter_tamanho_y(prado)

    for y in range(max_y):
        for x in range(max_x):
            if (x == 0 and y == 0) or (x == max_x-1 and y == max_y-1) or (x == 0 and y == max_y-1) or (x == max_x-1 and y == 0):
                result += "+"
            elif x == 0 or x == max_x-1:
                result += "|"
            elif y == 0 or y == max_y-1:
                result += "-"
            elif eh_posicao_livre(prado, cria_posicao(x, y)):
                result += "."
            elif eh_posicao_obstaculo(prado, cria_posicao(x, y)):
                result += "@"
            else:
                result += animal_para_char(obter_animal(prado,
                                           cria_posicao(x, y)))
        if y != max_y-1:
            result += "\n"
    return result


def obter_valor_numerico(prado, posicao):
    '''
    obter_valor_numerico: prado, posicao -> int

    Devolve o valor numérico da posição recebida.
    '''
    return obter_pos_y(posicao) * obter_tamanho_x(prado) + obter_pos_x(posicao)


def obter_movimento(prado, posicao):
    '''
    obter_movimento: prado, posicao -> posicao

    Devolve a posição seguinte do animal que se encontra na posição recebida.
    '''
    posicao_nova = posicao
    valor_numerico = obter_valor_numerico(prado, posicao)
    posicoes_adjacentes = obter_posicoes_adjacentes(posicao)
    movimentos = []

    if eh_predador(obter_animal(prado, posicao)):
        for posicao_adjacente in posicoes_adjacentes:
            if eh_presa(obter_animal(prado, posicao_adjacente)):
                movimentos.append(posicao_adjacente)
    if movimentos == []:  # significa que a posição dada tem uma presa ou não tem presas à volta
        for posicao_adjacente in posicoes_adjacentes:
            if eh_posicao_livre(prado, posicao_adjacente):
                movimentos.append(posicao_adjacente)
    if movimentos != []:
        posicao_nova = movimentos[valor_numerico % len(movimentos)]
    return posicao_nova


#
#
#


def geracao(prado):
    '''
    geracao: prado -> prado
    '''
    posicoes_movimentadas = []
    posicoes_animais = obter_posicao_animais(prado)
    for posicao in posicoes_animais:
        if posicao not in posicoes_movimentadas:
            animal = obter_animal(prado, posicao)
            animal = aumenta_idade(animal)
            animal = aumenta_fome(animal)
            posicao_nova = obter_movimento(prado, posicao)
            if not posicoes_iguais(posicao, posicao_nova):  # muda de posição
                # reproduz e come
                if eh_animal_fertil(animal) and eh_presa(obter_animal(prado, posicao_nova)):
                    prado = eliminar_animal(prado, posicao_nova)
                    animal = reset_fome(animal)
                    animal_novo, animal = reproduz_animal(animal)
                    prado = mover_animal(prado, posicao, posicao_nova)
                    prado = inserir_animal(animal_novo, posicao)
                elif eh_presa(obter_animal(prado, posicao_nova)):  # só come
                    animal = reset_fome(animal)
                    prado = eliminar_animal(prado, posicao_nova)
                    prado = mover_animal(prado, posicao, posicao_nova)
                elif eh_animal_faminto(animal):  # morre à fome
                    prado = eliminar_animal(prado, posicao)
                elif eh_animal_fertil(animal):    # só reproduz
                    animal_novo, animal = reproduz_animal(animal)
                    prado = mover_animal(prado, posicao, posicao_nova)
                    prado = inserir_animal(prado, animal_novo, posicao)
                else:
                    prado = mover_animal(prado, posicao, posicao_nova)
                posicoes_movimentadas.append(posicao_nova)
            elif eh_animal_faminto(animal):
                prado = eliminar_animal(prado, posicao)
    return prado


def get_ultima_posicao(line):
    ultima_posicao_re = eval(line)  # re = representação externa
    return cria_posicao(ultima_posicao_re[0], ultima_posicao_re[1])


def get_rochedos(line):
    rochedos = ()
    rochedos_re = eval(line)
    for rochedo_re in rochedos_re:
        rochedos += (cria_posicao(rochedo_re[0], rochedo_re[1]),)
    return rochedos


def get_animais_e_posicoes(linhas):
    animais = ()
    posicoes_animais = ()
    for linha in linhas:
        tudo = eval(linha)
        posicoes_animais += (cria_posicao(tudo[-1][0], tudo[-1][1]),)
        animais += (cria_animal(tudo[0], tudo[1], tudo[2]),)
    return animais, posicoes_animais


def mostra_geracao(prado, g):
    print("Predadores: " + str(obter_numero_predadores(prado)), end=" ")
    print("vs", end=" ")
    print("Presas: " + str(obter_numero_presas(prado)), end=" ")
    print("(Gen. " + str(g) + ")")
    print(prado_para_str(prado))


def simula_ecossistema(ficheiro, geracoes, verboso):
    '''
    simula_ecossistema: str, int, booleano -> tuplo
    '''
    file = open(ficheiro, "r")

    linhas = file.readlines()
    ultima_posicao = get_ultima_posicao(linhas[0])
    rochedos = get_rochedos(linhas[1])
    animais, posicoes_animais = get_animais_e_posicoes(linhas[2:])

    espacos_livres = (obter_pos_x(ultima_posicao) - 2) * \
        (obter_pos_y(ultima_posicao) - 2) - len(rochedos)

    file.close()

    prado = cria_prado(ultima_posicao, rochedos, animais, posicoes_animais)

    mostra_geracao(prado, 0)
    predadores = obter_numero_predadores(prado)
    presas = obter_numero_presas(prado)
    for g in range(1, geracoes+1):
        if espacos_livres == predadores or espacos_livres == presas:
            break
        prado = geracao(prado)
        if (predadores != obter_numero_predadores(prado) or presas != obter_numero_presas(prado)) and verboso:
            mostra_geracao(prado, g)
        predadores = obter_numero_predadores(prado)
        presas = obter_numero_presas(prado)

    if not verboso:
        mostra_geracao(prado, g)
    print(f"({obter_numero_predadores(prado)}, {obter_numero_presas(prado)})")
