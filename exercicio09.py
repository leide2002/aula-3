#Gazolina

valor = input ("escolha o combustivel que deseja, digite G se for gazolina e digite E se for estanol:")
litros= float(input("quantidade de litros:"))

gazolina = 5.80
etanol = 4.90


if valor == "g":
    precog = gazolina * litros
    print (f" o valor da gasolina e de {gazolina} o total deu {precog}" )

else:
    if valor == "e":
        precoe = etanol * litros
        print(f" o valor do {etanol} e o total deu{precoe}")

    else:
        print ("se a letra for incorreta vai dar erro:")