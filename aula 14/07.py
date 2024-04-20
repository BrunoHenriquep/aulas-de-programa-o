#crie um programa que leia 6 valores inteirose, em seguida, mostre os valores lidos na tela

valores =[]

for i in range(6):
    valores.append(int(input("digite 6 numeros: ")))
    
for i in range(6):
    print(valores[i])