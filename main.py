import math


def get_newton_sqrt(n, steps):
    a = float(n)
    for i in range(steps):
        n = 0.5 * (n + a / n)
    return n


def newton_sqrt():
    n = int(input("Numarul citit este: "))
    steps = int(input("Numarul de pasi este: "))
    print("Aproximarea obtinuta este:", get_newton_sqrt(n, steps))


def test_get_newton_sqrt():
    assert get_newton_sqrt(4, 100) == 2.0
    assert get_newton_sqrt(10, 10) == 3.162277660168379
    assert get_newton_sqrt(1,1) == 1.0

def perfect_squares():
    print("Capetele intervalului sunt")
    x = int(input())
    y = int(input())
    get_perfect_squares(x, y)
    print("Numerele din intervalul", x, "si", y, "care sunt patrate perfecte sunt:")
    print(get_perfect_squares(x,y))

def get_perfect_squares(x, y):
    if (x > y):
        a = x
        x = y
        y = a
    lst = []
    for i in range(x, y + 1):
        if (math.sqrt(i) == int(math.sqrt(i))):
            lst.append(i)
    return lst


def test_get_perfect_squares():
    assert get_perfect_squares(1,10) == [1,4,9]
    assert get_perfect_squares(2,3) == []
    assert get_perfect_squares(16,100) == [16,25,36,49,64,81,100]


def show_menu():
    print("""
1.Execută un număr dat de pași pentru a calcula radicalul unui număr dat folosind metoda lui Newton cu `x0=2` și afișează aproximarea obținută.
2.Afișează toate patratele perfecte dintr-un interval închis dat.
Apasati x pentru a iesi din meniu
    """)

test_get_newton_sqrt()
test_get_perfect_squares()
def main():
    while True:

        show_menu()
        P = input("Numarul problemei cerute este: ")
        if (P == '1'):
            newton_sqrt()
        elif (P == '2'):
            perfect_squares()
        elif (P == 'x'):
            print("Ati iesit din meniu.")
            break
        else:
            print("Comanda invalida. Reincearca")


main()
