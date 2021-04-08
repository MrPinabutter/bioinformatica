from amino import aminos

rna_m = input().replace('.', '') # Remove o caractere .
start = False
for n in range(0, len(rna_m)-1, 3): # Pula 3 bases para formar as trincas
    trinca = rna_m[n:n+3]
    if 'Start' in aminos[trinca]:
        start = True
    if start:
        print(aminos[trinca])
        if 'Stop' in trinca:
            break