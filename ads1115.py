'''!
  @file demo_read_voltage.py
  @brief connect ADS1115 I2C interface with your board (please reference board compatibility)
  @n  The voltage value read by A0 A1 A2 A3 is printed through the serial port.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author [luoyufeng](yufeng.luo@dfrobot.com)
  @version  V1.0
  @date  2019-06-19
  @url https://github.com/DFRobot/DFRobot_ADS1115
'''

import os
import time
import DFRobot_ADS1115

#from DFRobot_ADS1115 import ADS1115

ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16

ads = DFRobot_ADS1115.ADS1115()

while True :
    #Set the IIC address
    ads.set_addr_ADS1115(0x48)
    #Sets the gain and input voltage range.
    ads.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
    
    #Get the Digital Value of Analog of selected channel
    a0 = ads.read_voltage(0)['r']
    time.sleep(0.2)
    a1 = ads.read_voltage(1)['r']
    time.sleep(0.2)
    a2 = ads.read_voltage(2)['r']
    time.sleep(0.2)
    a3 = ads.read_voltage(3)['r']
    time.sleep(0.2)
    
    print("%dmV %dmV %dmV %dmV" % (a0, a1, a2, a3))
