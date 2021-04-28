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
    # print("i =", i_idx, "j =", j_idx, "diag_score =", diag_score, end=' ')
    
    vert_gap_score = score_list[i_idx][j_idx+1] + gap
    # print("i =", i_idx, "j =", j_idx, "gap_score =",vert_gap_score)

    hor_gap_score = score_list[i_idx+1][j_idx] + gap
    # print("i =", i_idx, "j =", j_idx, "gap_score =", hor_gap_score)

    max_score = max([diag_score, vert_gap_score, hor_gap_score])

    if diag_score == max_score:
      backtrack_row.append((i_idx-1, j_idx-1))
    elif vert_gap_score == max_score:
      backtrack_row.append((i_idx-1, j_idx))
    elif hor_gap_score == max_score:
      backtrack_row.append((i_idx, j_idx-1))

    score_list[i_idx+1][j_idx+1] = max_score
  backtrack.append(backtrack_row)

# print('score', score_list)
print('backtrack', backtrack)

seqCorrigida1 = ''
seqCorrigida2 = ''

# posição mais alta da matriz  
aux = (len(backtrack)-1, len(backtrack[0])-1)

while(True):
  aux1 = aux
  aux = backtrack[aux1[0]][aux1[1]]
  print('Aux', aux)
  print('Aux1', aux1)

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

# print(backtrack)
# print(score_list)