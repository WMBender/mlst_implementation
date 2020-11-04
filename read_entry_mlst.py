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

def verifica_alcance_vertices():
    for i in range(len(s0)):
        if s0[i]:
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

def greed_randomized_solution(alpha):
    while(verifica_alcance_vertices() == 0):
        rcl = melhores_candidatos(quantos_vertices_rotulo_atinge(),alpha)  #Restricted Candidate List
        rotulo_escolhido = random.choice(rcl)
        print('rotulo adicionado = ', rotulo_escolhido)
        s0[rotulo_escolhido] = 1
        print(s0)
    return s0

print(s0)
test_g_r_s = greed_randomized_solution(30)
# print(test_g_r_s)
#
# def grasp(s0,alpha):
#     solucao_atual = s0
#     do:
#         nova_solucao = greed_randomized_solution(alpha)
#         nova_solucao = busca_local(nova_solucao)
#         if( f(nova_solucao) < f(solucao_atual)):
#             solucao_atual = nova_solucao
#     until a stop criterion is satisfied
#     return s
