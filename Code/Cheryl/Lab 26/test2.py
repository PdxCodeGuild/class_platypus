import pygame
import time
pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("access_library_computer.wav")

sounda.play()

time.sleep(3)
# sounda.stop()