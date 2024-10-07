nome = [""]*5
senha = [""]*5
tamanho = len(nome)
for x in range(tamanho):
  nome[x]=input("Digite seu nome:")
  senha[x] = int(input("Digite sua senha:"))
for y in range(tamanho):
   print(f"posição:{y},{nome[y]},{senha[y]}")
