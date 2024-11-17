import pygame 

pygame.init()

#setzt die bildschirmgöße fest
gameDisplay = pygame.display.set_mode((1080,720))
#Fenster name wird festgelegt
pygame.display.set_caption("Space Shooter")
#FPS bzw Ticks pro sekunde
clock = pygame.time.Clock()
#Das Raumschiff is nicht zerstört
exploded = False 

while not exploded:
#Erzeugt eine Liste mit Events die PAssiern pro Frame pro Sekunde ist eine Pygame methode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exploded = True
# Gibt die Evnets zu Kontrolle in der Konsole aus
        print(event)
#mit dieser methode kann man alle und spezifische parameter aktuallisieren
    pygame.display.update()

#FPS die Zahl ist quasi FPS es läuft die ganze schleife in dieser geschwingikeit 
    clock.tick(60)

#Pygame verlassen
pygame.quit()
#Python verlassen
quit()