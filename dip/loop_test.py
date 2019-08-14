import pygame
import time
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
pygame.mixer.init(22050,-16,1,2048)
bang = pygame.mixer.Sound("./music/C4.wav")
pygame.mixer.set_num_channels(8)
Doo = pygame.mixer.Channel(0)
#bang = pygame.mixer.Sound("./music/Audio_Pop01_15sec.wav")
Doo.set_volume(0.1)
Doo.play(bang,3,0,0)
while(1):
	None

