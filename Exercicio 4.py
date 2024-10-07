a = [0,0,0,0,0,0,0,0,0,0]
x = 0
m = [0,0,0,0,0,0,0,0,0,0]
tamanho = len(a)
for y in range(tamanho):
    a[y]= int(input("Digite o numero:"))
x = int(input("Digite o multiplicador:"))
for i in range(tamanho):
    m[i]=a[i]*x
print(a)
print(x)
print(m)