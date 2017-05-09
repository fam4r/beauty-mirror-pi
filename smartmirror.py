#################################################
#
# Author: FabLab Romagna by Nicolas Farabegoli - Fabrizio Margotta
# Version: 0.6
#
#   TODO:
#       - check uscita prima di stampare la scritta (o multi-threading)
#       - liste (vettori non esistono in python?)
#       - liste su file
#       - storie
#       - OK font
#       - "favicon"
#
#
#################################################

#Comando per caricare la libreria pygame
import pygame
import random
import RPi.GPIO as GPIO
from time import sleep
from sys import exit

print("\t\tWelcome to Smart Mirror Project by FabLab Romagna")
print("Please exit with ESC or ALT+F4 or CTRL+C")

portaLed = 27
portaPIR = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(portaPIR, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(portaLed, GPIO.OUT)         #LED output pin

#Comando per le operazioni preparatorie
stop = False

#Comando per far partire la libreria grafica
pygame.init()

#print pygame.font.match_font('')

#Comando per la creazione della finestra grafica
#finestra = pygame.display.set_mode([1366, 768], pygame.FULLSCREEN)
################################################################################## SOLO PER TEST
finestra = pygame.display.set_mode([800,600])

# Ricavo altezza e larghezza finestra
screen_w = pygame.display.Info().current_w
screen_h = pygame.display.Info().current_h

# Setting up program icon BEFORE program caption (see later)
# It seems it needs a Surface Object...
#pygame.display.set_icon(pygame.Surface((32, 32), flags=0, depth=0, masks=None))

#Comando per scrivere un messaggio nella barra della finestra
pygame.display.set_caption("Smart Mirror")

pygame.font.init()

# Loading local font
font = pygame.font.Font("OpenSans-Light.ttf", 100)

# Loading texts
# vett = [
#     ["Intro1", "Text1_1", "Text1_2", "Text1_3"],
#     ["Intro2", "Text2_1", "Text2_2", "Text2_3"]
# ]
vett = [ "Guarda con attenzione",
         "",
         "Non cercare",
         "altrove",
         "Fai vibrare le",
         "corde del cuore",
         "Tu sei reale e",
         "specchio di armonia",
         "Sei involucro",
         "di bellezza",
         "Puoi naufragar dolcemente",
         "in questo mare!"
]

def getRand(myList):
    random.seed()
    rand = random.randrange(0, len(vett))
    if ((rand % 2)):
        rand -= 1
    return rand

# Print text in the center of the screen
def printText(vett):
    num = getRand(vett)
    text = font.render(vett[num], True, (255,255,255))
    text2 = font.render(vett[num + 1], True, (255,255,255))

    # TODO: We can use font.Font.size()
    text_rect = text.get_rect()
    text_rect_w = text_rect.width
    text_rect_h = text_rect.height

    text2_rect = text2.get_rect()
    text2_rect_w = text2_rect.width
    text2_rect_h = text2_rect.height + text_rect_h

    finestra.blit(text, (screen_w / 2 - text_rect_w / 2, screen_h /2 - text_rect_h / 2))
    finestra.blit(text2, (screen_w / 2 - text2_rect_w / 2, screen_h /2 + text_rect_h / 2))

    # DO NOT REMOVE THIS
    pygame.display.update()

def printPhrase():
    # We want to print a random
    for elem in vett[getRand(vett)]:
        print (elem)
        finestra.fill(pygame.Color("black")) # erases the entire screen surface
        printText(elem)
        sleep(1)

# Inizio del ciclo di gestione del gioco (GAME LOOP)
while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE] or (keys[pygame.K_LALT] and keys[pygame.K_F4]) or (keys[pygame.K_LCTRL] and keys[pygame.K_c])):
            # Comando per chiudere la libreria grafica
            pygame.quit()
            exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE or event.key == pygame.K_LALT and event.key == pygame

    finestra.fill(pygame.Color("black")) # erases the entire screen surface

    # Getting PIR sensor data
    i=GPIO.input(portaPIR)
    if i==0:                 #When output from motion sensor is LOW
         print("No intruders",i)
         #GPIO.output(portaLed, 0)  #Turn OFF LED
         sleep(0.1)
    if i==1:               #When output from motion sensor is HIGH
        print("Intruder detected",i)
        #GPIO.output(portaLed, 1)  #Turn ON LED
        #printPhrase()
        printText(vett)
        sleep(0.1)
        sleep(2)


    pygame.display.flip()
