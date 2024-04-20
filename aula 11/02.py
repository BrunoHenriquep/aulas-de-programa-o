nota = float(input("informe uma nota: "))

while nota <0 or nota>10:
    print("informe uma nota maior que e menor que 10")
    nota = float(input("informe uma nota: "))
print("nota inserida com sucesso!")