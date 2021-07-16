k = input()
seq = input()

k = int(k.replace('k=', ''))

kmers = ''
for i in range(0, len(seq)-k+1):
  kmers += seq[i: i+k] + ','

arquivo = open(f'k{k}mer.txt', "w")
arquivo.write(kmers[:len(kmers)-1])