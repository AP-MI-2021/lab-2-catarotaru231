import math
def get_newton_sqrt(n,steps):
    a = float(n)
    for i in range(steps):
        n = 0.5 * (n + a / n)
    return n
def test_get_newton_sqrt():
    n = int(input("Numarul citit este: "))
    steps = int(input("Numarul de pasi este: "))
    print("Aproximarea obtinuta este:", get_newton_sqrt(n,steps))
def get_perfect_squares(x, y):
    if(x>y):
        a=x
        x=y
        y=a
    lst = []
    for i in range (x,y):
        if(math.sqrt(i) == int(math.sqrt(i))):
            lst.append(i)
    print("Numerele din intervalul", x, "si", y, "care sunt patrate perfecte sunt:")
    print (lst)
def test_get_perfect_squares():
    print("Capetele intervalului sunt")
    x=int(input())
    y=int(input())
    get_perfect_squares(x, y)
def main():
    P=int(input("Numarul problemei cerute este: "))
    if(P==4):
        test_get_newton_sqrt()
    elif(P==12):
        test_get_perfect_squares()
    else:
        print("Numerele problemelor cerute au fost 4 si 12")
main()
