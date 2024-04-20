lado_1 = float(input("informe o tamanho do lado :"))
lado_2 = float(input("informe o tamanho do lado :"))
lado_3 = float(input("informe o tamanho do lado :"))

if lado_1 == lado_2 == lado_3 :
    print("triângulo equilatero")
    
elif lado_1 != lado_2 != lado_3:
    print("triângulo escaleno")
    
else :
    print("isósceles")

