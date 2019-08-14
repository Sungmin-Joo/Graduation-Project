import pygame
import time
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_UP)
pygame.mixer.init(22050,-16,1,8)
Do = pygame.mixer.Sound("./music/C4.wav")
Le = pygame.mixer.Sound("./music/D4.wav")
#Bang = pygame.mixer.Sound("./music/Audio_Pop01_15sec.wav")
Do.set_volume(0.1)
Le.set_volume(0.1)
while(1):
	if GPIO.input(17) == 0:
		print('A')
		Le.set_volume(0.3)
		Le.play()
		while(1):
			'''
			if pygame.mixer.get_busy():
				pass
			else:
				bang.play()
			'''
			if GPIO.input(17) == 1:
				Le.fadeout(500)
				time.sleep(0.01)
				break
	if GPIO.input(20) == 0:
		print('A')
		Do.set_volume(0.3)
		Do.play()
		while(1):
			'''
			if pygame.mixer.get_busy():
				pass
			else:
				bang.play()
			'''
			if GPIO.input(20) == 1:
				Do.fadeout(500)
				time.sleep(0.01)
				break
				
				
				
'''				
bang = pygame.mixer.Sound("Audio_Pop01_15sec.wav")
pygame.mixer.init(22050,-16,2,2048)'''
'''
pygame.mixer.music.load("Audio_Pop01_15sec.wav")
pygame.mixer.music.play()
time.sleep(2.0)
pygame.mixer.music.stop()
time.sleep(2.0)
pygame.mixer.music.play()
'''
'''
bang = pygame.mixer.Sound("Audio_Pop01_15sec.wav")
bang.play()
time.sleep(2.0)
bang.fadeout(1000)
time.sleep(2.0)
bang.play()

while 1:
	if pygame.mixer.get_busy() == False:
		break
	time.sleep(0.5)
	bang.set_volume(0.1) 
'''
