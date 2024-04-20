turno = input("digite o turno  :")

match turno :
    case "m":
        print("bom dia!")
    case "v" :
        print("boa tarde!")
    case "n" :
        ("boa noite!")
    case _:
      print("opção invalida") 