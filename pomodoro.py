import time, os

def countdown(minutes):
	  while minutes > 0:
		  seconds = 60
		  minutes = minutes -1
		  while seconds != 0:
			seconds = seconds -1
			time.sleep(1)
			os.system('clear')
			print minutes,':',seconds


countdown(20)

