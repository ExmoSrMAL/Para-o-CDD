cont = 0
soma = 0
notas = ["","","","",""]
tamanho = len(notas)
for x in range(tamanho):
  notas[x]=float(input("Digite sua nota:"))

for y in range(tamanho):
  soma += notas[y]
media = soma/tamanho

for i in range(tamanho):
   if notas[i]>=media:
    cont+=1
print(f"temos {cont} alunos com nota maior que a media{media}:")

