nome_de_usuario = input("digite seu nome de usuario: ")
senha = input("digite sua senha: ")

while nome_de_usuario == senha:
    print("senha igual ao nome de usuario, digite novamente:")
    senha = input("digite sua senha: ")
print("bem vindo!")