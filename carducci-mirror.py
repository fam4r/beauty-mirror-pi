#################################################
#
# Carducci-Mirror
#
# Author:
#   Fabrizio Margotta - Nicolas Farabegoli
#       for FabLab Romagna
# Version: 0.6
#
#################################################

import pygame
import random
import RPi.GPIO as GPIO
from time import sleep
from sys import exit

print("\t\tWelcome to Smart Mirror Project by FabLab Romagna")
print("Please exit with ESC or ALT+F4 or CTRL+C")

#ledPort = 27
pirPort = 17

# Raspberry GPIO initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPort, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(ledPort, GPIO.OUT)         #LED output pin

#Comando per le operazioni preparatorie
stop = False

#Comando per far partire la libreria grafica
pygame.init()

#print pygame.font.match_font('')

#Comando per la creazione della myWindow grafica
#myWindow = pygame.display.set_mode([1366, 768], pygame.FULLSCREEN)
################################################################################## SOLO PER TEST
myWindow = pygame.display.set_mode([800,600])

# Ricavo altezza e larghezza myWindow
screen_w = pygame.display.Info().current_w
screen_h = pygame.display.Info().current_h

# Setting up program icon BEFORE program caption (see later)
# It seems it needs a Surface Object...
#pygame.display.set_icon(pygame.Surface((32, 32), flags=0, depth=0, masks=None))

#Comando per scrivere un messaggio nella barra della myWindow
pygame.display.set_caption("Smart Mirror")

# Useless with pygame.init() -> http://www.pygame.org/docs/ref/font.html#pygame.font.init
pygame.font.init()

# Loading local font
font = pygame.font.Font("fonts/OpenSans-Light.ttf", 100)

# Loading texts (two objects displayed)
# Blank line -> one object displayed
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
    # Forcing odd random numer
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

    # Printing two lines of text, centered
    myWindow.blit(text, (screen_w / 2 - text_rect_w / 2, screen_h /2 - text_rect_h / 2))
    myWindow.blit(text2, (screen_w / 2 - text2_rect_w / 2, screen_h /2 + text_rect_h / 2))

    # DO NOT REMOVE THAT LINE
    pygame.display.update()

# Starting "Game Loop"
while True:

    # Detecting pressed keys to quit (ESC, ALT+F4, CTRL+C)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE] or (keys[pygame.K_LALT] and keys[pygame.K_F4]) or (keys[pygame.K_LCTRL] and keys[pygame.K_c])):
            # Comando per chiudere la libreria grafica
            pygame.quit()
            exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE or event.key == pygame.K_LALT and event.key == pygame

    # erases the entire screen surface
    myWindow.fill(pygame.Color("black"))

    # Getting PIR sensor data
    pirData=GPIO.input(pirPort)

    # sensor output -> LOW
    if pirData==0:
         print("No intruders",pirData)
         #GPIO.output(ledPort, 0)  #Turn OFF LED
         sleep(0.1)
    # sensor output -> HIGH
    if pirData==1:
        print("Intruder detected",pirData)
        #GPIO.output(ledPort, 1)  #Turn ON LED
        printText(vett)
        sleep(0.1)
        sleep(2)


    # Refreshing screen
    pygame.display.flip()
