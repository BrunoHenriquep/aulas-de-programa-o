opção = int(input("informe a opção :"))

match opção :
    case 1 :
        temperatura = float(input("informe a temperatura em celsius"))
        print("o valor de",temperatura, "é de",(temperatura * 9/5) + 32,"f")
    case 2 :
        temperatura = float(input("informe a temperatura em fahrenheit"))
        print("o valor de", temperatura, " é de",(temperatura - 32)* 5/9,"c")
    case _:
        print("opção invalida")