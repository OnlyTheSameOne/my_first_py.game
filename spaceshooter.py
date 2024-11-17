import pygame 

pygame.init()
# Dynamische Dsipalygröße als Parmeter für die set_mode
display_height = 720
display_width = 1080

#Fraben im RGB-System
balck = (0,0,0)
white = (255,255,255)

#setzt die bildschirmgöße fest
gameDisplay = pygame.display.set_mode((display_height,display_width))
#Fenster name wird festgelegt
pygame.display.set_caption("Space Shooter")
#FPS bzw Ticks pro sekunde
clock = pygame.time.Clock()
#generiere das Space Ship in den Hintergrund
spaceShip = pygame.image.load("Charakter_models\output-onlinepngtools.png")

#Funktion die Das SPaceShip mit der blit methode an dern psoition x & y erzeugt 
#dabei ist spaceShip ein Parameter mit den werten von (x,y)
def ship(x,y):
    gameDisplay.blit(spaceShip,(x,y))

#Das kordinaten-System in Pygame starte oben link vom Bildschirm P(0/0)
#Positve X werte bringen den den Punkt nach rechts
#Positive Y werte bringen den Punk nach links
x = (display_height  * 0.1)
y =  (display_width * 0.1) 





#Das Raumschiff is nicht zerstört
exploded = False 

while not exploded:
#Erzeugt eine Liste mit Events die Passiern pro Frame pro Sekunde ist eine Pygame methode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exploded = True
# Gibt die Evnets zu Kontrolle in der Konsole aus
       #print(event)
#Zuerst erzeugen wir den weißen Hintergrund
    gameDisplay.fill(white)
#Danch Erzeugen wir das Space Ship    
    ship(x,y)
#mit dieser methode kann man alle und spezifische parameter aktuallisieren
    pygame.display.update()

#FPS die Zahl ist quasi FPS es läuft die ganze schleife in dieser geschwingikeit 
    clock.tick(60)

#Pygame verlassen
pygame.quit()
#Python verlassen
quit()