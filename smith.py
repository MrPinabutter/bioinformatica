seq1 = input("Digite a sequencia 1: ")
seq2 = input("Digite a sequencia 2: ")

mis = int(input("Mis: "))
match = int(input("Match: "))
gap = int(input("Gap: "))

score_list = []
for i in range(len(seq1)+1):
  row = []
  for j in range(len(seq2)+1):
    if i == 0:
      row.append(j*gap)
      continue
    if j == 0: 
      row.append(i*gap)
      continue    
    row.append(0)

  score_list.append(row)

backtrack = []
for i_idx, i in enumerate(seq1):
  backtrack_row = []
  for j_idx, j in enumerate(seq2):
    if i == j:
      aux = match
    else:
      aux = mis
    diag_score = score_list[i_idx][j_idx] + aux
    print("i =", i_idx, "j =", j_idx, "diag_score =", diag_score)
    
    vert_gap_score = score_list[i_idx][j_idx+1] + gap
    print("i =", i_idx, "j =", j_idx, "gap_score =",vert_gap_score)

    hor_gap_score = score_list[i_idx+1][j_idx] + gap
    print("i =", i_idx, "j =", j_idx, "gap_score =", hor_gap_score)

    max_score = max([diag_score, vert_gap_score, hor_gap_score])

    if diag_score == max_score:
      backtrack_row.append((i_idx-1, j_idx-1))
    elif vert_gap_score == max_score:
      backtrack_row.append((i_idx-1, j_idx))
    elif hor_gap_score == max_score:
      backtrack_row.append((i_idx, j_idx-1))

    score_list[i_idx+1][j_idx+1] = max_score
  backtrack.append(backtrack_row)
print()
print('-'*35)
print('SCORES: ')

max_score = -float('inf')
max_indice = 0
for i in range(len(score_list) -1, 0, -1):
  if max_score < max(score_list[i][1:]):
    max_score = max(score_list[i][1:])
    max_indice = (i-1, score_list[i][1:].index(max_score))
  print(score_list[i][1:])
print('-'*35)

print('Score:', score_list[len(backtrack)] [len(backtrack[0])])
print('Indice do score:', (len(backtrack)-1,len(backtrack[0])-1))
print('-'*35)
print('Max Score:', max_score)
print('Indice do score maximo:', max_indice)
print('-'*35)
seqCorrigida1 = ''
seqCorrigida2 = ''

# posição mais alta da matriz  
aux = (len(backtrack)-1, len(backtrack[0])-1)

while(True):
  aux1 = aux
  aux = backtrack[aux1[0]][aux1[1]]

  if aux1[0] < 0:
    for i in range(aux1[1], -1, -1):
      print(i)
      seqCorrigida1 += '-'
      seqCorrigida2 += seq2[i]
    break      

  if aux1[1] < 0:
    for i in range(aux1[0], -1, -1):
      print(i)
      seqCorrigida1 += seq1[i]
      seqCorrigida2 += '-'
    break

  if aux[0] == aux1[0]:               # Voltou na horizintal
    seqCorrigida1 += '-'
    seqCorrigida2 += seq2[aux1[1]]
  elif aux[1] == aux1[1]:             # Voltou na vertical
    seqCorrigida1 += seq1[aux1[0]]
    seqCorrigida2 += '-'
  else:                               # Voltou na diagonal
    seqCorrigida1 += seq1[aux1[0]]
    seqCorrigida2 += seq2[aux1[1]]
  
  if aux1 == (-1, -1):
    break

print("Sequencia 1 gerada:", seqCorrigida1[len(seqCorrigida1)::-1])
print("Sequencia 2 gerada:", seqCorrigida2[len(seqCorrigida1)::-1])

# Score a partir do máximo
aux = (max_indice[0], max_indice[1])
seqCorrigida1 = ''
seqCorrigida2 = ''

while(True):
  aux1 = aux
  aux = backtrack[aux1[0]][aux1[1]]

  if aux1[0] < 0:
    for i in range(aux1[1], -1, -1):
      print(i)
      seqCorrigida1 += '-'
      seqCorrigida2 += seq2[i]
    break      

  if aux1[1] < 0:
    for i in range(aux1[0], -1, -1):
      print(i)
      seqCorrigida1 += seq1[i]
      seqCorrigida2 += '-'
    break

  if aux[0] == aux1[0]:               # Voltou na horizintal
    seqCorrigida1 += '-'
    seqCorrigida2 += seq2[aux1[1]]
  elif aux[1] == aux1[1]:             # Voltou na vertical
    seqCorrigida1 += seq1[aux1[0]]
    seqCorrigida2 += '-'
  else:                               # Voltou na diagonal
    seqCorrigida1 += seq1[aux1[0]]
    seqCorrigida2 += seq2[aux1[1]]
  
  if aux1 == (-1, -1):
    break

print('-'*35)
print("Sequencia do score máximo 1 gerada:", seqCorrigida1[len(seqCorrigida1)::-1])
print("Sequencia do score máximo 2 gerada:", seqCorrigida2[len(seqCorrigida1)::-1])

# print(backtrack)
# print(score_list)