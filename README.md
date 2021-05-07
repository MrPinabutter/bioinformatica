# Comandos para executar o projeto
Para entrada e saída do programa enviamos podemos colocar da seguinte forma a baixo, o compilador ("python3" para linux e "py" para windows e apenas "python"):

- Linux
python3 smith.py < teste.fasta > saida.txt 

- Mac
python smith.py < teste.fasta > saida.txt 

- Windows 
py smith.py < teste.fasta > saida.txt 

# Arquivo de entrada de entrada (fasta)
O teste.fasta precisa ter a primeira e segunda linha as sequencias que serão lidas,
a terceira linha para o dismatch, a quarta para match e ultima para o gap, como pode se observar no 
exemplo teste.fasta ao lado

# Arquivo de saída 
O arquivo de saida é o saida.txt que apresenta os scores de cada célula (tanto horizontal,
como vertival e diagonal). Logo abaixo de todas elas é mostrado a lista de scores. E depois apresentado
o score global e máximo com sua respectiva localização na matriz. E por ultimo os alinhamentos,
as duas sequencias do global e em seguida as sequências a partir do maior score encontrado.
