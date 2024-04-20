nome = input("diga seu nome: ")
idade = int(input("digite sua idade: "))
salario = float(input("diga seu salario: "))
sexo = input("diga seu sexo: ")
estado_civil = input("informe seu estado civil: ")

while len (nome) <= 3:
    nome = input("diga seu nome: ")
    
while len (idade < 0) or (idade > 150):
    idade = int(input("digite sua idade: "))

while len(salario) > 0:
    salario = float(input("diga seu salario: "))

while len(sexo!= "m") and (sexo!= "f"):
    sexo = input("diga seu sexo: ")
    
while len (estado_civil!= "s") and (estado_civil!= "c") and (estado_civil!="v" ) and (estado_civil!= "d"):
    estado_civil = input("informe seu estado civil: ")
    