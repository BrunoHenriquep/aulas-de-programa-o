dia = int(input(" informe o dia :"))

match dia: 
    case 1:
        print("domingo")
    case 2:
        print("segunda-feira")
    case 3:
        print("terça-feira")
    case 4:
        print("quarta")
    case 5:
        print("quinta")
    case 6:
        print("sexta")
    case 7:
        print("sabado")
        
    case _:
        print("opção invalida")