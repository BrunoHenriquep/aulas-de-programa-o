print(" m - masculino f - feminino")
sexo = input("digite seu sexo :")    

if sexo == "m" :
    altura = float(input("informe sua altura :"))
    if  altura >= 1.70 :
        print("voçê está apto")
    else: 
        print("voçê não está apto")
    
if sexo == "f" :
    altura = float(input("informe sua altura"))
    if altura >= 1.60 :
        print("voçê está apto")
    else :
        print("voçê não está apto")
    
else :
    print("sexo invalido")