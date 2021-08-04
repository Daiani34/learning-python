nome = input(" Digite o nome do paciente: ")
idade = int(input(" Digite a idade: "))
doenca_infectocontagiosa = input(" O paciente tem sintomas de doenças infectocontagiosas?").upper()
if doenca_infectocontagiosa == "SIM":
    print(" Encaminhe o paciente para sala amarela ")
elif doenca_infectocontagiosa == "NAO":
    print(" Encaminhe o paciente para a sala branca")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
if idade >= 65:
    print("Paciente COM prioridade ")
else:
    genero = input("Qual o gênero do paciente? ").upper()
    if genero=="FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida?").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
