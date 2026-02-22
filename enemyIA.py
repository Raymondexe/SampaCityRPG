import random

def turno_inimigo_simples(enemy, player):
    acao = random.choice(["ataque", "defesa", "habilidade"])

    print("\n👹 Turno do inimigo!")

    if acao == "ataque":
        dano = random.randint(5, enemy["dano"])
        player["HP"] -= dano
        print(f"{enemy['nome']} atacou e causou {dano} de dano!")

    elif acao == "defesa":
        print(f"{enemy['nome']} entrou em posição defensiva 🛡️")

    elif acao == "habilidade":
        dano = random.randint(enemy["dano"], enemy["dano"] + 10)
        player["HP"] -= dano
        print(f"{enemy['nome']} usou habilidade especial! 💥 {dano} de dano!")

    print("Seu HP agora é:", player["HP"])
    print("\n----------------------------------\n")