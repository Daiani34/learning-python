nome = input("Digite o nome :")
idade = int(input(" Digite a idade: "))
doenca_infectocontagiosa = input(" Possui sintomas de doença infectocontagiosa? ")
if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print(" O paciente será direcionado a sala de espera amarela - COM PRIORIDADE ")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print(" O paciente será direcionado a sala de espera amrela - SEM PRIORIDADE")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print(" O paciente deve aguardar na sala de espera comum - COM PRIORIDADE")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print(" O paciente deve aguardar na sala de espera comum - SEM PRIORIDADE")
else:
    print(" Responda a pergunta de doenças infectocontagiosas com SIM ou NAO")
