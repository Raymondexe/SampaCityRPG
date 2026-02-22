import dice


def ataque_jogador(player, enemy):
    dado = dice.dado_random()
    print(f"🎲 Você tirou: {dado}")

    if dado <= 5:
        print("Você errou o ataque!")

    elif dado <= 10:
        dano = player["Dano"] * 0.5
        enemy["HP"] -= dano
        print("⚔️  Dano fraco:", dano)

    elif dado <= 15:
        dano = player["Dano"] * 0.75
        enemy["HP"] -= dano
        print("⚔️  Dano normal:", dano)

    elif dado <= 19:
        dano = player["Dano"] * 1.5
        enemy["HP"] -= dano
        print("💥  Ataque forte:", dano)

    else:  
        dano = player["Dano"] * 2
        enemy["HP"] -= dano
        print("🔥  CRÍTICO:", dano)

    print("❤️  HP do inimigo:", enemy["HP"])
         

def defender(player, enemy):
    danoRecebido = 0
    dado = dice.dado_random()

    if dado < 5:
        print("Você não conseguiu defender. Recebeu dano total")
        player["HP"] -= enemy["dano"]
        print("HP atual:", player["HP"])

    elif dado > 10 and dado <= 15:
        print("Você defendeu parcialmente, mas recebeu dano")
        danoRecebido = enemy["dano"] / 2
        player["HP"] -= danoRecebido
        print("Dano recebido:", danoRecebido)
        print("HP restante:", player["HP"])

    else:
        print("Parry perfeito! Você refletiu todo dano do inimigo")
        

                
def abrir_inventario(player):
    print("🎒 Abrindo inventário...")
    print(player["Inventario"])

    print("\n----------------------------------\n")

    if "Poção de cura" in player["Inventario"]:
        print("Você tem uma cura básica. Deseja usar?")
        print("1 - Usar cura")
        print("2 - Voltar")

        usar = int(input("Escolha: "))

        if usar == 1:
            player["HP"] += 15
            player["Inventario"].remove("Poção de cura")

            print("✨ Você usou a poção!")
            print("HP atual:", player["HP"])

        else:
            print("Você guardou a poção.")

    else:
        print("Seu inventário está vazio 😢")

    print("\n----------------------------------\n")