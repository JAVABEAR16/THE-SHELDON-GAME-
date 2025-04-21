print()
IDIOMA = int(input("Which Language do you prefer, Portuguese (Press 1) or English (Press 2) ?\n\nQual idioma você prefere, Português (Pressione 1) ou Inglês (Pressione 2) ? "))
if IDIOMA == 1:
    print()
    print(40*"-")
    print("O Julgamento dos Quatro Portões 🏰".center(40))
    print(40*"-")
    print()
    Nome = input("Saudações! Qual é o seu nome, jovem? ")
    print()
    print(f"É um prazer, {Nome}! Você é um(a) aventureiro(a) tentando atravessar um castelo encantado!\nResponda as perguntas corretamente, e passe pelos QUATRO PORTÕES DO DRAGÃO SHELDON 🐲")
    print()
    Idade = int(input(f"Qual a sua idade, {Nome}? "))
    print()
    Energia = int(input("E quanto a sua energia? Medimos esse nível através da métrica Chi, onde o potencial máximo humano é de 100... "))
    print()
    if Energia > 100:
        print("Apocalipse 21:8. Sua energia será considerada nula!")
        Energia == 0
    elif Energia >= 80:
        print("Nossa, sua energia é fascinante!")
    elif Energia < 50:
        print("Uau, faz um bom tempo que não vejo alguém tão fraco...")
    else:
        print("Huuum, um nível decente...")
    print()
    Classe = int(input("E qual a sua classe? Guerreiro (Pressione 1), Mago (Pressione 2), Ladino (Pressione 3), ou Clérigo (Pressione 4)? "))
    print()
    if Classe == 1:
        print("Hah, então você é da classe \"Guerreiro\"! Pegue essa espada 🗡️")
    elif Classe == 2:
        print("Hah, então você é da classe \"Mago\"! Pegue essa bola de cristal 🔮")
    elif Classe == 3:
        print("Hah, então você é da classe \"Ladino\"! Pegue essa faca 🪒")
    elif Classe == 4:
        print("Hah, então você é da classe \"Clérigo\"! Pegue esse rosário 📿")
    else:
        Classe == 0
        print("Ah, esquece! Você tem cara de vagabundo(a)...")
    print()
    Poção = int(input("Você está com poções? Sim (pressione 1), ou Não (pressione 2)? "))
    print()
    if Poção == 1:
        print("Certo. Esperto de sua parte.")
    elif Poção == 2:
        print("Huuum...Arriscado de sua parte.")
    else:
        print("Ah, fala sério, você nem está com uma mochila 🎒")
    print()
    Maldição = int(input("Você está amaldiçoado? Sim (pressione 1), ou Não (pressione 2)? "))
    print()
    if Maldição == 2:
        print("Ufa, que bom...")
    elif Maldição == 1:
        print("Uou, uou, uou... Fique longe!")
    else:
        print("Talvez a sua própria existência seja sua maior maldição...")
    print()
    Acompanhante = int(input("Você está acompanhado? Sim (pressione 1), ou Não (pressione 2)? "))
    print()
    if Acompanhante == 1:
        print("Nossa, como eu não te vi antes? Mas que Xuxuzinho!")
    elif Acompanhante == 2:
        print("Antes sozinho que mal-acompanhado...")
    else:
        print("Esquece, talvez você valha por dois...")
    print()
    print("Agora, vejamos...")
    print()
    # PORTÃO UM 🌀 (MATURIDADE)
    if Idade >= 15:
        print("Você passou pelo Portão Um, da Maturidade 🌀")
        print()
        # PORTÃO DOIS 🔥 (VONTADE)
        if Poção == 1 or Energia >= 40:
            print("Você passou pelo Portão Dois, da Vontade 🔥")
            print()
            # PORTÃO TRÊS 🧠 (ALMA PURA)
            if Maldição == 1 and Classe == 2 or Acompanhante == 1 or Maldição == 2:
                print("Você passou pelo Portão Três, da Alma pura 🧠")
                print()
                # PORTÃO QUATRO ⚔️ (VALOR)
                if Classe == 1 or Classe == 2 and Poção == 1 and Maldição == 2 or Classe == 3 and Energia >= 50 or Classe == 4 and Maldição == 2:
                    print("Você passou pelo Portão Quatro, do Valor ⚔️")
                    print()
                    print("Parabéns! Você conseguiu passar por todos os QUATRO PORTÕES DO DRAGÃO SHELDON 🐲")
                    print()
                else:
                    print("DO PORTÃO QUATRO...VOCÊ NÃO PASSARÁ!!!")
                    print()
            else:
                print("DO PORTÃO UM...VOCÊ NÃO PASSARÁ!!!")
                print()
        else:
            print("DO PORTÃO DOIS...VOCÊ NÃO PASSARÁ!!!")
            print()
    else:
        print("DO PORTÃO TRÊS...VOCÊ NÃO PASSARÁ!!!")
        print()
