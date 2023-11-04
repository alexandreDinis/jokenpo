import random
import time
import pygame

pygame.mixer.init()
cont = "1"
negrito = "\033[1m"
cor_azul = "\033[94m"
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_reset = "\033[0m"
joquem = ["Pedra", "Papel", "Tesoura"]

while cont == "1":
    pygame.mixer.music.load("audios/8bit-music-for-game-68698.mp3")
    pygame.mixer.music.play()
    jogador = int(
        input(f'\nEscolha uma alternativa:\n{negrito}{cor_vermelha}Pedra [0] Papel [1] Tesoura [2] ->>{cor_reset} '))
    pygame.mixer.music.stop()
    print("=-" * 20)
    pygame.mixer.music.load("audios/boom-geomorphism-cinematic-trailer-sound-effects-123876.mp3")
    pygame.mixer.music.play()
    print(f'{negrito}{cor_amarela}J0')
    time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audios/boom-geomorphism-cinematic-trailer-sound-effects-123876.mp3")
    pygame.mixer.music.play()
    print("KEN")
    time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audios/boom-geomorphism-cinematic-trailer-sound-effects-123876.mp3")
    pygame.mixer.music.play()
    print(f'PO{cor_reset}\n')
    time.sleep(1)
    pygame.mixer.music.stop()
    cpu = random.randrange(0, 3)
    print("=-" * 20)
    pygame.mixer.music.load("audios/boom-geomorphism-cinematic-trailer-sound-effects-123876.mp3")
    pygame.mixer.music.play()
    print(f'{cor_verde}VOCE JOGOU = {cor_azul}{joquem[jogador]}')
    time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audios/boom-geomorphism-cinematic-trailer-sound-effects-123876.mp3")
    pygame.mixer.music.play()
    print(f'{cor_verde}CPU  JOGOU = {cor_azul}{joquem[cpu]}\n')
    time.sleep(1)
    pygame.mixer.music.stop()

    if cpu == 0:
        if jogador == 1:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}VOCE VENCEU!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()
        elif jogador == 2:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}CPU VENCEU!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}EMPATE!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()
    elif cpu == 1:
        if jogador == 0:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}CPU VENCEU!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()
        elif jogador == 2:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}VOCE VENCEU!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}EMPATE!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()
    elif cpu == 2:
        if jogador == 1:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}CPU VENCEU!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()
        elif jogador == 0:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}VOCE VENCEU!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load("audios/epic-hybrid-logo-157092.mp3")
            pygame.mixer.music.play()
            print(f'{negrito}{cor_azul}EMPATE!!!{cor_reset}')
            time.sleep(4)
            pygame.mixer.music.stop()

    print("=-" * 20)
    pygame.mixer.music.load("audios/Jellica - I tried to write some cutesy platformer kiddy nintendo shit.mp3")
    pygame.mixer.music.play()
    cont = input("Digiti [1] para jogar novamente ")
    pygame.mixer.music.stop()

