n = [""]*10
tamanho = len(n)
maior = 0
menor = 0
for x in range(tamanho):
    n[x] = int(input("Digite seu numero: "))
for y in range(tamanho):
    if n [y] % 2==0:
        print(n[y], end ="")
for z in range(tamanho):
    if n[y] > maior:
      maior = n [y]
    if n[y] < menor:
      menor = n[y]

print(f"Contem{y} numeros pares. \n"
      f"O maior numero é: {maior}\n"
      f"O menor numero é: {menor}\n")