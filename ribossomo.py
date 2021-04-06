from amino import aminos

rna_m = input().replace('.', '') # Remove o caractere .

for n in range(0, len(rna_m)-1, 3): # Pula 3 bases para formar as trincas
    trinca = rna_m[n:n+3]
    print(aminos[trinca]) 