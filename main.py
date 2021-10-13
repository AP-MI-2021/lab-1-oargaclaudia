
def is_prime(n):
    if n<2:
      return False
    if n==2:
      return True
    for i in range(2,n//2+1):
      if n%i==0:
        return False
    return True
def test_is_prime():
    assert is_prime(2)==True
    assert is_prime(3)==True
    assert is_prime(4)==False
def get_cmmdc_v1(a,b):
    while a*b!=0:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a+b
def test_get_cmmdc_v1():
    assert get_cmmdc_v1(2,10)==2
    assert get_cmmdc_v1(3,9)==3
def get_cmmdc_v2(a,b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
             b = b - a
    return a
def test_get_cmmdc_v2():
    assert get_cmmdc_v2(10,20)==10
    assert get_cmmdc_v2(15,25)==5
def menu():
    print('1. Stabileste daca un numar este prim ')
    print('2. Sa se calculeze produsul a n numere ')
    print('3. Sa se calculeze cmmdc folosind prima metoda ')
    print('4. Sa se calculeze cmmdc folosind a doua metoda ')
    print('x. Exit')
def main():
    menu()
    while True:
        optiune = input('Dati optiunea de la utilizator: ')
        if optiune=='1':
            n=int(input('Dati numarul de la tastatura: '))
            if is_prime(n):
                print('DA')
            else:
                print('NU')
        elif optiune=='2':
            n=int(input('Dati numarul de numere: '))
            p=1
            for i in range(n):
                x=int(input('Dati numarul: '))
                p=p*x
            print(p)
        elif optiune=='3':
            a=int(input('Dati primul numar: '))
            b=int(input('Dati al doilea numar: '))
            print(get_cmmdc_v1(a,b))
        elif optiune=='4':
            a=int(input('Dati primul numar: '))
            b=int(input('Dati al doilea numar: '))
            print(get_cmmdc_v2(a,b))
        elif optiune=='x':
            break
        else:
            print('optiunea este gresita')
main()