elif IDIOMA == 2:
    print()
    print(40*"-")
    print("The Trial of the Four Gates 🏰".center(40))
    print(40*"-")
    print()
    Name = input("Greetings! What is your name, young one? ")
    print()
    print(f"Nice to meet you, {Name}! You are an adventurer trying to pass through an enchanted castle!\nAnswer the questions correctly, and pass through the FOUR GATES OF THE DRAGON SHELDON 🐲")
    print()
    Age = int(input(f"How old are you, {Name}? "))
    print()
    Energy = int(input("And how about your energy? We measure this level through the Chi metric, where the maximum human potential is 100... "))
    print()
    if Energy > 100:
        print("Revelation 21:8. Your energy shall be considered null!")
        Energy == 0
    elif Energy >= 80:
        print("Wow, your energy is fascinating!")
    elif Energy < 50:
        print("Whoa, it's been a while since I've seen someone so weak...")
    else:
        print("Hmmm, a decent level...")
    print()
    Class = int(input("And what's your class? Warrior (Press 1), Mage (Press 2), Rogue (Press 3), or Cleric (Press 4)? "))
    print()
    if Class == 1:
        print("Hah, so you're a \"Warrior\"! Take this sword 🗡️")
    elif Class == 2:
        print("Hah, so you're a \"Mage\"! Take this crystal ball 🔮")
    elif Class == 3:
        print("Hah, so you're a \"Rogue\"! Take this dagger 🪒")
    elif Class == 4:
        print("Hah, so you're a \"Cleric\"! Take this rosary 📿")
    else:
        Class == 0
        print("Ah, forget it! You look like a bum...")
    print()
    Potion = int(input("Do you have potions with you? Yes (press 1), or No (press 2)? "))
    print()
    if Potion == 1:
        print("Alright. Smart move.")
    elif Potion == 2:
        print("Hmm... A risky choice.")
    else:
        print("Oh, come on, you don't even have a backpack 🎒")
    print()
    Curse = int(input("Are you cursed? Yes (press 1), or No (press 2)? "))
    print()
    if Curse == 2:
        print("Phew, good to hear...")
    elif Curse == 1:
        print("Whoa, whoa, whoa... Stay away!")
    else:
        print("Maybe your very existence is your greatest curse...")
    print()
    Companion = int(input("Are you accompanied? Yes (press 1), or No (press 2)? "))
    print()
    if Companion == 1:
        print("Wow, how did I not notice before? What a cutie!")
    elif Companion == 2:
        print("Better alone than in bad company...")
    else:
        print("Forget it, maybe you're worth two...")
    print()
    print("Now, let's see...")
    print()
    # GATE ONE 🌀 (MATURITY)
    if Age >= 15:
        print("You passed through Gate One, of Maturity 🌀")
        print()
        # GATE TWO 🔥 (WILL)
        if Potion == 1 or Energy >= 40:
            print("You passed through Gate Two, of Will 🔥")
            print()
            # GATE THREE 🧠 (PURE SOUL)
            if Curse == 1 and Class == 2 or Companion == 1 or Curse == 2:
                print("You passed through Gate Three, of Pure Soul 🧠")
                print()
                # GATE FOUR ⚔️ (VALOR)
                if Class == 1 or Class == 2 and Potion == 1 and Curse == 2 or Class == 3 and Energy >= 50 or Class == 4 and Curse == 2:
                    print("You passed through Gate Four, of Valor ⚔️")
                    print()
                    print("Congratulations! You passed through all FOUR GATES OF THE DRAGON SHELDON 🐲")
                    print()
                else:
                    print("THROUGH GATE FOUR... YOU SHALL NOT PASS!!!")
                    print()
            else:
                print("THROUGH GATE ONE... YOU SHALL NOT PASS!!!")
                print()
        else:
            print("THROUGH GATE TWO... YOU SHALL NOT PASS!!!")
            print()
    else:
        print("THROUGH GATE THREE... YOU SHALL NOT PASS!!!")
        print()
else:
    print()
    print("LOL, I'M SO FUNNY BRO, I TRIED TO BROKEN THE CODE 😎")
    print()
        
# Code By Davi G. Luiz (JAVABEAR16)