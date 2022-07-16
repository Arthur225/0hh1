"""

*********************************
Feito por Arthur Andrade
*********************************

Agradecimento especial: Lucas Weber

"""

import winsound

import keyboard
import pyautogui

# valores rgb
amarelo = 200  # "(255, 213, 0)"
azul = 20  # "(0, 89, 190)"
preto = 38  # "(42, 42, 42)"
fundo = 39  # "(34, 34, 34)"


# coordenadas iniciais
cordx_inicial = 671
cordy_inicial = 264

cordx_inicial_verdadeira = 0

distancia_final = 0


def distancia_entre_cada():  # distância entre cada verificação de cor
    quadrado = 0
    espaco = 0
    teste_de_cor = qual_cor(cordx_inicial, cordy_inicial)
    cordx_nova = cordx_inicial
    cordy_nova = cordy_inicial
    while teste_de_cor != 4:
        teste_de_cor = qual_cor(cordx_nova - 1, cordy_nova)
        cordx_nova -= 1
    cordx_nova += 1
    teste_de_cor = qual_cor(cordx_nova, cordy_nova)
    global cordx_inicial_verdadeira
    cordx_inicial_verdadeira = cordx_nova + 10
    while teste_de_cor != 4:
        teste_de_cor = qual_cor(cordx_nova + 1, cordy_nova)
        cordx_nova += 1
        quadrado += 1
    distancia = quadrado
    while teste_de_cor == 4:
        teste_de_cor = qual_cor(cordx_nova + 1, cordy_nova)
        cordx_nova += 1
        espaco += 1
    distancia += espaco
    return distancia


def qual_cor(cordx, cordy):  # verifica a cor do pixel
    valor_atual, g, b = pyautogui.pixel(cordx, cordy)
    if valor_atual > amarelo:
        return 1
    if valor_atual < azul:
        return 2
    if valor_atual > preto:
        return 0
    if valor_atual < fundo:
        return 4
    else:
        print(valor_atual)


def arrumar(parametro_lista):  # arruma tudo na lista, linha por linha
    lista = parametro_lista
    for v in range(len(lista)):
        #  confere se já tem metade:
        if lista[v].count(1) == (len(lista) / 2):
            substituir(lista[v], 0, 2)
        if lista[v].count(2) == (len(lista) / 2):
            substituir(lista[v], 0, 1)

        #  confere se tem 2 seguidos ou 1, espaço, outro e troca eles:
        for n in range(len(lista[v])):
            if lista[v][n] != 0:
                soma = 0
                outra_cor = get_outra_cor(lista[v][n])
                #  verifica se não é o ultimo pra ver se são dois seguidos:
                if n < (len(lista[v]) - 1 + soma):
                    #  verifica se o próximo é da mesma cor:
                    if lista[v][n] == lista[v][n + 1]:
                        #  verifica se não é o primeiro:
                        if n > 0:
                            lista[v][n - 1] = outra_cor
                        #  verifica se não é o penúltimo:
                        if n < (len(lista[v]) - 2 + soma):
                            lista[v][n + 2] = outra_cor
                #  verifica se é antepenúltimo para saber se é 1, espaço, outro:
                if n < (len(lista[v]) - 2 + soma):
                    #  verifica se o depois do próximo é da mesma cor:
                    if lista[v][n] == lista[v][n + 2]:
                        lista[v][n + 1] = outra_cor

        #  confere se tem outra linha pronta igual e deixa diferente:
        #  verifica se tem 2 zeros:
        if lista[v].count(0) == 2:
            for k in range(len(lista)):
                if lista[v].count(0) == 2:
                    linha_provisoria = lista[v]
                    #  verifica se a lista tá cheia:
                    if lista[k].count(0) == 0 and 0 in linha_provisoria:
                        primeiro_zero = linha_provisoria.index(0)
                        segundo_zero = len(linha_provisoria) - list(reversed(linha_provisoria)).index(0) - 1
                        teste = lista[v]
                        #  troca os dois index:
                        linha_provisoria[primeiro_zero] = lista[k][primeiro_zero]
                        linha_provisoria[segundo_zero] = lista[k][segundo_zero]
                        lista[v] = teste
                        #  verifica se ficou igual:
                        if linha_provisoria == lista[k]:
                            lista[v][primeiro_zero] = get_outra_cor(lista[k][primeiro_zero])
                            lista[v][segundo_zero] = get_outra_cor(lista[k][segundo_zero])
                        else:
                            lista[v][primeiro_zero] = 0
                            lista[v][segundo_zero] = 0
    return lista


