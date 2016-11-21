# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:51:22 2016

@author: Roman
"""

import Queue, threading, time
import numpy as np
from tc08usb import TC08USB, USBTC08_TC_TYPE, USBTC08_ERROR#, USBTC08_UNITS

class PicoLog():
    def __init__(self):
        self.__numChannels = {0:False,
                              1:True,
                              2:False,
                              3:False,
                              4:False,
                              5:False,
                              6:False,
                              7:False,
                              8:False}
                              
        

class MonitorTC08USBThread(threading.Thread):
    def __init__(self, device, dataQ):
        threading.Thread.__init__(self)
        
        self.dataQ = dataQ
        self.alive = threading.Event()
        self.alive.set()    
        self.tc08 = device
        self.tc08.set_mains(50)
        self.tc08.set_channel(1, USBTC08_TC_TYPE.K)
        self.tc08.set_channel(2, USBTC08_TC_TYPE.K)
        
    def join(self, timeout = None):
        self.alive.clear()
        threading.Thread.join(self, timeout) 
        
    def run(self):
        while self.alive.isSet():
            self.tc08.get_single()
            temp = self.tc08[1]
            temp2 = self.tc08[2]
            #print(temp, temp2)
            self.dataQ.put((temp, temp2))