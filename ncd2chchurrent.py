# NCD.io two-channel ADS1115/INA196 current readout driver
# Kaveh Pezeshki
# 6/17/2021
# kpezeshki@hmc.edu

# NOTE: breakout requires 5V signaling. Use level shifter with a Raspberry Pi
# NOTE: this driver requires the Adafruit ADS1x15 library to be installed

import Adafruit_ADS1x15

class CurrentSensor:

    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115()

    def read_channel(self, channel):
        # channel: channel to measure, 0 or 1
        # returns: measured current in mA

        adc_val = self.adc.read_adc(channel, gain=2)
        current = adc_val*6.22e-4
        return current 

#-------------------------------------------

import time
sensor = CurrentSensor()

while(1):
    #print(sensor.read_channel(0), sensor.read_channel(1))
    print(sensor.read_channel(0))

    
