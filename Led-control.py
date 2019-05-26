import RPi.GPIO as GPIO
import time
print("Welcome to LED-light control for raspberry pi!")
print("")
print("|    |-- |-|")
print("|    |-- |  |")
print("|--- |-- |-|")
print("")
print("Made by The Leo Developer")
print("")
print("Enter color:")
print("1 - Red")
print("2 - Green")
print("3 - Blue")
print("4 - Pink")
print("5 - Yellow")
print("6 - Rainbow")
color = int(input("Enter your choise:"))
print("Enter blink style:")
print("1 - Just glow")
print("2 - Blink")
print("3 - Off")
style = int(input("Enter your choise:"))
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
if color==1 and style==1:
	GPIO.output(14,GPIO.HIGH)
elif color==2 and style==1:
	GPIO.output(15,GPIO.HIGH)
elif color==3 and style==1:
	GPIO.output(18,GPIO.HIGH)
elif color==1 and style==2:
	print("Press CTRL+C to stop")
	while True:
		GPIO.output(14,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(14,GPIO.LOW)
		time.sleep(1)
elif color==2 and style==2:
	print("Press CTRL+C to stop")
	while True:
		GPIO.output(15,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(15,GPIO.LOW)
		time.sleep(1)
elif color==3 and style==2:
	print("Press CTRL+C to stop")
	while True:
		GPIO.output(18,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(18,GPIO.LOW)
		time.sleep(1)
elif color==1 and style==3:
	GPIO.output(14,GPIO.LOW)
elif color==2 and style==3:
	GPIO.output(15,GPIO.LOW)
elif color==3 and style==3:
	GPIO.output(18,GPIO.LOW)
elif color==4 and style==1:
	GPIO.output(14,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(18,GPIO.HIGH)
elif color==4 and style==2:
	print("Press CTRL+C to stop")
	while True:
		GPIO.output(14,GPIO.HIGH)
		GPIO.output(15,GPIO.HIGH)
		GPIO.output(18,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(14,GPIO.LOW)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		time.sleep(1)
elif color==4 and style==3:
	GPIO.output(14,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)
elif color==6 and style==1:
	GPIO.output(14,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(15,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(18,GPIO.HIGH)
elif color==5 and style==1:
	GPIO.output(14,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)
elif color==5 and style==2:
	print("Press CTRL+C to stop")
	while True:
		GPIO.output(14,GPIO.HIGH)
		GPIO.output(15,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(14,GPIO.LOW)
		GPIO.output(15,GPIO.LOW)
		time.sleep(1)
elif color==5 and style==3:
	GPIO.output(14,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
elif color==6 and style==2:
	print("Press CTRL+C to stop")
	while True:
		GPIO.output(14,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(14,GPIO.LOW)
		time.sleep(1)
		GPIO.output(15,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(15,GPIO.LOW)
		time.sleep(1)
		GPIO.output(18,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(18,GPIO.LOW)
		time.sleep(1)
elif color==6 and style==3:
	GPIO.output(14,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)
else:
	print("Invalid input!")
