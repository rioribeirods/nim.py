def partida():
    modo_de_jogo = int(input("Bem-vindo ao jogo do NIM! Escolha: \n1 - para jogar uma partida isolada \n2 - para jogar um campeonato\n"))
    if modo_de_jogo == 1:
        print("\nVocê escolheu partida isolada ")
    elif modo_de_jogo == 2:
        print("\nVocê escolheu campeonato! ")
        return modo_de_jogo
    else:
        print("Escolha inválida")
    return modo_de_jogo

def computador_escolhe_jogada(n, m):
    print("Vez do computador!")
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        return m

def quem_comeca(n, m):
    if n % (m+1) == 0:
        print(" \nVocê começa \n")
        return 0
    else:
        print("O computador começa! \n")
        return 1

def usuario_escolhe_jogada(b, c):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada < 1 or jogada > c:
        print("Quantidade inválida")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def main():
    a = partida()
    if a == 1:
        b = int(input("\nQuantas peças? "))
        c = int(input("Limite de peças por jogada? "))
        while c >= b:
            print("Limite inválido!")
            c = int(input("Limite de peças por jogada? "))
        teste = quem_comeca(b, c)
        if b % (c+1) == 0: is_computer_turn = False
        if teste == 0:
            while b > 0:
                jogada = usuario_escolhe_jogada(b, c)
                b = b - jogada
                is_computer_turn = False
                print(f"O jogador tirou {jogada} peças")
                if b == 0: break
                jogada = computador_escolhe_jogada(b, c)
                b = b - jogada
                is_computer_turn = True
                print(f"O computador tirou {jogada} peças")
                if b == 0: break
        elif teste == 1:
            while b > 0:
                jogada = computador_escolhe_jogada(b, c)
                b = b - jogada
                is_computer_turn = True
                print(f"O computador tirou {jogada} peças")
                if b == 0: break
                jogada = usuario_escolhe_jogada(b, c)
                b = b - jogada
                is_computer_turn = False
                print(f"O jogador tirou {jogada} peças")
                if b == 0: break
        if is_computer_turn == False:
                print("Você venceu! Fim do jogo.")
        else:
            print("O computador venceu! Fim do jogo.")
    else:
        rodadas = 1
        computador = 0
        usuario = 0
        while rodadas < 4:
            print(f"\n*** Rodada {rodadas} *** \n")
            b = int(input("Quantas peças? "))
            c = int(input("Limite de peças por jogada? "))
            if b % (c+1) == 0: is_computer_turn = False
            while c >= b:
                print("Limite inválido!")
                c = int(input("Limite de peças por jogada? "))
            teste = quem_comeca(b, c)
            if teste == 0:
                while b > 0:
                    jogada = usuario_escolhe_jogada(b, c)
                    b = b - jogada
                    is_computer_turn = False
                    print(f"O jogador tirou {jogada} peças")
                    if b == 0: break
                    jogada = computador_escolhe_jogada(b, c)
                    b = b - jogada
                    is_computer_turn = True
                    print(f"O computador tirou {jogada} peças")
                    if b == 0: break
                if is_computer_turn == False:
                    usuario = usuario + 1
                    print("Você venceu! Fim do jogo.")
                else:
                    computador = computador + 1
                    print("O computador venceu! Fim do jogo.")
            elif teste == 1:
                while b > 0:
                    jogada = computador_escolhe_jogada(b, c)
                    b = b - jogada
                    is_computer_turn = True
                    print(f"O computador tirou {jogada} peças")
                    if b == 0: break
                    jogada = usuario_escolhe_jogada(b, c)
                    b = b - jogada
                    is_computer_turn = False
                    print(f"O jogador tirou {jogada} peças")
                    if b == 0: break
                if is_computer_turn == False:
                    usuario = usuario + 1
                    print("Você venceu! Fim do jogo.")
                else:
                    computador = computador + 1
                    print("O computador venceu! Fim do jogo.")
            rodadas += 1
        print("*** Final do campeonato *** \n")
        print(f"Placar: Você {usuario} x {computador} Computador")



main()