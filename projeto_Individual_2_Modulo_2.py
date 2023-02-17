
cand = dict()


def cad():
    sair = "n"
    while sair != "s":
        #cand = dict()
        nome = input("Digite seu nome: ").lower()
        carta = input("Digite sua apresentação: ").lower()
        #cand: dict(nome, carta) = dict()
        cand[nome] = (carta)
        sair = input("Deseja sair? s ou n: ")


def imp():
    print("-"*50)
    #print(f"O Candidato {cad.keys()} tem a caracteristica {cad.values()}.")
    print(f"{cand}")
    print("-" * 50)

def busca():
    #vaga1 = ("python" and "desenvolvedor" and "programador")
    #vaga2 = ("analise de dados" and "dados" and "sql")
    for palavra in cand.items():
        if "python" or "desenvolvedor" or "programador" in palavra:
            print(f"{palavra} atende vaga1")
        elif "analise de dados" or "dados" or "sql" in palavra:
            print(f"{palavra} atende vaga2")
        else:
            print(f"{palavra} não atende as vagas.")


cad()
imp()
busca()
