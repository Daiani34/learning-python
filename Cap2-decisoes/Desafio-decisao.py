nivel_de_acesso = input("Digite seu nivel de acesso: ").upper()
genero = input("Qual seu gênero? ").upper()
if genero == "FEMININO" and nivel_de_acesso == "ADM":
    print("Olá administradora")
elif genero == "FEMININO" and nivel_de_acesso == "USER":
    print("Olá usuária")
elif genero == "FEMININO" and nivel_de_acesso == "GUEST":
    print("Olá convidada")
else:
    if nivel_de_acesso == "ADM":
        print("Olá administrador")
    elif nivel_de_acesso == "GUEST":
        print("Olá convidado")
    elif nivel_de_acesso == "USER":
        print("Olá usuário")
    else:
        print("Olá desconhecido (a)!")
