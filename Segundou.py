numero = [""]*10
tamanho = len(numero)
cont = 0
for x in range (tamanho):
  numero[x]=int(input("Digite seu numero: "))

p = int(input("Informe o numero para pesquisar: "))

for y in range(tamanho):
  if p == numero[y]:
    cont+=1
print(cont)
