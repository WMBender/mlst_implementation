import sys
from collections import Counter

n_vertices = 0
n_arestas = 0
n_rotulos = 0

rotulos_used = []

with open(sys.argv[1], 'r') as f:
    content=f.readlines()
    first_line=content[0].split()


n_vertices = int(first_line[0])
n_arestas = int(first_line[1])
n_rotulos = int(first_line[2])

print(n_vertices,n_arestas,n_rotulos)

for i in range(1,len(content)):
    split_line=content[i].split()
    rotulos_used.append(split_line[2])

rotulos_ocurrencies = Counter(rotulos_used)
print(rotulos_ocurrencies['1'])

s0 = []

for i in range(n_rotulos):
    s0.append(0)

print(s0)
alpha = 5

# def greed_randomized_solution(alpha):
#     S = []
#     while S=(s1,...,si) com i < n do:
#         entre todos candidatos C para si+1:
#         forma a rcl com os alpha % melhores candidatos em C #Restricted Candidate List
#         escolhe aleatoriamente um s pertencente à rcl
#         S=(s1,...,si,s)
#     end while
#
# def grasp(s0,alpha):
#     solucao_atual = s0
#     do:
#         nova_solucao = greed_randomized_solution(alpha)
#         nova_solucao = busca_local(y)
#         if( f(nova_solucao) < f(solucao_atual)):
#             solucao_atual = nova_solucao
#     until a stop criterion is satisfied
#     return s
