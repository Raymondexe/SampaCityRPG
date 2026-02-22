
### IMPORTE ZONE 

print("\nSeja bem-vindo(a) ao projeto de login") 

usuario = {
    "email": "emailUser",
    "senha": "senhaUser"
}


def cadastrar_usuario():
    usuario["email"] = input("Insira o seu email: ")
    usuario["senha"] = input("Insira a sua senha: ")

    while usuario["email"] == "" or usuario["senha"] == "":
        print("Email ou senha vazios. Tente novamente")
        print("")
        print("---------------------")

        usuario["email"] = input("Insira o seu email: ")
        usuario["senha"] = input("Insira a sua senha: ")

    return usuario["email"], usuario["senha"]


usuario["email"], usuario["senha"] = cadastrar_usuario()


def login(email_cadastrado, senha_cadastrada):
    print("Vamos verificar suas informações")
    print("")
    print("---------------------")

    tentativas = 0

    while tentativas <= 3:
        email_cadastrado = input("Digite o seu email:")
        senha_cadastrada = input("Digite a sua senha:")

        if email_cadastrado == usuario["email"] and senha_cadastrada == usuario["senha"]:
            print("LOGIN REALIZADO")
            return

        else:
            print("Email ou senha incorretos")
            print("Número de tentativas restantes:", tentativas)
            tentativas += 1

    print("")
    print("---------------------")
    print("O número de tentativas foi excedido, tente novamente mais tarde")


login(usuario["email"], usuario["senha"])


