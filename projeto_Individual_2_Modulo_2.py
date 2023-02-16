
cand = dict()


def cad():
    sair = "n"
    while sair != "s":
        #cand = dict()
        nome = input("Digite seu nome: ")
        carta = input("Digite sua apresentação: ")
        cand: dict(nome, carta) = dict()
        cand.update()
    sair = input("Deseja sair? s ou n: ")


def imp():
    print("-"*50)
    #print(f"O Candidato {Nome} tem a caracteristica {Carta}.")
    print(f"{cand}")
    print("-" * 50)



cad()
imp()
print("-"*50)

vaga1 = ("python" + "desenvolvedor" + "programador")
vaga2 = ("analise de dados" + "dados" + "sql")
for palavra in cand.values():
    if vaga1 in palavra:
        print(f"vaga1: {palavra}")
    elif vaga2 in palavra:
        print(f"vaga2: {palavra}")
    else:
        print(f"não atende: {palavra}")


