
def piramide(n):
    for i in range(1,n+1):
        for x in range(i):
             print(i,end = "")
        print()
n = int(input("Digite seu numero:"))
piramide(n)