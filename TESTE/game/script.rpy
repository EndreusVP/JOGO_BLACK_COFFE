init python:
    #variaveis para medir pontuação de lados 
    little_demon = 0
    little_angel = 0

#redimencionamento de personagem
transform pequeno: 
    zoom 0.5

transform cima:
    xalign 0.5
    yalign 0.4

#movimentação do personagem
transform andar_frente:
    linear 3.0 zoom 0.3


#personagens irrelevantes
define bandido = Character("Marginal")

#personagens
define anjinho = Character("Anjinho")
define demoninho = Character("demoninho")
define player = Character("Player")
define pai_player = Character("Pai player")

#imagem personagens
image pai_player = "images/imagem_pai_player.png"

#imagem de ações
image assalto = "images/assalto.png"

#fundos
image fundo_teatro_end = im.Scale("images/fundo_teatro_end.png", 1920, 1080)
image fundo_teatro_peca = im.Scale("images/fundo_teatro_peça.png", 1920, 1080) 
image fundo_corredor_teatro = im.Scale("images/fundo_corredor_teatro.png", 1920,1080)
image fundo_beco = im.Scale("images/fundo_beco.png",1920, 1080)

#iniciar jogo
label  start:
    scene fundo_teatro_peca

    player "Achei que um teatro fosse mais chato"
    player "Mas tenho q admitir, o pai estava certo, da pra me divertir"

    scene fundo_teatro_end with fade

    pai_player "hora de ir, vamos filho."

    player "ok, pai"

    scene fundo_corredor_teatro with fade
#pai andando pra frente
    show pai_player at cima:
        pequeno
        andar_frente
    
    player "Voltar pra casa uma hora dessas, ainda bem que estou com meu pai"
    player "Sera que um dia vou ser corajoso igual a ele?"

    pai_player "Vamos logo, você anda muito devagar"

    player "Estou indo, pai"

    scene fundo_beco with dissolve

    show pai_player at center:
        zoom 0.6
        xalign 0.5
        yalign 0.6

    player "Essas ruas me dão medo"

    hide pai_player

    show assalto 

    player "HAN..."
    player "De onde ele veio???"
    player "PAAAAAAI"

    pai_player "calma filho, esta tudo bem"
    pai_player "..."

    demoninho "Ele esta mentindo, você sabe que nao esta tudo bem"

    anjinho "Seu pai não mentiria pra você, escute ele e tudo ocorrera bem"

    player "Que merda eh essa na minha cabeça?..."

    bandido "Anda logo... passa tudo, ou você vai parecer escorredor de macarrão"

    demoninho "HAHAHA... é melhor você fazer algo. Quer mesmo ver seu pai morrer?"

    anjinho "Não faça nenhuma besteira"

    pai_player "Eu te dou tudo o que quiser, só não faça nada com meu filho"