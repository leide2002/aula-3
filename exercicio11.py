hora1= int (input("hora da primeira entrada:"))
hora2= int (input("hora da segunda entrada:"))

entrada1=3
seg1=0.45
entrada2=14
seg2=0.20

somahora = entrada2 + entrada1

somaminut = seg1 + seg2

if somahora >24:
    somahora= somahora - 24
    print("somahora")

if somaminut >=60:
    somaminut= somaminut + 1

    print(somahora, somaminut)