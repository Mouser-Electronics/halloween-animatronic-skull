import RPi.GPIO as GPIO
import time
from pygame import mixer

mixer.init()
eyes_servo = 13
jaw_servo = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(eyes_servo, GPIO.OUT)
GPIO.setup(jaw_servo, GPIO.OUT)


SENSOR_PIN = 23

 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)


pwm_eyes = GPIO.PWM(eyes_servo, 50) # GPIO 13 for PWM with 50Hz
pwm_jaw = GPIO.PWM(jaw_servo, 50) 

pwm_jaw.start(2.5) # Initialization
pwm_eyes.start(7)
time.sleep(1)
pwm_eyes.ChangeDutyCycle(0)
pwm_jaw.ChangeDutyCycle(0)

def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement!')
    # first scenario
    mixer.music.load('/home/pi/halloween/scream_2.mp3')
    mixer.music.play()
    
    pwm_jaw.ChangeDutyCycle(6) # open jaw
    time.sleep(0.5)
    pwm_jaw.ChangeDutyCycle(0)
    time.sleep(0.2)
    
    
    pwm_eyes.ChangeDutyCycle(6)
    time.sleep(0.2)
    pwm_eyes.ChangeDutyCycle(8)
    time.sleep(0.2)
    pwm_eyes.ChangeDutyCycle(6)
    time.sleep(0.2)
    pwm_eyes.ChangeDutyCycle(7)
    time.sleep(0.2)
    pwm_eyes.ChangeDutyCycle(0)
    
    pwm_jaw.ChangeDutyCycle(2.5) # close jaw
    time.sleep(0.5)
    pwm_jaw.ChangeDutyCycle(0)
    time.sleep(0.5)
    
    # second scenario
    
    for x in range(0,2):
        
        mixer.music.load('/home/pi/halloween/scream_3.mp3')
        mixer.music.play()
        pwm_jaw.ChangeDutyCycle(6) # open jaw
        time.sleep(0.2)
        pwm_jaw.ChangeDutyCycle(0)
        time.sleep(0.2)
        
        pwm_eyes.ChangeDutyCycle(6)
        time.sleep(0.2)
        pwm_eyes.ChangeDutyCycle(8)
        time.sleep(1)
        pwm_eyes.ChangeDutyCycle(6)
        time.sleep(0.2)
        pwm_eyes.ChangeDutyCycle(7)
        time.sleep(0.2)
        pwm_eyes.ChangeDutyCycle(6)
        time.sleep(0.2)
        pwm_eyes.ChangeDutyCycle(8)
        time.sleep(1)
        pwm_eyes.ChangeDutyCycle(7)
        time.sleep(0.2)
        pwm_eyes.ChangeDutyCycle(0)

        pwm_jaw.ChangeDutyCycle(2.5) # close jaw
        time.sleep(0.5)
        pwm_jaw.ChangeDutyCycle(0)
        time.sleep(0.5)
        mixer.music.stop()
    
    for i in range(0,2):
        pwm_jaw.ChangeDutyCycle(6) # open jaw
        pwm_eyes.ChangeDutyCycle(6)
        time.sleep(0.2)
        pwm_jaw.ChangeDutyCycle(2.5) # close jaw
        pwm_eyes.ChangeDutyCycle(8)
        time.sleep(0.2)
        pwm_jaw.ChangeDutyCycle(6) # open jaw
        pwm_eyes.ChangeDutyCycle(7)
        time.sleep(0.2)
        pwm_jaw.ChangeDutyCycle(2.5) # close jaw
        pwm_eyes.ChangeDutyCycle(6)
        time.sleep(0.2)
        pwm_jaw.ChangeDutyCycle(6) # open jaw
        pwm_eyes.ChangeDutyCycle(7)
        time.sleep(0.2)
        pwm_jaw.ChangeDutyCycle(2.5) # close jaw
        time.sleep(0.2)
    pwm_eyes.ChangeDutyCycle(0)
    pwm_jaw.ChangeDutyCycle(0)
    time.sleep(2)

    print('motor function ended')
    
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print ("Finish...")
GPIO.cleanup()
pwm_eyes.stop()
pwm_jaw.stop()