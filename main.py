import pygame #pygame library
from time import sleep #time module , sleep function
pygame.init() #intializing pygame
window = pygame.display.set_mode((0 , 0), pygame.FULLSCREEN)
pygame.mixer.init() #mixer function
pygame.mixer.music.load('amma end.mp3') #loading songs
pygame.mixer.music.play() # playing
image1 = pygame.image.load('maa2.jpg') # backgroung image loading
window.blit(image1,(0,0)) #whole window
pygame.display.update() #updating
sleep(5.5) #song plays for 5 seconds
image = pygame.image.load('mother3.jpg')
window.blit(image,(0,0))
pygame.display.update()
sleep(5.5)
image2 = pygame.image.load('mother4.jpg')
window.blit(image2,(0,0))
pygame.display.update()
sleep(5.5)
image3 = pygame.image.load('mother5.jpg')
window.blit(image3,(0,0))
pygame.display.update()
sleep(5.5)
image4 = pygame.image.load('mother6.jpg')
window.blit(image4,(0,0))
pygame.display.update()
sleep(5.5)
image5 = pygame.image.load('mother7.jpg')
window.blit(image5,(0,0))
pygame.display.update()
sleep(5.5)
image6 = pygame.image.load('mother8.jpg')
window.blit(image6,(0,0))
pygame.display.update()
sleep(7.5)
