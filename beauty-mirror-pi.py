#################################################
#
# Beauty Mirror Pi
#
# Authors:
#   Fabrizio Margotta - Nicolas Farabegoli
#       for FabLab Romagna
# Version: 1.0
#
#################################################


print("Welcome to Beauty Mirror Pi by FabLab Romagna")
print("Please exit with ESC or ALT+F4 or CTRL+C")

import sys

if ('-h' in str(sys.argv) or '--help' in str(sys.argv)):
    print("Usage: python3 ./carducci-mirror.py [--nofullscreen]")
    print("\t-h, --help\t\tShow this help message and exit")
    print("\t--nofullscreen\t\tExecute program in window mode (800x600)")
    print("\t-d, --debug\t\tLow delay between texts")
    sys.exit()

import pygame
import random
try:
    import RPi.GPIO as GPIO
    rasp = True
except Exception as e:
    print("WARNING: Not running on a Raspberry...\n")
    rasp = False
from time import sleep

#ledPort = 27
pirPort = 17
pirData = 1
fontSize = 80
delayTime = 15

# Raspberry GPIO initialization
if rasp:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pirPort, GPIO.IN)         #Read output from PIR motion sensor
    #GPIO.setup(ledPort, GPIO.OUT)         #LED output pin

#Comando per le operazioni preparatorie
stop = False

#Comando per far partire la libreria grafica
pygame.init()

#print pygame.font.match_font('')

# Ricavo altezza e larghezza myWindow

#Comando per la creazione della myWindow grafica
if ('--nofullscreen' in str(sys.argv)):
    screen_w = 800
    screen_h = 600
    myWindow = pygame.display.set_mode([screen_w, screen_h])
else:
    screen_h = pygame.display.Info().current_h
    screen_w = pygame.display.Info().current_w
    myWindow = pygame.display.set_mode([screen_w, screen_h], pygame.FULLSCREEN)
    # Fullscreen mode -> no mouse pointer
    pygame.mouse.set_visible(False)

# Setting up program icon BEFORE program caption (see later)
# It seems it needs a Surface Object...
#pygame.display.set_icon(pygame.Surface((32, 32), flags=0, depth=0, masks=None))

#Comando per scrivere un messaggio nella barra della myWindow
pygame.display.set_caption("Beauty Mirror Pi by FabLab Romagna")

# Loading local font
font = pygame.font.Font("fonts/OpenSans-Light.ttf", fontSize)

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
    isQuitting()
    pygame.display.update()
    #pygame.display.flip()

def isQuitting():
    # Detecting pressed keys to quit (ESC, ALT+F4, CTRL+C)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE] or (keys[pygame.K_LALT] and keys[pygame.K_F4]) or (keys[pygame.K_LCTRL] and keys[pygame.K_c])):
            # Comando per chiudere la libreria grafica
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE or event.key == pygame.K_LALT and event.key == pygame

# Starting "Game Loop"
while True:
    isQuitting()

    # erases the entire screen surface
    myWindow.fill(pygame.Color("black"))

    # Getting PIR sensor data
    if rasp:
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
        if ('-d' in str(sys.argv) or '--debug' in str(sys.argv)):
            delayTime = 5
        sleep(delayTime)

    # Refreshing screen
    pygame.display.flip()
