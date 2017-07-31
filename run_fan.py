import RPi.GPIO as GPIO #use "pin commands"
import os as os #popon to read temperature

FAN_PIN = 4 #GPIO04 or BOARD 7
GPIO.setwarnings(False) #just for not write warnings
GPIO.setmode(GPIO.BCM) #setting mode BCM instead BOARD (read more about it)
GPIO.setup(FAN_PIN, GPIO.OUT) #making a GPIO an output


def getCPUtemperature():
        temp = os.popen('vcgencmd measure_temp').readline()
        temp = temp.replace('temp=','').replace('\'C\n','') #formatting to float
        temp = float(temp)
        return temp

while(True):
        if getCPUtemperature() > 60.00: #max temperature until the fan turn on
            GPIO.output(FAN_PIN, 1) #set 1/True/HIGH to turn on the fan
        else:
        	GPIO.output(FAN_PIN, 0) #set 0/False/LOW to turn off the fan