#nota_do aluno
nota1 = float (input("primeira nota:"))
nota2 = float (input("segunda nota:"))
nota3 = float (input("terceira nota:"))

media = (nota1 + nota1 + nota3)/3

if media <=4:
    print( f"reprovado")
else:
    if media >= 7:
        print(f"aprovado{media:.2f}")
    else:
        print("recuperaçao")




