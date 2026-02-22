import dice
import enemyIA
import battle

while True:
     
    print("Seja bem-vindo(a) ao RPG em python (em texto).")
    print("1 - Começar um novo jogo")
    print("2 - Sair")

    choice = int(input("Digite a sua decisão: "))

    if choice == 1:
        print("Vamos começar uma nova campanha\n")

        nomePlayer = input("Qual será o nome do seu personagem? ")

        player = {
            "nome": nomePlayer,
            "level": 1,
            "HP": 100,
            "Dano": 5,
            "Dinheiro": 0,
            "Inventario": ["Poção de cura"]
        }

        print("\nAgora escolha sua classe:")
        print("1 - Guerreiro")
        print("2 - Mago")
        print("3 - Arqueiro")

        escolha = int(input("Digite o número da classe desejada: "))

        if escolha == 1:
            player["Dano"] += 20
            classe = "Guerreiro"
        elif escolha == 2:
            player["Dano"] += 15
            classe = "Mago"
        else:
            player["Dano"] += 10
            classe = "Arqueiro"

        print(f"\nParabéns {player['nome']}! Você escolheu {classe}!")

        print("\nVamos treinar contra um Goblin!")

        enemy = {
            "nome": "Nikogoblin",
            "dano": 8,
            "HP": 50
        }

        print("\n⚔️ A batalha começou!")

        
        while player["HP"] > 0 and enemy["HP"] > 0:

            print("\n----------------------------------")
            print(player["nome"], "você pode tomar 3 decisões")
            print("1 - Atacar ⚔️")
            print("2 - Defender 🛡️")
            print("3 - Abrir inventário 🎒")

            acao = int(input("O que fará? "))

            print("\n----------------------------------")

            

            if acao == 1:
                battle.ataque_jogador(player, enemy)

            elif acao == 2:
                battle.defender(player, enemy)

            elif acao == 3:
                battle.abrir_inventario(player)

            else:
                print("Não há essa opção.")
                continue

            
            if enemy["HP"] <= 0:
                print("O inimigo morreu! Você venceu! ✨")
                player["level"] += 1
                print("Seu nível agora é:", player["level"])
                break

            
            enemyIA.turno_inimigo_simples(enemy, player)

            if player["HP"] <= 0:
                print("Você morreu... 💀")
                break

        print("\n----------------------------------")
        print("Fim da batalha!")
        print("----------------------------------")

        break

    elif choice == 2:
        print("Saindo do jogo...")
        break

    else:
        print("Opção inválida!")