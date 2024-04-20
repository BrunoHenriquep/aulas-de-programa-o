quantidade_mangás = int(input("informe a quantidade: "))


acumulador = 0

for i in range(quantidade_mangás):
    valor_unitario = int(input("iforme o valor: "))
    acumulador = acumulador + valor_unitario
print("o valor total é :",acumulador)
print("a media de gastos é :",(acumulador/quantidade_mangás))