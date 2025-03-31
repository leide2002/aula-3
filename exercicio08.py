#time de futebol
time1 = input("time um:")
time2 = input("time 2:")
gols1 = int(input("quantos gols time um fez:"))
gols2 = int(input ("quantos gols time dois fez:" ))

if gols1>gols2:
    print (f"se for o gols do {time1}, for maior que o {time2}, esta aprovado:")

else:
    if(gols2>gols1):
        print(f"se o gols do {time1}, for igual que o do {time2}, e empate:")
    else:
        print("empate")
