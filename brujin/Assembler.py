from random import shuffle
kmers = input().split(',')
print('kmers', len(kmers))
print('Final esperado', len(kmers)+ len(kmers[0])-1)

shuffle(kmers)

# Inicializando sufixo e prefixo
prefix = []
sufix = []

for kmer in kmers:
  # Indices: 0 = prefixo; 1 = Verificação se de passagem para criação de composition graph 
  prefix.append([kmer[:len(kmer)-1], False]) 
  sufix.append([kmer[1:], False])

# Encontrando inicio e fim
cont = 0
for idx, pre in enumerate(prefix):
  if sufix.count(pre) == 0:
    cont += 1
    start = kmers[idx]
if cont != 1:
  print("Tamanho de K insuficiente para encontrar inicio")
  exit()

cont = 0
for idx, suf in enumerate(sufix):
  if prefix.count(suf) == 0:
    cont +=1
    end = kmers[idx]
if cont != 1:
  print("Tamanho de K insuficiente para encontra final")
  exit()
print("Inicio =", start)
print("Fim =", end)

# print(kmers)

newPre = []
for i in prefix:
  if i not in newPre:
    newPre.append(i)
  else:
    newPre.append([i[0], True])
pre = newPre

# path graph + debrujin -> composition graph
arestas = {}
paresDeIndices = []
arestas[start[:-1]] =[[start[1:], False]]
verifySuf = sufix.copy()
for idxPre, pre in enumerate(prefix):
  for idxSuf, suf in enumerate(sufix):
    if pre[0] == suf[0] and idxPre != idxSuf and (not pre[1] and not suf[1]) and sufix not in verifySuf:
      if pre[0] in arestas.keys():
        arestas[pre[0]].append([kmers[idxPre][1:], False]) # 0 = vertice de destino; 1 = verificação de saída
      else:
        arestas[pre[0]] = [[kmers[idxPre][1:], False]]
      paresDeIndices.append([idxPre, idxSuf])
      pre[1] = True
      suf[1]
      verifySuf.remove(suf)
# print(sufix)
arestas[end[1:]] =[[start[:-1], False]]

# for key, value in arestas.items():
#   print(key, value)

# Formiguinha leo
def percorreArestas(start, grafo, listaDeVertices, caminhosPossiveis=[]):
  path = []
  while True:
    path.append(start)
    thereIsNoWay = True
    thereIsNewWay = False
    for destino in grafo[start]:
      if not destino[1]:
        start = destino[0]
        destino[1] = True
        thereIsNoWay = False
        thereIsNewWay = True
        break
    
    if thereIsNewWay:
      continue
    
    lifeGoesOn = False
    if thereIsNoWay:
      caminhosPossiveis.append(path)
      path = []
      # Passar para a proxima aresta com caminho livre
      for cam in caminhosPossiveis:
        for vertex in cam:
          for destino in grafo[vertex]:
            if not destino[1]:
              start = vertex
              lifeGoesOn = True
    if lifeGoesOn:
      continue
    return caminhosPossiveis

caminhos = percorreArestas(start[:-1], arestas, arestas.keys())

pathFinal = []

def remonta(caminhoAtual, idx = 0):
  global pathFinal
  global caminhos
  camAux = caminhoAtual.copy()
  for vertices in camAux:
    pathFinal.append(vertices[0])
    if idx + 1 < len(caminhos):
      if vertices in caminhos[idx+1][0]:
        # print('DEBUG', vertices, caminhos[idx + 1][0])
        # print('CAMINHOS:', caminhos)
        
        remonta(caminhos[idx+1][1:], idx + 1)
  caminhos.remove(caminhos[idx])
  
# print(caminhos)
remonta(caminhos[0])
pathFinal.pop()
for i in range(2, len(end)):
  pathFinal.append(end[i])

for i in pathFinal:
  print(i, end='')
print()
print('Tamanho final:', len(pathFinal))
pathFinal = []

























# pathFinal.append(caminhos[0][0])
# def remonta(caminhoAtual, caminhos, idx = 0):
#   global pathFinal
#   camAux = caminhoAtual.copy()
#   camAux.pop()
#   isDisturbed = False
#   for vertices in camAux:
#     pathFinal.append(vertices[0])
#     if idx + 1 < len(caminhos):
#       if vertices in caminhos[idx+1][0] and not isDisturbed:
#         print('DEBUG', vertices, caminhos[idx + 1][0])
#         # pathFinal.append(vertices[-1])
#         print('CAMINHOS:', caminhos)
#         remonta(caminhos[idx+1][:], caminhos, idx + 1)
#         isDisturbed = True

# remonta(caminhos[0][len(kmers[0][0]):], caminhos)
# # print(pathFinal)
# for i in pathFinal:
#   print(i, end='')
# print()
# print('Tamanho final:', len(pathFinal))
