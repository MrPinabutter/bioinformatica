dna = input()

rna = ''
for i in dna:
   if i == 'A': rna += 'U'
   if i == 'T': rna += 'A'
   if i == 'G': rna += 'C'
   if i == 'C': rna += 'G'
   if i == '.': rna += '.'
print(rna)