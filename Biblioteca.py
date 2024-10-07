def piramide(n):
    for i in range(1,n+1):
        for x in range(i):
             print(i,end = "")
        print()


def piramide2(n):
    for x in range(1,n+1):
     for y in range(1,x+1):
        print(y,end="")
    print()

def vogais(texto):
    cont=0
    for x in texto:
        if x in "AEIOUaeiou":
            cont=+1
    print(f"O texto digitado possui{cont}:")
