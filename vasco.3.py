nome = input("Qual é o seu nome?")
Temperatura = float(input("Qual é a temperatura de onde voce está?"))
if Temperatura >=20 and Temperatura <= 40:
    print(f"{nome} Onde tu está tá muitooo quenteeee")

elif Temperatura <=20 and Temperatura >= 5:
    print(f"{nome} Onde tu está tá muitooooo frioooo")
elif Temperatura <=5 and Temperatura >=0 :
    print(f"{nome} tá geladooooo pra caralhooo")
else:
    print(f"{nome} se vai morrerrrrrr se ferrrouuuu")
