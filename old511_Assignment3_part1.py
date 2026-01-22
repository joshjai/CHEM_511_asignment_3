from machine import Pin, I2C, ADC 
import i2c_lcd
import time

#setup

i2c_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(i2c_device, 0x27, 2, 16)


potentiometer = ADC(Pin(34))
potentiometer.ATTN_11DB
count = 0

while True:
    lcd.clear()
    reading = potentiometer.read()
    maximum = reading
    minimum = reading
    lcd.move_to(0, 0)
    lcd.putstr('reading: %d' % reading)
    lcd.move_to(0,1) 
    lcd.putstr(f'+ {maximum}')
    lcd.move_to(8,1) 
    lcd.putstr(f'- {minimum}')
    count +=1
    time.sleep(1)
    
    
