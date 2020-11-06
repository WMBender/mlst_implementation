import sys
from numpy import random

arestas = []

with open(sys.argv[1], 'r') as f:
    content = f.readlines()
    first_line = content[0].split()

n_vertices = int(first_line[0])
n_arestas = int(first_line[1])
n_rotulos = int(first_line[2])

for i in range(1, len(content)):
    split_line = content[i].split()
    arestas.append((int(split_line[0]), int(split_line[1]), int(split_line[2])))

s0 = []  # solução_inicial = zeros

for i in range(n_rotulos):
    s0.append(0)

vertices_atingidos = []

for i in range(n_vertices):
    vertices_atingidos.append(0)

def verifica_alcance_vertices(solution):
    for i in range(len(solution)):
        if solution[i]:
            for j in arestas:
                if j[2] == i:
                    vertices_atingidos[j[0]] = 1
                    vertices_atingidos[j[1]] = 1
    if 0 in vertices_atingidos:
        return 0
    else:
        return 1

# s0[0] = 1
# s0[1] = 1
# s0[2] = 1
# s0[3] = 1
# s0[4] = 1

# alcanca_todos = verifica_alcance_vertices()
# print("vertice i atingido ?")
# for i in range(len(vertices_atingidos)):
#     print('vertice ', i, ' = ', vertices_atingidos[i])
#
# print("alcança todos ?", alcanca_todos)

def quantos_vertices_rotulo_atinge():
    new_rotulos = []
    for i in range(n_rotulos):
        new_vertices_atingidos = []
        for j in arestas:
            if (j[2] == i):
                if(vertices_atingidos[j[0]] == 0):
                    new_vertices_atingidos.append(j[0])
                if (vertices_atingidos[j[1]] == 0):
                    new_vertices_atingidos.append(j[1])
        new_rotulos.append(len(set(new_vertices_atingidos)))
    return new_rotulos

# vertices_por_rotulo = quantos_vertices_rotulo_atinge()
# print(vertices_por_rotulo)

def melhores_candidatos(lista,alpha):
    n_melhores = round(len(lista) * alpha / 100)
    # print('n_melhores = ', n_melhores)
    posicao_max = []
    while n_melhores > 0:
        for i in range(len(lista)):
            max_list = max(lista)
            if (max_list == lista[i]):
                posicao_max.append(i)
                lista[i] = 0
                n_melhores -= 1
                break
    return posicao_max

def greed_randomized_solution(solucao_atual,alpha):
    while(verifica_alcance_vertices(solucao_atual) == 0):
        rcl = melhores_candidatos(quantos_vertices_rotulo_atinge(),alpha)  #Restricted Candidate List
        rotulo_escolhido = random.choice(rcl)
        print('rotulo adicionado = ', rotulo_escolhido)
        s0[rotulo_escolhido] = 1
        print(s0)
    return s0

# test_g_r_s = greed_randomized_solution(s0,30)
# print(test_g_r_s)

def gera_vizinhos(solution):
    vizinhos = []
    copy_solution = solution.copy()
    for i in range(len(copy_solution)):
        if copy_solution[i] == 1:
            copy_solution[i] = 0
            if verifica_alcance_vertices(copy_solution):
                vizinhos.append(copy_solution)
            copy_solution[i] = 1
    if len(vizinhos) == 0:
        return solution
    else:
        return vizinhos

def busca_local(solution):
    vizinhos = gera_vizinhos(solution)
    if vizinhos[0] is int:
        return vizinhos
    else:
        return random.choice(vizinhos)

def n_rotulos_usados(solution):
    count = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            count +=1
    return count


def grasp(s0,alpha):
    solucao_atual = s0
    iterations = 0
    while iterations < 20:
        nova_solucao = greed_randomized_solution(solucao_atual,alpha)
        nova_solucao = busca_local(nova_solucao)
        if( n_rotulos_usados(nova_solucao) < n_rotulos_usados(solucao_atual)):
            print("solucao atualizada")
            solucao_atual = nova_solucao
    iterations+=1
    return solucao_atual
