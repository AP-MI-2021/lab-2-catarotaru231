import math
def get_newton_sqrt(n,steps):
    a = float(n)
    for i in range(steps):
        n = 0.5 * (n + a / n)
    return n
def newton_sqrt():
    n = int(input("Numarul citit este: "))
    steps = int(input("Numarul de pasi este: "))
    print("Aproximarea obtinuta este:", get_newton_sqrt(n, steps))
def test_get_newton_sqrt():
    pass
def perfect_squares():
    print("Capetele intervalului sunt")
    x = int(input())
    y = int(input())
    get_perfect_squares(x, y)
def get_perfect_squares(x, y):
    if(x>y):
        a=x
        x=y
        y=a
    lst = []
    for i in range (x,y+1):
        if(math.sqrt(i) == int(math.sqrt(i))):
            lst.append(i)
    print("Numerele din intervalul", x, "si", y, "care sunt patrate perfecte sunt:")
    print (lst)
def test_get_perfect_squares():
    pass

def show_menu():
    print("""
1.Execută un număr dat de pași pentru a calcula radicalul unui număr dat folosind metoda lui Newton cu `x0=2` și afișează aproximarea obținută.
2.Afișează toate pătratele perfecte dintr-un interval închis dat.
    """)

def main():
    while True:
        show_menu()
        P=input("Numarul problemei cerute este: ")
        if(P == '1'):
            newton_sqrt()
        elif(P == '2'):
            perfect_squares()
        elif(P == 'x'):
            print("Ati iesit din meniu.")
            break
        else:
            print("Comanda invalida. Reincearca")


main()