def clicar_em_cada(lista, distancia, cordx_inicio, cordy_inicio):  # clica nos quadrados de acordo com valores da lista
    for u in range(len(lista)):
        for t in range(len(lista[i])):
            if lista[u][t] == 1:
                pyautogui.click(x=cordx_inicio + (t * distancia), y=cordy_inicio + (u * distancia))
            else:
                pyautogui.click(x=cordx_inicio + (t * distancia), y=cordy_inicio + (u * distancia), button="right")


def verseterminou(lista):  # verifica se tem 0 na lista
    for m in range(len(lista)):
        for b in range(len(lista[m])):
            if lista[m][b] == 0:
                return False
    return True


def printarlista(lista):  # imprime lista por lista
    for p in range(len(lista)):
        print(lista[p])


def trocarorientacao(lista):  # transforma linhas em colunas e vice-versa
    lista_pro = []
    for r in range(x):
        prov = []
        for o in range(x):
            prov.append(lista[o][r])
        lista_pro.append(prov)
    return lista_pro


def substituir(lista, esse, por_esse):  # substitui elementos iguais de uma lista por outros
    for j in range(len(lista)):
        if lista[j] == esse:
            lista[j] = por_esse


def get_outra_cor(primeira_cor):  # pega a cor contrária
    if primeira_cor == 1:
        return 2
    else:
        return 1


while 1:  # loop infinito
    if keyboard.is_pressed('p'):
        # forma a matriz do tabuleiro:
        pyautogui.moveTo(1, cordy_inicial)
        tapronto = False
        distancia_final = distancia_entre_cada()
        lista_linhas = []
        lista_colunas = []
        linha1 = []
        x = 0
        controle = 0
        while controle != 4:
            linha1.append(qual_cor(cordx_inicial_verdadeira + (x * distancia_final), cordy_inicial))
            x += 1
            controle = qual_cor(cordx_inicial_verdadeira + (x * distancia_final), cordy_inicial)
        lista_linhas.append(linha1)
        numy = 1
        for i in range(x - 1):

            y = 0
            controle = 0
            outras_linhas = []
            while controle != 4:
                outras_linhas.append(qual_cor(cordx_inicial_verdadeira + (y * distancia_final),
                                              cordy_inicial + (numy * distancia_final)))
                y += 1
                controle = qual_cor(cordx_inicial_verdadeira + (y * distancia_final),
                                    cordy_inicial + (numy * distancia_final))
            lista_linhas.append(outras_linhas)
            numy += 1

        print("-------------------------------------------------------------------------------------------------------")

        # imprime a matriz inicial:
        print("\n")
        print("Valores iniciais:")
        print("\n")
        printarlista(lista_linhas)
        winsound.Beep(440, 500)
        print("Tamanho tabuleiro:")
        print(str(x) + "x" + str(x))

        # resolve o jogo a partir da matriz:
        while not tapronto:
            lista_colunas = trocarorientacao(arrumar(lista_linhas))
            lista_linhas = trocarorientacao(arrumar(lista_colunas))

            tapronto = verseterminou(lista_linhas)  # verifica se tem zeros na lista

        # imprime a matriz resolvida:
        print("\n")
        print("Valores finais:")
        print("\n")
        printarlista(lista_linhas)

        winsound.Beep(440, 500)

        clicar_em_cada(lista_linhas, distancia_final, cordx_inicial_verdadeira, cordy_inicial)  # chama função de click

        winsound.Beep(440, 500)
        winsound.Beep(440, 500)
        winsound.Beep(440, 500)

        print("\n")
        print("Finalizado")
        print("\n")
        print("-------------------------------------------------------------------------------------------------------")
