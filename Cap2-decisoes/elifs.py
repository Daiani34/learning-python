nome=input( " Digite o nome do paciente ")
idade=int(input(" Digite a idade: "))
doenca_infectocontagiosa=input( "Suspeitas de doenças infecto-contagiosas? ") .upper()
if idade>=65 :
    print( "O paciente " + nome + " possui atendimento prioritário ")
elif doenca_infectocontagiosa=="SIM":
    print( " O paciente " + nome + " deve aguardar na sala de espera reservada")
else:
    print (" O paciente " + nome + " não possui atendimento prioritário e pode aguardar na sala de espera comum")